SDL_ttf API
===========

The `sdl.ttf` module exposes the `SDL_ttf` API without the `TTF_` prefix.

Many of these functions have `Text`, `UTF8`, and `UNICODE` variants. It's
recommended to only use the `UTF8` variant, since `pysdl2-cffi`
automatically converts to and from utf-8 when passing `char *` to C.

See also http://www.libsdl.org/projects/SDL_ttf/

.. automodule:: sdl.ttf
    :members:
    :undoc-members:
