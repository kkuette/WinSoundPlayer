# WinSoundPlayer
Pythonic minimal sound player for windows

I've just enhanced a bit the [playsound](https://github.com/TaylorSMarks/playsound) project with start and stop functions.

## How to use
```
player = playsound(sound, block=False) # Init with the sound you want
player.play_sound()                    # and just start it
player.stop_sound()                    # Stop it when you want with a condition
```
