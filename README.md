# WinSoundPlayer
Pythonic minimal sound player for windows

I've just enhanced a bit the [playsound](https://github.com/TaylorSMarks/playsound) project with start and stop functions.

## How to use
```
self.lector = playsound(sound, block=False) # Init with the sound you want
self.lector.play_sound()                    # and just start it
self.lector.stop_sound()                    # Stop it when you want with a condition
```
