#!/bin/sh
# SDL_AUDIOCVT_PACKED also causes trouble
# Get rid of most of the stdef functions, all have Python equivalents
# Doesn't like inlined SDL_RectEmpty etc functions
# Keydefs are char constants not numeric
# No SDL_dummy structs / typedefs
# Also SDL_WINDOW_FULLSCREEN_DESKTOP
cpp -D _SDL_endian_h -D SDL_FORCE_INLINE= -D DECLSPEC= -D SDLCALL= -I /usr/include/SDL2 < /usr/include/SDL2/SDL.h | filtercdefs.py > _sdl/sdl.h
