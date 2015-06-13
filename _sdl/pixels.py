# The parts of SDL_pixels.h that can't be parsed by cffi.

from __sdl import lib

SDL_ALPHA_OPAQUE=255
SDL_ALPHA_TRANSPARENT=0

def SDL_FOURCC(A, B, C, D):
    """Return a four-character code as a uint32."""
    return ord(A) | (ord(B)<<8) | (ord(C)<<16) | (ord(D)<<24)

SDL_DEFINE_PIXELFOURCC = SDL_FOURCC

def SDL_DEFINE_PIXELFORMAT(type, order, layout, bits, bytes):
    return ((1 << 28) | ((type) << 24) | ((order) << 20) | ((layout) << 16) |
            ((bits) << 8) | ((bytes) << 0))
def SDL_PIXELFLAG(X):
    return (((X) >> 28) & 0x0F)
def SDL_PIXELTYPE(X):
    return (((X) >> 24) & 0x0F)
def SDL_PIXELORDER(X):
    return (((X) >> 20) & 0x0F)
def SDL_PIXELLAYOUT(X):
    return (((X) >> 16) & 0x0F)
def SDL_BITSPERPIXEL(X):
    return (((X) >> 8) & 0xFF)
def SDL_BYTESPERPIXEL(X):
    if SDL_ISPIXELFORMAT_FOURCC(X):
        if (((X) == lib.SDL_PIXELFORMAT_YUY2) or
            ((X) == lib.SDL_PIXELFORMAT_UYVY) or
            ((X) == lib.SDL_PIXELFORMAT_YVYU)):
            return 2
        return 1
    else:
        return (((X) >> 0) & 0xFF)

def SDL_ISPIXELFORMAT_INDEXED(format):
    return (not SDL_ISPIXELFORMAT_FOURCC(format) and
     ((SDL_PIXELTYPE(format) == lib.SDL_PIXELTYPE_INDEX1) or
      (SDL_PIXELTYPE(format) == lib.SDL_PIXELTYPE_INDEX4) or
      (SDL_PIXELTYPE(format) == lib.SDL_PIXELTYPE_INDEX8)))

def SDL_ISPIXELFORMAT_ALPHA(format):
    return (not SDL_ISPIXELFORMAT_FOURCC(format) and
     ((SDL_PIXELORDER(format) == lib.SDL_PACKEDORDER_ARGB) or
      (SDL_PIXELORDER(format) == lib.SDL_PACKEDORDER_RGBA) or
      (SDL_PIXELORDER(format) == lib.SDL_PACKEDORDER_ABGR) or
      (SDL_PIXELORDER(format) == lib.SDL_PACKEDORDER_BGRA)))

# The flag is set to 1 because 0x1? is not in the printable ASCII range
def SDL_ISPIXELFORMAT_FOURCC(format):
    return ((format) and (SDL_PIXELFLAG(format) != 1))
