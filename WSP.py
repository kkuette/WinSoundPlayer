from ctypes import c_buffer, windll
from random import random
from time   import sleep
from sys    import getfilesystemencoding

def winCommand(*command):
    buf = c_buffer(255)
    command = ' '.join(command).encode(getfilesystemencoding())
    errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))
    if errorCode:
        errorBuffer = c_buffer(255)
        windll.winmm.mciGetErrorStringA(errorCode, errorBuffer, 254)
        exceptionMessage = ('\n    Error ' + str(errorCode) + ' for command:'
                            '\n        ' + command.decode() +
                            '\n    ' + errorBuffer.value.decode())
        raise PlaysoundException(exceptionMessage)
    return buf.value

class WinSoundPlayer(object):
    '''
    Utilizes windll.winmm. Tested and known to work with MP3 and WAVE on
    Windows 7 with Python 2.7. Probably works with more file formats.
    Probably works on Windows XP thru Windows 10. Probably works with all
    versions of Python.
    Inspired by (but not copied from) Michael Gundlach <gundlach@gmail.com>'s mp3play:
    https://github.com/michaelgundlach/mp3play
    I never would have tried using windll.winmm without seeing his code.
    '''

    def __init__(self, sound, block=True):
        self.alias = 'playsound_' + str(random())
        self.sound = sound
        self.block = block
        self.open_sound()
        self.set_sound()
        self.status_sound()

    def open_sound(self):
        winCommand('open "' + self.sound + '" alias', self.alias)

    def set_sound(self):
        winCommand('set', self.alias, 'time format milliseconds')

    def status_sound(self):
        self.durationInMS = winCommand('status', self.alias, 'length')

    def play_sound(self):
        winCommand('play', self.alias, 'from 0 to', self.durationInMS.decode())
        if self.block:
            sleep(float(self.durationInMS) / 1000.0)

    def stop_sound(self):
        winCommand('close', self.alias)
