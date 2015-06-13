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
# This file is created by : Nitin Jain (nitin.j4@samsung.com)
#

# Sample program:  Draw a Chess Board  by using SDL_CreateSoftwareRenderer API

from __sdl import lib, ffi

def SDL_LogSetPriority(*args):
    pass

def SDL_LogError(*args):
    pass

def DrawChessBoard(renderer):
    row = 0
    coloum = 0
    x = 0
    rect = ffi.new("SDL_Rect *")
    darea = ffi.new("SDL_Rect *")

    # Get the Size of drawing surface
    lib.SDL_RenderGetViewport(renderer, darea)

    for row in range(8):
        coloum = row%2
        x = x + coloum

        for coloum in range(coloum, 4+(row%2)):

            lib.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0xFF)

            rect.w = darea.w//8
            rect.h = darea.h//8
            rect.x = x * rect.w
            rect.y = row * rect.h
            x = x + 2
            lib.SDL_RenderFillRect(renderer, rect)

        x = 0

def main():
    # Enable standard application logging
    lib.SDL_LogSetPriority(lib.SDL_LOG_CATEGORY_APPLICATION, lib.SDL_LOG_PRIORITY_INFO)

    # Initialize SDL
    if lib.SDL_Init(lib.SDL_INIT_VIDEO) != 0:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION, "lib.SDL_Init fail : %s\n" % (lib.SDL_GetError()))
        return 1


    # Create window and renderer for given surface
    window = lib.SDL_CreateWindow("Chess Board", lib.SDL_WINDOWPOS_UNDEFINED, lib.SDL_WINDOWPOS_UNDEFINED, 640, 640, lib.SDL_WINDOW_SHOWN)
    if not window:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION, "Window creation fail : %s\n" % (lib.SDL_GetError()))
        return 1
    surface = lib.SDL_GetWindowSurface(window)
    renderer = lib.SDL_CreateSoftwareRenderer(surface)
    if not renderer:
        lib.SDL_LogError(lib.SDL_LOG_CATEGORY_APPLICATION, "Render creation for surface fail : %s\n" % (lib.SDL_GetError()))
        return 1

    # Clear the rendering surface with the specified color
    lib.SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF)
    lib.SDL_RenderClear(renderer)

    # Draw the Image on rendering surface
    e = ffi.new("SDL_Event *")
    while True:
        if lib.SDL_PollEvent(e):
            if e.type == lib.SDL_QUIT:
                break

            if e.key.keysym.sym == lib.SDLK_ESCAPE:
                break

        DrawChessBoard(renderer)

        # Got everything on rendering surface,
        # now Update the drawing image on window screen
        lib.SDL_UpdateWindowSurface(window)

if __name__ == "__main__":
    main()
