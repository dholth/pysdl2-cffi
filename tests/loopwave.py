#
# Copyright (C) 1997-2014 Sam Lantinga <slouken@libsdl.org>
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely.
#

# Program to load a wave file and loop playing it using SDL sound

# loopwaves.c is much more robust in handling WAVE files --
#    This is only for simple WAVEs

import sys
from __sdl import lib, ffi

class wave():
    spec = ffi.new("SDL_AudioSpec *")
    sound_p = ffi.new("uint8_t **")
    soundlen_p = ffi.new("uint32_t *")
    soundpos = 0
    soundlen = 0

def SDL_Log(message):
    sys.stderr.write(message)

SDL_LogError = SDL_Log

# Call this instead of exit(), so we can clean up SDL: atexit() is evil.
def quit(rc):
    lib.SDL_Quit()
    sys.exit(rc)

def fillerup(unused, stream, len):
    # print("fillerup", stream, len)
    # Set up the pointers
    waveptr = wave.sound_p[0] + wave.soundpos
    waveleft = wave.soundlen_p[0] - wave.soundpos

    # Go!
    while waveleft <= len:
        lib.SDL_memcpy(stream, waveptr, waveleft)
        stream += waveleft
        len -= waveleft
        waveptr = wave.sound_p[0]
        waveleft = wave.soundlen_p[0]
        wave.soundpos = 0
    lib.SDL_memcpy(stream, waveptr, len)
    wave.soundpos += len

done = 0
def poked(sig):
    global done
    done = 1

def main():
    # Enable standard application logging
    lib.SDL_LogSetPriority(lib.SDL_LOG_CATEGORY_APPLICATION, lib.SDL_LOG_PRIORITY_INFO)

    # Load the SDL library
    if lib.SDL_Init(lib.SDL_INIT_AUDIO) < 0:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION,
                     "Couldn't initialize SDL: %s\n" % (lib.SDL_GetError()))
        return 1

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "sample.wav"

    # Load the wave file into memory
    rwops = lib.SDL_RWFromFile(filename, "rb")

    if lib.SDL_LoadWAV_RW(rwops,
                      1,
                      wave.spec,
                      wave.sound_p,
                      wave.soundlen_p) == ffi.NULL:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION,
                     "Couldn't load %s: %s\n" % (filename, lib.SDL_GetError()))
        quit(1)
    else:
        print("Loaded " + filename)

    wave.spec.callback = ffi.callback("SDL_AudioCallback", fillerup)


    # Show the list of available drivers
    lib.SDL_Log("Available audio drivers:")
    for i in range(lib.SDL_GetNumAudioDrivers()):
        lib.SDL_Log("%i: %s" % (i, ffi.string(lib.SDL_GetAudioDriver(i))))

    # Initialize fillerup() variables
    if lib.SDL_OpenAudio(wave.spec, ffi.NULL) < 0:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION,
                     "Couldn't open audio: %s\n" % (lib.SDL_GetError()))
        lib.SDL_FreeWAV(wave.sound)
        quit(2)

    lib.SDL_Log("Using audio driver: %s\n" % (ffi.string(lib.SDL_GetCurrentAudioDriver())))

    # Let the audio run
    lib.SDL_PauseAudio(0)
    while not done and (lib.SDL_GetAudioStatus() == lib.SDL_AUDIO_PLAYING):
        lib.SDL_Delay(1000)

    # Clean up on signal
    lib.SDL_CloseAudio()
    lib.SDL_FreeWAV(wave.sound_p[0])
    lib.SDL_Quit()
    return 0

if __name__ == "__main__":
    main()
