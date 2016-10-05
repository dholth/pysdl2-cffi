"""
Locate SDL2 to compile extensions; provide necessary build arguments.
"""

import sys
import os.path
import glob
import platform

system = platform.system()

if system == "Windows":
    # Added to the include path below
    _headers = {
        'sdl_h':'SDL.h',
        'sdl_image_h':'SDL_image.h', 
        'sdl_mixer_h':'SDL_mixer.h',         
        'sdl_ttf_h':'SDL_ttf.h',
        'sdl_gfx_h':'SDL2_gfxPrimitives.h',
    } 

elif system == "Darwin":
    # Header paths for framework build
    _headers = {
        'sdl_h':'SDL2/SDL.h',
        'sdl_image_h':'SDL2_image/SDL_image.h', 
        'sdl_mixer_h':'SDL2_mixer/SDL_mixer.h',         
        'sdl_ttf_h':'SDL2_ttf/SDL_ttf.h',
        'sdl_gfx_h':'SDL2_gfx/SDL2_gfxPrimitives.h',
    }

else:
    # Linux with /usr/include/.../SDL2/
    _headers = {
        'sdl_h':'SDL2/SDL.h',
        'sdl_image_h':'SDL2/SDL_image.h', 
        'sdl_mixer_h':'SDL2/SDL_mixer.h',         
        'sdl_ttf_h':'SDL2/SDL_ttf.h',
        'sdl_gfx_h':'SDL2/SDL2_gfxPrimitives.h',
    }

def make_absolute(paths):
    return [os.path.abspath(p) for p in paths]

def _extension_args(libname):
    here = os.path.dirname(__file__)

    args = {}

    if system == 'Darwin':
        # Link with framework SDL2 on Darwin
        compiler_args = {
            "sdl" : {
                "extra_link_args" : [
                    "-framework", "SDL2"
                    ]
            },
            "image" : {
                "extra_link_args" : [
                    "-framework", "SDL2",
                    "-framework", "SDL2_image"
                    ]
            },
            "mixer" : {
                "extra_link_args" : [
                    "-framework", "SDL2",
                    "-framework", "SDL2_mixer"
                    ]
            },
            "ttf" : {
                "extra_link_args" : [
                    "-framework", "SDL2",
                    "-framework", "SDL2_ttf"
                    ]
            },
        }[libname]
        
    else:
        # Link with plain old -l... on Windows, Linux
        compiler_args = {
            "sdl"   : {"libraries":["SDL2"]},
            "image" : {"libraries":["SDL2", "SDL2_image"], },
            "mixer" : {"libraries":["SDL2", "SDL2_mixer"], },
            "ttf"   : {"libraries":["SDL2", "SDL2_ttf"], },
            "gfx"   : {"libraries":["SDL2", "SDL2_gfx"], },
        }[libname]

    args.update(compiler_args)

    # Use bundled SDL2 to build on Windows
    if system == "Windows":
        arch_dir = "x64" if sys.maxsize.bit_length() > 32 else "x86"
        include_dirs = make_absolute(glob.glob(os.path.join(here, "win", "SDL2*", "include")))
        library_dirs = make_absolute(glob.glob(os.path.join(here, "win", "SDL2*", "lib", arch_dir)))

        args.update(dict(include_dirs=include_dirs, library_dirs=library_dirs))

    return args
