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

import sys

from __sdl import lib, ffi

def SDL_Log(message):
    sys.stderr.write(message)

def print_devices(iscapture):
    typestr = "capture" if iscapture else "output"
    n = lib.SDL_GetNumAudioDevices(iscapture)

    print("%s devices" % typestr)

    if n == -1:
        lib.SDL_Log("  Driver can't detect specific %s devices.\n\n" % (typestr))
    elif n == 0:
        lib.SDL_Log("  No %s devices found.\n\n" % (typestr))
    else:
        for i in range(n):
            lib.SDL_Log("  %s\n" % ffi.string(lib.SDL_GetAudioDeviceName(i, iscapture),))
        lib.SDL_Log("\n")

def main():
    # Enable standard application logging
    lib.SDL_LogSetPriority(lib.SDL_LOG_CATEGORY_APPLICATION, lib.SDL_LOG_PRIORITY_INFO)

    # Load the SDL library
    if lib.SDL_Init(lib.SDL_INIT_AUDIO) < 0:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION, "Couldn't initialize SDL: %s\n" % (lib.SDL_GetError()))
        return (1)

    # Print available audio drivers
    n = lib.SDL_GetNumAudioDrivers()
    if n == 0:
        lib.SDL_Log("No built-in audio drivers\n\n")
    else:
        lib.SDL_Log("Built-in audio drivers:\n")
        for i in range(n):
            lib.SDL_Log("  %s\n" % ffi.string(lib.SDL_GetAudioDriver(i)))
        lib.SDL_Log("\n")

    lib.SDL_Log("Using audio driver: %s\n\n" % ffi.string(lib.SDL_GetCurrentAudioDriver()))

    print_devices(0)
    print_devices(1)

    lib.SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())

