from raylibpy import *
import winsound

class RaylibAudioService:
    def __init__(self):
        """
            Everything that has to do with sound...
        """
        init_audio_device()
        self._sound_cache = {}

    def _load_sound(self, path):
        """
            - Load in the sound
            - Store the sound to cache
            - return the sound
        """
        sound = load_sound(path)
        self._sound_cache[path] = sound
        return sound

    def play_sound(self, path, volume : float = 1):
        """
            Play a sound given:
                - the path to the sound file (a string)
                - the volume: goes from 0 to 1
        """
        winsound.PlaySound(path, winsound.SND_ASYNC)