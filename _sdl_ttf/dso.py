# dlopen the SDL library.

from .cdefs import ffi

# strategy from cairocffi
def dlopen(ffi, *names):
    """Try various names for the same library, for different platforms."""
    for name in names:
        try:
            return ffi.dlopen(name)
        except OSError:
            pass
    # Re-raise the exception.
    return ffi.dlopen(names[0]) # pragma: no cover

_LIB = dlopen(ffi,
              'SDL2_ttf',
              'libSDL2_ttf.so',
              'libSDL2_ttf-2.0.so.0')