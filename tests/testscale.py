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
# Simple program:  Move N sprites around on the screen as fast as possible

# Translated to Python by Daniel Holth <dholth@fastmail.fm>

import sys
import time

import sdl
from sdl import ffi

#include "sdl.test_common.h"

WINDOW_WIDTH	= 640
WINDOW_HEIGHT	= 480

class DrawState(object):
    def __init__(self):
        self.window = None
        self.renderer = None
        self.background = None
        self.sprite = None
        self.sprite_rect = sdl.Rect()
        self.scale_direction = 0

# Call this instead of exit(), so we can clean up SDL: atexit() is evil.
def quit(rc):
    # SDLTest_CommonQuit(state)
    sys.exit(rc)

def LoadTexture(renderer, file, transparent):
    # Load the sprite image
    rwops = sdl.RWFromFile(file, 'r')
    temp = sdl.loadBMP_RW(rwops, True)
    if temp == ffi.NULL:
        sys.stderr.write("Couldn't load %s: %s\n" % (file, sdl.getError()))
        return None

    # Set transparent pixel as the pixel at (0,0)
    if transparent:
        if temp.format.palette:
            sdl.setColorKey(temp, True, ffi.cast("uint8_t *", temp.pixels)[0])
        else:
            # TODO ffi.cast to correct-width type
            bpp = temp.format.BitsPerPixel
            if bbp == 15:
                sdl.setColorKey(temp, True, temp.pixels[0] & 0x00007FFF)
            elif bpp == 16:
                sdl.setColorKey(temp, sdl.TRUE, temp.pixels[0])
            elif bpp == 24:
                sdl.setColorKey(temp, True, temp.pixels[0] & 0x00FFFFFF)
            elif bpp == 32:
                sdl.setColorKey(temp, True, temp.pixels[0])

    # Create textures from the image
    texture = sdl.createTextureFromSurface(renderer, temp)
    sdl.freeSurface(temp)
    if not texture:
        sys.stderr.write("Couldn't create texture: %s\n" % (sdl.getError()))
        return None

    # We're ready to roll. :)
    return texture

def Draw(s):
    viewport = sdl.Rect()
    sdl.renderGetViewport(s.renderer, viewport)

    # Draw the background
    sdl.renderCopy(s.renderer, s.background, None, None)

    # Scale and draw the sprite
    s.sprite_rect.w += s.scale_direction
    s.sprite_rect.h += s.scale_direction
    if s.scale_direction > 0:
        if s.sprite_rect.w >= viewport.w or s.sprite_rect.h >= viewport.h:
            s.scale_direction = -1
    else:
        if s.sprite_rect.w <= 1 or s.sprite_rect.h <= 1:
            s.scale_direction = 1
    s.sprite_rect.x = (viewport.w - s.sprite_rect.w) // 2
    s.sprite_rect.y = (viewport.h - s.sprite_rect.h) // 2

    sdl.renderCopy(s.renderer, s.sprite, ffi.NULL, s.sprite_rect)

    # Update the screen!
    sdl.renderPresent(s.renderer)

def main():
    event = sdl.Event()

    sdl.init(sdl.INIT_VIDEO)

    # Initialize test framework
#    state = SDLTest_CommonCreateState(argv, sdl.INIT_VIDEO)
#     if not state:
#         return 1

#     for (i = 1; i < argc;) {
#
#         consumed = SDLTest_CommonArg(state, i)
#         if consumed == 0:
#             sdl.Log("Usage: %s %s\n" % (argv[0], SDLTest_CommonUsage(state)))
#             return 1
#         i += consumed
#     if not SDLTest_CommonInit(state):
#         quit(2)

    drawstates = [DrawState()]
    for i in range(len(drawstates)):
        drawstate = drawstates[i]

        drawstate.window = sdl.createWindow("Scale %d" % i,
                                            sdl.WINDOWPOS_UNDEFINED,
                                            sdl.WINDOWPOS_UNDEFINED,
                                            WINDOW_WIDTH,
                                            WINDOW_HEIGHT,
                                            sdl.WINDOW_SHOWN)

        drawstate.renderer = sdl.createRenderer(drawstate.window, -1, 0)
        drawstate.sprite = LoadTexture(drawstate.renderer, "icon.bmp", True)
        drawstate.background = LoadTexture(drawstate.renderer, "sample.bmp", False)
        if not drawstate.sprite or not drawstate.background:
            quit(2)
        rc, format, access, w, h = sdl.queryTexture(drawstate.sprite)
        drawstate.sprite_rect.w = w
        drawstate.sprite_rect.h = h
        drawstate.scale_direction = 1

    # Main render loop
    frames = 0
    then = sdl.getTicks()
    done = 0
    while not done:
        # Check for events
        frames += 1
        while sdl.pollEvent(event):
            if event.type == sdl.QUIT:
                done = 1
        for i in range(len(drawstates)):
            if not drawstates[i].window:
                continue
            Draw(drawstates[i])

    # Print out some timing information
    now = sdl.getTicks()
    if now > then:
        fps = (frames * 1000) / (now - then)
        sys.stderr.write("%2.2f frames per second\n" % (fps))

    # TODO for x in drawstates: free stuff

    quit(0)
    return 0

if __name__ == "__main__":
    main()
