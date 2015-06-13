# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl_image import ffi, lib
from _sdl_image.structs import unbox
from _sdl.structs import SDLError, u8

from sdl import Surface as SDL_Surface, Texture as SDL_Texture, version as SDL_version
from sdl import getError, setError

def init(flags):
    """
    ``int IMG_Init(int)``
    """
    flags_c = flags
    rc = lib.IMG_Init(flags_c)
    return rc

def linked_Version():
    """
    ``SDL_version const * IMG_Linked_Version(void)``
    """
    rc = lib.IMG_Linked_Version()
    return SDL_version(rc)

def load(file):
    """
    ``SDL_Surface * IMG_Load(char const *)``
    """
    file_c = u8(file)
    rc = lib.IMG_Load(file_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadBMP_RW(src):
    """
    ``SDL_Surface * IMG_LoadBMP_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadBMP_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadCUR_RW(src):
    """
    ``SDL_Surface * IMG_LoadCUR_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadCUR_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadGIF_RW(src):
    """
    ``SDL_Surface * IMG_LoadGIF_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadGIF_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadICO_RW(src):
    """
    ``SDL_Surface * IMG_LoadICO_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadICO_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadJPG_RW(src):
    """
    ``SDL_Surface * IMG_LoadJPG_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadJPG_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadLBM_RW(src):
    """
    ``SDL_Surface * IMG_LoadLBM_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadLBM_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadPCX_RW(src):
    """
    ``SDL_Surface * IMG_LoadPCX_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadPCX_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadPNG_RW(src):
    """
    ``SDL_Surface * IMG_LoadPNG_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadPNG_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadPNM_RW(src):
    """
    ``SDL_Surface * IMG_LoadPNM_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadPNM_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadTGA_RW(src):
    """
    ``SDL_Surface * IMG_LoadTGA_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadTGA_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadTIF_RW(src):
    """
    ``SDL_Surface * IMG_LoadTIF_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadTIF_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadTexture(renderer, file):
    """
    ``SDL_Texture * IMG_LoadTexture(SDL_Renderer *, char const *)``
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    file_c = u8(file)
    rc = lib.IMG_LoadTexture(renderer_c, file_c)
    return SDL_Texture(rc)

def loadTextureTyped_RW(renderer, src, freesrc, type):
    """
    ``SDL_Texture * IMG_LoadTextureTyped_RW(SDL_Renderer *, SDL_RWops *, int, char const *)``
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    type_c = u8(type)
    rc = lib.IMG_LoadTextureTyped_RW(renderer_c, src_c, freesrc_c, type_c)
    return SDL_Texture(rc)

def loadTexture_RW(renderer, src, freesrc):
    """
    ``SDL_Texture * IMG_LoadTexture_RW(SDL_Renderer *, SDL_RWops *, int)``
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    rc = lib.IMG_LoadTexture_RW(renderer_c, src_c, freesrc_c)
    return SDL_Texture(rc)

def loadTyped_RW(src, freesrc, type):
    """
    ``SDL_Surface * IMG_LoadTyped_RW(SDL_RWops *, int, char const *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    type_c = u8(type)
    rc = lib.IMG_LoadTyped_RW(src_c, freesrc_c, type_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadWEBP_RW(src):
    """
    ``SDL_Surface * IMG_LoadWEBP_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadWEBP_RW(src_c)
    return SDL_Surface(rc)

def loadXCF_RW(src):
    """
    ``SDL_Surface * IMG_LoadXCF_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadXCF_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadXPM_RW(src):
    """
    ``SDL_Surface * IMG_LoadXPM_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadXPM_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def loadXV_RW(src):
    """
    ``SDL_Surface * IMG_LoadXV_RW(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_LoadXV_RW(src_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def load_RW(src, freesrc):
    """
    ``SDL_Surface * IMG_Load_RW(SDL_RWops *, int)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    rc = lib.IMG_Load_RW(src_c, freesrc_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def quit():
    """
    ``void IMG_Quit(void)``
    """
    lib.IMG_Quit()

def readXPMFromArray(xpm):
    """
    ``SDL_Surface * IMG_ReadXPMFromArray(char * *)``
    """
    xpm_c = unbox(xpm, 'char * *')
    rc = lib.IMG_ReadXPMFromArray(xpm_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def savePNG(surface, file):
    """
    ``int IMG_SavePNG(SDL_Surface *, char const *)``
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    file_c = u8(file)
    rc = lib.IMG_SavePNG(surface_c, file_c)
    return rc

def savePNG_RW(surface, dst, freedst):
    """
    ``int IMG_SavePNG_RW(SDL_Surface *, SDL_RWops *, int)``
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    dst_c = unbox(dst, 'SDL_RWops *')
    freedst_c = freedst
    rc = lib.IMG_SavePNG_RW(surface_c, dst_c, freedst_c)
    return rc

def isBMP(src):
    """
    ``int IMG_isBMP(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isBMP(src_c)
    return rc

def isCUR(src):
    """
    ``int IMG_isCUR(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isCUR(src_c)
    return rc

def isGIF(src):
    """
    ``int IMG_isGIF(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isGIF(src_c)
    return rc

def isICO(src):
    """
    ``int IMG_isICO(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isICO(src_c)
    return rc

def isJPG(src):
    """
    ``int IMG_isJPG(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isJPG(src_c)
    return rc

def isLBM(src):
    """
    ``int IMG_isLBM(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isLBM(src_c)
    return rc

def isPCX(src):
    """
    ``int IMG_isPCX(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isPCX(src_c)
    return rc

def isPNG(src):
    """
    ``int IMG_isPNG(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isPNG(src_c)
    return rc

def isPNM(src):
    """
    ``int IMG_isPNM(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isPNM(src_c)
    return rc

def isTIF(src):
    """
    ``int IMG_isTIF(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isTIF(src_c)
    return rc

def isWEBP(src):
    """
    ``int IMG_isWEBP(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isWEBP(src_c)
    return rc

def isXCF(src):
    """
    ``int IMG_isXCF(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isXCF(src_c)
    return rc

def isXPM(src):
    """
    ``int IMG_isXPM(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isXPM(src_c)
    return rc

def isXV(src):
    """
    ``int IMG_isXV(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.IMG_isXV(src_c)
    return rc

INIT_JPG = lib.IMG_INIT_JPG
INIT_PNG = lib.IMG_INIT_PNG
INIT_TIF = lib.IMG_INIT_TIF
INIT_WEBP = lib.IMG_INIT_WEBP

