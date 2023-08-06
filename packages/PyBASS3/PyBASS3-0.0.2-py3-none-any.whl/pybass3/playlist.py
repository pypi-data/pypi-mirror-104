
import enum
from pathlib import Path
import random

from .bass_module import BassException
from .song import Song


class PlaylistState(enum.Enum):
    stopped = enum.auto()
    playing = enum.auto()
    paused = enum.auto()
    error = enum.auto()


class PlaylistMode(enum.Enum):
    loop_single = enum.auto()
    loop_all = enum.auto()
    one_time = enum.auto()

    sequential = enum.auto()
    random = enum.auto()

    progress_on_error = enum.auto()
    die_on_error = enum.auto()

class Playlist:

    VALID_TYPES = [".mp3", ".mp4", ".ogg", ".opus"]

    songs: dict # The songs the playlist knows about
    queue: list # The order songs will be played in
    state: PlaylistState # Is the playlist playing songs, stopped, or paused?
    mode: PlaylistMode # Is the playlist running sequential or random
    play_mode: PlaylistMode # is the playlist looping the whole queue, just a song, or running to end?

    queue_position: int  # Where is the playlist in the current queue
    _current_song: Song # What is currently playing
    fadein_song: Song # if fade_in is not None, this is the next song to play
    fade_in: int # How soon should the next song start playing, None if lock step
    song_cls: Song # What is the container for a song (eg Song or QtSong)



    def __init__(self, song_cls = Song):
        self.songs = {}
        self.queue = []
        self.state = PlaylistState.stopped
        self.mode = PlaylistMode.sequential
        self.play_mode = PlaylistMode.one_time

        self.error_mode = PlaylistMode.progress_on_error

        self.queue_position = None
        self._current_song = None

        self.fade_in = None
        self.fadein_song = None
        self.song_cls = song_cls

    @property
    def current_song_id(self):
        return self.current.id

    def add_song(self, song_path):
        song = self.song_cls(song_path)
        try:
            song.duration
        except BassException as bexc:
            if bexc.code == 41:
                # bad formatted song
                print(bexc)
                return None
            raise bexc

        else:
            song.free_stream()
            self.songs[song.id] = song
            self.queue.append(song.id)
            return song.id, song

    def get_song_by_row(self, row_position:int) -> Song:
        try:
            key = list(self.songs.keys())[row_position]
        except IndexError:
            return None

        return self.songs[key]

    def get_song_by_id(self, song_id) -> Song:
        return self.songs.get(song_id, None)


    def add_directory(self, dir_path: Path, recurse=True):
        files = (file for file in dir_path.iterdir() if file.is_file() and file.suffix in self.VALID_TYPES)
        dirs = (fdir for fdir in dir_path.iterdir() if fdir.is_dir())

        for song_path in files:
            self.add_song(song_path)

        if recurse is True:
            for fdir in dirs:
                self.add_directory(fdir, recurse)

    @property
    def fadein(self):
        return self.fade_in

    @fadein.setter
    def fadein(self, value):
        self.fade_in = value

    @fadein.deleter
    def fadein(self):
        self.fade_in = None

    def set_randomize(self):
        if self.current is not None:
            self.stop()

        ids = list(self.songs.keys())
        random.shuffle(ids)
        self.queue = ids
        self.mode = PlaylistMode.random
        self.queue_position = 0


    def set_sequential(self):
        if self.current is not None:
            self.stop()

        self.queue = list(self.songs.keys())
        self.mode = PlaylistMode.sequential
        self.queue_position = 0


    def loop_song(self):
        self.play_mode = PlaylistMode.loop_single

    def loop_queue(self):
        self.play_mode = PlaylistMode.loop_all

    @property
    def current(self) -> Song:
        return self._current_song

    @current.setter
    def current(self, new_song):
        if self._current_song is not None:
            if self._current_song.is_playing:
                self._current_song.stop()

            self._current_song.free_stream()

        self._current_song = new_song
        return self._current_song

    @current.deleter
    def current(self):
        if self._current_song is not None:
            if self._current_song.is_playing():
                self._current_song.stop()

            self._current_song.free_stream()

        del self._current_song



    @property
    def upcoming(self) -> Song:
        qpos = self.queue_position + 1
        # Is the next song past the queue's length?
        if qpos >= len(self.queue):
            if self.mode == PlaylistMode.loop_all:
                qpos = 0
            else:
                return None

        song_id = self.queue[qpos]

        return self.songs[song_id]


    @property
    def prior(self):
        qpos = self.queue_position - 1
        if qpos < 0:
            if self.mode == PlaylistMode.loop_all:
                qpos = len(self.songs) - 1
            else:
                return None

        song_id = self.queue[qpos]

        return self.songs[song_id]



    def song_playing(self, song: Song):
        """
            Helper/hook that is intended for event driven Playlist inheriting classes.

            Intentionally empty.

        :param song:
        :return:
        """
        return

    def play(self):

        if self.fadein_song is not None:
            self.fadein_song.play()

        if self.current is None:
            if len(self.queue) == 0:
                if self.mode == PlaylistMode.sequential:
                    self.set_sequential()
                else:
                    self.set_randomize()

            self.queue_position = 0
            current_id = self.queue[self.queue_position]
            self.current = self.songs[current_id]
        self.current.play()

        self.song_playing(self.current)



    def stop(self):
        if self.fadein_song is not None:
            self.fadein_song.stop()

        self.current.stop()


    def pause(self):
        if self.fadein_song is not None:
            self.fadein_song.pause()

        return self.current.pause()


    def restart(self):
        if self.fadein_song is not None:
            self.fadein_song.free_stream()
            self.fadein_song = None

        return self.current.move2position_seconds(0)


    def next(self):
        try:
            return self._next()
        except BassException:
            if self.error_mode == PlaylistMode.progress_on_error:
                self.queue_position += 1
                if self.queue_position > len(self.queue) and self.mode == PlaylistMode.loop_all:
                    self.queue_position = 0

                return self._next()

    def _next(self):

        if self.fadein_song is not None:
            self.current.stop()
            self.current = self.fadein_song
            self.fadein_song = None
            return


        self.current.free_stream()
        self.current = self.upcoming
        self.queue_position += 1
        if self.current is not None:
            self.current.play()
            return


        self.queue_position += 1
        if self.queue_position > len(self.queue) and self.mode == PlaylistMode.loop_all:
            self.queue_position = 0

        song_id = self.queue[self.queue_position]
        return song_id, self.current

    def previous(self):
        try:
            return self._previous()
        except BaseException:
            if self.error_mode == PlaylistMode.progress_on_error:
                self.queue_position -= 1
                if self.queue_position < 0:
                    self.queue_position = len(self.queue)

                return self._previous()
            else:
                raise


    def _previous(self):
        prior = self.prior
        if self.fadein_song is not None:
            self.fadein_song.free_stream()
            self.fadein_song = None
            self.current.move2position_seconds(0)
            self.current.play()
        else:
            self.current.free_stream()
            self.current = prior
            self.current.play()


            self.queue_position -= 1
            if self.queue_position < 0:
                self.queue_position = len(self.queue)

        song_id = self.queue[self.queue_position]
        return song_id, self.current

    def tick(self):
        remaining = self.current.remaining_bytes
        remaining_seconds = self.current.remaining_seconds

        if self.play_mode == PlaylistMode.loop_single and remaining == 0:
            self.current.move2position_seconds(0)

        elif self.fade_in is not None and remaining_seconds <= self.fade_in:
            if self.fadein_song is not None and remaining <= 0:
                self.current.stop()
                self.current.free_stream()
                self.current = self.fadein_song
                self.fadein_song = None
                self.queue_position += 1
            elif self.upcoming is not None:
                self.fadein_song = self.upcoming
                self.fadein_song.play()

        elif remaining <= 0:
            self.current.stop()
            self.current.free_stream()
            self.next()
            self.queue_position += 1
            self.current.play()

    def items(self):
        # TODO yield from instead?
        for song_id, song in self.songs.items():
            yield song_id, song

    def __len__(self):
        return len(self.songs)
