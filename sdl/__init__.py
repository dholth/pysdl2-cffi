# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl import ffi, lib
from _sdl.structs import Struct, unbox, SDLError, u8
from _sdl.helpers import *

import _sdl.pixels
import _sdl.constants

for _lib in _sdl.pixels, _sdl.constants:
    globals().update(dict((key[4:], getattr(_lib, key)) 
        for key in dir(_lib) if key.startswith('SDL_')))

def addEventWatch(filter, userdata):
    """
    ``void SDL_AddEventWatch(int SDL_AddEventWatch(void *, SDL_Event *), void *)``
    
    Add a function which is called when an event is added to the queue.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_AddEventWatch(filter_c, userdata_c)

def addHintCallback(name, callback, userdata):
    """
    ``void SDL_AddHintCallback(char const *, void SDL_AddHintCallback(void *, char const *, char const *, char const *), void *)``
    """
    name_c = u8(name)
    callback_c = unbox(callback, 'void(*)(void *, char const *, char const *, char const *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_AddHintCallback(name_c, callback_c, userdata_c)

def addTimer(interval, callback, param):
    """
    ``int SDL_AddTimer(unsigned int, unsigned int SDL_AddTimer(unsigned int, void *), void *)``
    
    Add a new timer to the pool of timers already running.
    
    :return: A timer ID, or NULL when an error occurs.
    """
    interval_c = interval
    callback_c = unbox(callback, 'unsigned int(*)(unsigned int, void *)')
    param_c = unbox(param, 'void *')
    rc = lib.SDL_AddTimer(interval_c, callback_c, param_c)
    if rc == ffi.NULL: raise SDLError()
    return rc

def allocFormat(pixel_format):
    """
    ``SDL_PixelFormat * SDL_AllocFormat(unsigned int)``
    
    Create an SDL_PixelFormat structure from a pixel format enum.
    """
    pixel_format_c = pixel_format
    rc = lib.SDL_AllocFormat(pixel_format_c)
    return PixelFormat(rc)

def allocPalette(ncolors):
    """
    ``SDL_Palette * SDL_AllocPalette(int)``
    
    Create a palette structure with the specified number of color entries.
    
    :return: A new palette, or NULL if there wasn't enough memory.
    
    The palette entries are initialized to white.
    
    See also SDL_FreePalette()
    """
    ncolors_c = ncolors
    rc = lib.SDL_AllocPalette(ncolors_c)
    return Palette(rc)

def allocRW():
    """
    ``SDL_RWops * SDL_AllocRW(void)``
    """
    rc = lib.SDL_AllocRW()
    return RWops(rc)

def atomicAdd(a, v):
    """
    ``int SDL_AtomicAdd(SDL_atomic_t *, int)``
    
    Add to an atomic variable.
    
    :return: The previous value of the atomic variable.
    
    This same style can be used for any number operation
    """
    a_c = unbox(a, 'SDL_atomic_t *')
    v_c = v
    rc = lib.SDL_AtomicAdd(a_c, v_c)
    return rc

def atomicCAS(a, oldval, newval):
    """
    ``SDL_bool SDL_AtomicCAS(SDL_atomic_t *, int, int)``
    
    Set an atomic variable to a new value if it is currently an old value.
    
    :return: SDL_TRUE if the atomic variable was set, SDL_FALSE otherwise.
    
    If you don't know what this function is for, you shouldn't use it!
    """
    a_c = unbox(a, 'SDL_atomic_t *')
    oldval_c = oldval
    newval_c = newval
    rc = lib.SDL_AtomicCAS(a_c, oldval_c, newval_c)
    return rc

def atomicCASPtr(a, oldval, newval):
    """
    ``SDL_bool SDL_AtomicCASPtr(void * *, void *, void *)``
    
    Set a pointer to a new value if it is currently an old value.
    
    :return: SDL_TRUE if the pointer was set, SDL_FALSE otherwise.
    
    If you don't know what this function is for, you shouldn't use it!
    """
    a_c = unbox(a, 'void * *')
    oldval_c = unbox(oldval, 'void *')
    newval_c = unbox(newval, 'void *')
    rc = lib.SDL_AtomicCASPtr(a_c, oldval_c, newval_c)
    return rc

def atomicGet(a):
    """
    ``int SDL_AtomicGet(SDL_atomic_t *)``
    
    Get the value of an atomic variable.
    """
    a_c = unbox(a, 'SDL_atomic_t *')
    rc = lib.SDL_AtomicGet(a_c)
    return rc

def atomicGetPtr(a):
    """
    ``void * SDL_AtomicGetPtr(void * *)``
    
    Get the value of a pointer atomically.
    """
    a_c = unbox(a, 'void * *')
    rc = lib.SDL_AtomicGetPtr(a_c)
    return rc

def atomicLock(lock=None):
    """
    ``void SDL_AtomicLock(int *)``
    
    Lock a spin lock by setting it to a non-zero value.
    
    :param lock: Points to the lock.
    """
    lock_c = unbox(lock, 'int *')
    lib.SDL_AtomicLock(lock_c)
    return lock_c[0]

def atomicSet(a, v):
    """
    ``int SDL_AtomicSet(SDL_atomic_t *, int)``
    
    Set an atomic variable to a value.
    
    :return: The previous value of the atomic variable.
    """
    a_c = unbox(a, 'SDL_atomic_t *')
    v_c = v
    rc = lib.SDL_AtomicSet(a_c, v_c)
    return rc

def atomicSetPtr(a, v):
    """
    ``void * SDL_AtomicSetPtr(void * *, void *)``
    
    Set a pointer to a value atomically.
    
    :return: The previous value of the pointer.
    """
    a_c = unbox(a, 'void * *')
    v_c = unbox(v, 'void *')
    rc = lib.SDL_AtomicSetPtr(a_c, v_c)
    return rc

def atomicTryLock(lock=None):
    """
    ``SDL_bool SDL_AtomicTryLock(int *)``
    
    Try to lock a spin lock by setting it to a non-zero value.
    
    :param lock: Points to the lock.
    :return: SDL_TRUE if the lock succeeded, SDL_FALSE if the lock is
        already held.
    """
    lock_c = unbox(lock, 'int *')
    rc = lib.SDL_AtomicTryLock(lock_c)
    return (rc, lock_c[0])

def atomicUnlock(lock=None):
    """
    ``void SDL_AtomicUnlock(int *)``
    
    Unlock a spin lock by setting it to 0. Always returns immediately.
    
    :param lock: Points to the lock.
    """
    lock_c = unbox(lock, 'int *')
    lib.SDL_AtomicUnlock(lock_c)
    return lock_c[0]

def audioInit(driver_name):
    """
    ``int SDL_AudioInit(char const *)``
    """
    driver_name_c = u8(driver_name)
    rc = lib.SDL_AudioInit(driver_name_c)
    return rc

def audioQuit():
    """
    ``void SDL_AudioQuit(void)``
    """
    lib.SDL_AudioQuit()

def buildAudioCVT(cvt, src_format, src_channels, src_rate, dst_format, dst_channels, dst_rate):
    """
    ``int SDL_BuildAudioCVT(SDL_AudioCVT *, unsigned short, unsigned char, int, unsigned short, unsigned char, int)``
    
    This function takes a source format and rate and a destination format
    and rate, and initializes the cvt structure with information needed by
    SDL_ConvertAudio() to convert a buffer of audio data from one format
    to the other.
    
    :return: -1 if the format conversion is not supported, 0 if there's no
        conversion needed, or 1 if the audio filter is set up.
    """
    cvt_c = unbox(cvt, 'SDL_AudioCVT *')
    src_format_c = src_format
    src_channels_c = src_channels
    src_rate_c = src_rate
    dst_format_c = dst_format
    dst_channels_c = dst_channels
    dst_rate_c = dst_rate
    rc = lib.SDL_BuildAudioCVT(cvt_c, src_format_c, src_channels_c, src_rate_c, dst_format_c, dst_channels_c, dst_rate_c)
    return rc

def calculateGammaRamp(gamma, ramp=None):
    """
    ``void SDL_CalculateGammaRamp(float, unsigned short *)``
    
    Calculate a 256 entry gamma ramp for a gamma value.
    """
    gamma_c = gamma
    ramp_c = unbox(ramp, 'unsigned short *')
    lib.SDL_CalculateGammaRamp(gamma_c, ramp_c)
    return ramp_c[0]

def clearError():
    """
    ``void SDL_ClearError(void)``
    """
    lib.SDL_ClearError()

def clearHints():
    """
    ``void SDL_ClearHints(void)``
    
    Clear all hints.
    
    This function is called during SDL_Quit() to free stored hints.
    """
    lib.SDL_ClearHints()

def closeAudio():
    """
    ``void SDL_CloseAudio(void)``
    
    This function shuts down audio processing and closes the audio device.
    """
    lib.SDL_CloseAudio()

def closeAudioDevice(dev):
    """
    ``void SDL_CloseAudioDevice(unsigned int)``
    """
    dev_c = dev
    lib.SDL_CloseAudioDevice(dev_c)

def condBroadcast(cond):
    """
    ``int SDL_CondBroadcast(SDL_cond *)``
    
    Restart all threads that are waiting on the condition variable.
    
    :return: 0 or -1 on error.
    """
    cond_c = unbox(cond, 'SDL_cond *')
    rc = lib.SDL_CondBroadcast(cond_c)
    if rc == -1: raise SDLError()
    return rc

def condSignal(cond):
    """
    ``int SDL_CondSignal(SDL_cond *)``
    
    Restart one of the threads that are waiting on the condition variable.
    
    :return: 0 or -1 on error.
    """
    cond_c = unbox(cond, 'SDL_cond *')
    rc = lib.SDL_CondSignal(cond_c)
    if rc == -1: raise SDLError()
    return rc

def condWait(cond, mutex):
    """
    ``int SDL_CondWait(SDL_cond *, SDL_mutex *)``
    
    Wait on the condition variable, unlocking the provided mutex.
    
    The mutex must be locked before entering this function!
    
    The mutex is re-locked once the condition variable is signaled.
    
    :return: 0 when it is signaled, or -1 on error.
    """
    cond_c = unbox(cond, 'SDL_cond *')
    mutex_c = unbox(mutex, 'SDL_mutex *')
    rc = lib.SDL_CondWait(cond_c, mutex_c)
    if rc == -1: raise SDLError()
    return rc

def condWaitTimeout(cond, mutex, ms):
    """
    ``int SDL_CondWaitTimeout(SDL_cond *, SDL_mutex *, unsigned int)``
    
    Waits for at most ms milliseconds, and returns 0 if the condition
    variable is signaled, SDL_MUTEX_TIMEDOUT if the condition is not
    signaled in the allotted time, and -1 on error.
    
    On some platforms this function is implemented by looping with a delay
    of 1 ms, and so should be avoided if possible.
    """
    cond_c = unbox(cond, 'SDL_cond *')
    mutex_c = unbox(mutex, 'SDL_mutex *')
    ms_c = ms
    rc = lib.SDL_CondWaitTimeout(cond_c, mutex_c, ms_c)
    if rc == -1: raise SDLError()
    return rc

def convertAudio(cvt):
    """
    ``int SDL_ConvertAudio(SDL_AudioCVT *)``
    
    Once you have initialized the cvt structure using SDL_BuildAudioCVT(),
    created an audio buffer cvt->buf, and filled it with cvt->len bytes of
    audio data in the source format, this function will convert it in-
    place to the desired format.
    
    The data conversion may expand the size of the audio data, so the
    buffer cvt->buf should be allocated after the cvt structure is
    initialized by SDL_BuildAudioCVT(), and should be
    cvt->len*cvt->len_mult bytes long.
    """
    cvt_c = unbox(cvt, 'SDL_AudioCVT *')
    rc = lib.SDL_ConvertAudio(cvt_c)
    return rc

def convertPixels(width, height, src_format, src, src_pitch, dst_format, dst, dst_pitch):
    """
    ``int SDL_ConvertPixels(int, int, unsigned int, void const *, int, unsigned int, void *, int)``
    
    Copy a block of pixels of one format to another format.
    
    :return: 0 on success, or -1 if there was an error
    """
    width_c = width
    height_c = height
    src_format_c = src_format
    src_c = unbox(src, 'void const *')
    src_pitch_c = src_pitch
    dst_format_c = dst_format
    dst_c = unbox(dst, 'void *')
    dst_pitch_c = dst_pitch
    rc = lib.SDL_ConvertPixels(width_c, height_c, src_format_c, src_c, src_pitch_c, dst_format_c, dst_c, dst_pitch_c)
    return rc

def convertSurface(src, fmt, flags):
    """
    ``SDL_Surface * SDL_ConvertSurface(SDL_Surface *, SDL_PixelFormat const *, unsigned int)``
    
    Creates a new surface of the specified format, and then copies and
    maps the given surface to it so the blit of the converted surface will
    be as fast as possible. If this function fails, it returns NULL.
    
    The flags parameter is passed to SDL_CreateRGBSurface() and has those
    semantics. You can also pass SDL_RLEACCEL in the flags parameter and
    SDL will try to RLE accelerate colorkey and alpha blits in the
    resulting surface.
    """
    src_c = unbox(src, 'SDL_Surface *')
    fmt_c = unbox(fmt, 'SDL_PixelFormat const *')
    flags_c = flags
    rc = lib.SDL_ConvertSurface(src_c, fmt_c, flags_c)
    return Surface(rc)

def convertSurfaceFormat(src, pixel_format, flags):
    """
    ``SDL_Surface * SDL_ConvertSurfaceFormat(SDL_Surface *, unsigned int, unsigned int)``
    """
    src_c = unbox(src, 'SDL_Surface *')
    pixel_format_c = pixel_format
    flags_c = flags
    rc = lib.SDL_ConvertSurfaceFormat(src_c, pixel_format_c, flags_c)
    return Surface(rc)

def createColorCursor(surface, hot_x, hot_y):
    """
    ``SDL_Cursor * SDL_CreateColorCursor(SDL_Surface *, int, int)``
    
    Create a color cursor.
    
    See also SDL_FreeCursor()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    hot_x_c = hot_x
    hot_y_c = hot_y
    rc = lib.SDL_CreateColorCursor(surface_c, hot_x_c, hot_y_c)
    return Cursor(rc)

def createCond():
    """
    ``SDL_cond * SDL_CreateCond(void)``
    
    Create a condition variable.
    
    Typical use of condition variables:
    
    Thread A: SDL_LockMutex(lock); while ( ! condition ) {
    SDL_CondWait(cond, lock); } SDL_UnlockMutex(lock);
    
    Thread B: SDL_LockMutex(lock); ... condition = true; ...
    SDL_CondSignal(cond); SDL_UnlockMutex(lock);
    
    There is some discussion whether to signal the condition variable with
    the mutex locked or not. There is some potential performance benefit
    to unlocking first on some platforms, but there are some potential
    race conditions depending on how your code is structured.
    
    In general it's safer to signal the condition variable while the mutex
    is locked.
    """
    rc = lib.SDL_CreateCond()
    return cond(rc)

def createCursor(data, mask, w, h, hot_x, hot_y):
    """
    ``SDL_Cursor * SDL_CreateCursor(unsigned char const *, unsigned char const *, int, int, int, int)``
    
    Create a cursor, using the specified bitmap data and mask (in MSB
    format).
    
    The cursor width must be a multiple of 8 bits.
    
    The cursor is created in black and white according to the following:
    data
    
    mask
    
    resulting pixel on screen
    
    0
    
    1
    
    White
    
    1
    
    1
    
    Black
    
    0
    
    0
    
    Transparent
    
    1
    
    0
    
    Inverted color if possible, black if not.
    
    See also SDL_FreeCursor()
    """
    data_c = unbox(data, 'unsigned char const *')
    mask_c = unbox(mask, 'unsigned char const *')
    w_c = w
    h_c = h
    hot_x_c = hot_x
    hot_y_c = hot_y
    rc = lib.SDL_CreateCursor(data_c, mask_c, w_c, h_c, hot_x_c, hot_y_c)
    return Cursor(rc)

def createMutex():
    """
    ``SDL_mutex * SDL_CreateMutex(void)``
    
    Create a mutex, initialized unlocked.
    """
    rc = lib.SDL_CreateMutex()
    return mutex(rc)

def createRGBSurface(flags, width, height, depth, Rmask, Gmask, Bmask, Amask):
    """
    ``SDL_Surface * SDL_CreateRGBSurface(unsigned int, int, int, int, unsigned int, unsigned int, unsigned int, unsigned int)``
    
    Allocate and free an RGB surface.
    
    If the depth is 4 or 8 bits, an empty palette is allocated for the
    surface. If the depth is greater than 8 bits, the pixel format is set
    using the flags '[RGB]mask'.
    
    If the function runs out of memory, it will return NULL.
    
    :param flags: The flags are obsolete and should be set to 0.
    :param width: The width in pixels of the surface to create.
    :param height: The height in pixels of the surface to create.
    :param depth: The depth in bits of the surface to create.
    :param Rmask: The red mask of the surface to create.
    :param Gmask: The green mask of the surface to create.
    :param Bmask: The blue mask of the surface to create.
    :param Amask: The alpha mask of the surface to create.
    """
    flags_c = flags
    width_c = width
    height_c = height
    depth_c = depth
    Rmask_c = Rmask
    Gmask_c = Gmask
    Bmask_c = Bmask
    Amask_c = Amask
    rc = lib.SDL_CreateRGBSurface(flags_c, width_c, height_c, depth_c, Rmask_c, Gmask_c, Bmask_c, Amask_c)
    return Surface(rc)

def createRGBSurfaceFrom(pixels, width, height, depth, pitch, Rmask, Gmask, Bmask, Amask):
    """
    ``SDL_Surface * SDL_CreateRGBSurfaceFrom(void *, int, int, int, int, unsigned int, unsigned int, unsigned int, unsigned int)``
    """
    pixels_c = unbox(pixels, 'void *')
    width_c = width
    height_c = height
    depth_c = depth
    pitch_c = pitch
    Rmask_c = Rmask
    Gmask_c = Gmask
    Bmask_c = Bmask
    Amask_c = Amask
    rc = lib.SDL_CreateRGBSurfaceFrom(pixels_c, width_c, height_c, depth_c, pitch_c, Rmask_c, Gmask_c, Bmask_c, Amask_c)
    return Surface(rc)

def createRenderer(window, index, flags):
    """
    ``SDL_Renderer * SDL_CreateRenderer(SDL_Window *, int, unsigned int)``
    
    Create a 2D rendering context for a window.
    
    :param window: The window where rendering is displayed.
    :param index: The index of the rendering driver to initialize, or -1
        to initialize the first one supporting the requested flags.
    :param flags: SDL_RendererFlags.
    :return: A valid rendering context or NULL if there was an error.
    
    See also SDL_CreateSoftwareRenderer()
    """
    window_c = unbox(window, 'SDL_Window *')
    index_c = index
    flags_c = flags
    rc = lib.SDL_CreateRenderer(window_c, index_c, flags_c)
    if rc == ffi.NULL: raise SDLError()
    return Renderer(rc)

def createSemaphore(initial_value):
    """
    ``SDL_sem * SDL_CreateSemaphore(unsigned int)``
    
    Create a semaphore, initialized with value, returns NULL on failure.
    """
    initial_value_c = initial_value
    rc = lib.SDL_CreateSemaphore(initial_value_c)
    return sem(rc)

def createSoftwareRenderer(surface):
    """
    ``SDL_Renderer * SDL_CreateSoftwareRenderer(SDL_Surface *)``
    
    Create a 2D software rendering context for a surface.
    
    :param surface: The surface where rendering is done.
    :return: A valid rendering context or NULL if there was an error.
    
    See also SDL_CreateRenderer()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    rc = lib.SDL_CreateSoftwareRenderer(surface_c)
    if rc == ffi.NULL: raise SDLError()
    return Renderer(rc)

def createSystemCursor(id):
    """
    ``SDL_Cursor * SDL_CreateSystemCursor(SDL_SystemCursor)``
    
    Create a system cursor.
    
    See also SDL_FreeCursor()
    """
    id_c = id
    rc = lib.SDL_CreateSystemCursor(id_c)
    return Cursor(rc)

def createTexture(renderer, format, access, w, h):
    """
    ``SDL_Texture * SDL_CreateTexture(SDL_Renderer *, unsigned int, int, int, int)``
    
    Create a texture for a rendering context.
    
    :param renderer: The renderer.
    :param format: The format of the texture.
    :param access: One of the enumerated values in SDL_TextureAccess.
    :param w: The width of the texture in pixels.
    :param h: The height of the texture in pixels.
    :return: The created texture is returned, or 0 if no rendering context
        was active, the format was unsupported, or the width or height
        were out of range.
    
    See also SDL_QueryTexture()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    format_c = format
    access_c = access
    w_c = w
    h_c = h
    rc = lib.SDL_CreateTexture(renderer_c, format_c, access_c, w_c, h_c)
    return Texture(rc)

def createTextureFromSurface(renderer, surface):
    """
    ``SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer *, SDL_Surface *)``
    
    Create a texture from an existing surface.
    
    :param renderer: The renderer.
    :param surface: The surface containing pixel data used to fill the
        texture.
    :return: The created texture is returned, or 0 on error.
    
    The surface is not modified or freed by this function.
    
    See also SDL_QueryTexture()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    surface_c = unbox(surface, 'SDL_Surface *')
    rc = lib.SDL_CreateTextureFromSurface(renderer_c, surface_c)
    if rc == ffi.NULL: raise SDLError()
    return Texture(rc)

def createThread(fn, name, data):
    """
    ``SDL_Thread * SDL_CreateThread(int SDL_CreateThread(void *), char const *, void *)``
    
    Create a thread.
    """
    fn_c = unbox(fn, 'int(*)(void *)')
    name_c = u8(name)
    data_c = unbox(data, 'void *')
    rc = lib.SDL_CreateThread(fn_c, name_c, data_c)
    return Thread(rc)

def createWindow(title, x, y, w, h, flags):
    """
    ``SDL_Window * SDL_CreateWindow(char const *, int, int, int, int, unsigned int)``
    
    Create a window with the specified position, dimensions, and flags.
    
    :param title: The title of the window, in UTF-8 encoding.
    :param x: The x position of the window, SDL_WINDOWPOS_CENTERED, or
        SDL_WINDOWPOS_UNDEFINED.
    :param y: The y position of the window, SDL_WINDOWPOS_CENTERED, or
        SDL_WINDOWPOS_UNDEFINED.
    :param w: The width of the window.
    :param h: The height of the window.
    :param flags: The flags for the window, a mask of any of the
        following: SDL_WINDOW_FULLSCREEN, SDL_WINDOW_OPENGL,
        SDL_WINDOW_HIDDEN, SDL_WINDOW_BORDERLESS, SDL_WINDOW_RESIZABLE,
        SDL_WINDOW_MAXIMIZED, SDL_WINDOW_MINIMIZED,
        SDL_WINDOW_INPUT_GRABBED, SDL_WINDOW_ALLOW_HIGHDPI.
    :return: The id of the window created, or zero if window creation
        failed.
    
    See also SDL_DestroyWindow()
    """
    title_c = u8(title)
    x_c = x
    y_c = y
    w_c = w
    h_c = h
    flags_c = flags
    rc = lib.SDL_CreateWindow(title_c, x_c, y_c, w_c, h_c, flags_c)
    return Window(rc)

def createWindowAndRenderer(width, height, window_flags, window, renderer):
    """
    ``int SDL_CreateWindowAndRenderer(int, int, unsigned int, SDL_Window * *, SDL_Renderer * *)``
    
    Create a window and default renderer.
    
    :param width: The width of the window
    :param height: The height of the window
    :param window_flags: The flags used to create the window
    :param window: A pointer filled with the window, or NULL on error
    :param renderer: A pointer filled with the renderer, or NULL on error
    :return: 0 on success, or -1 on error
    """
    width_c = width
    height_c = height
    window_flags_c = window_flags
    window_c = unbox(window, 'SDL_Window * *')
    renderer_c = unbox(renderer, 'SDL_Renderer * *')
    rc = lib.SDL_CreateWindowAndRenderer(width_c, height_c, window_flags_c, window_c, renderer_c)
    if rc == -1: raise SDLError()
    return rc

def createWindowFrom(data):
    """
    ``SDL_Window * SDL_CreateWindowFrom(void const *)``
    
    Create an SDL window from an existing native window.
    
    :param data: A pointer to driver-dependent window creation data
    :return: The id of the window created, or zero if window creation
        failed.
    
    See also SDL_DestroyWindow()
    """
    data_c = unbox(data, 'void const *')
    rc = lib.SDL_CreateWindowFrom(data_c)
    return Window(rc)

def delEventWatch(filter, userdata):
    """
    ``void SDL_DelEventWatch(int SDL_DelEventWatch(void *, SDL_Event *), void *)``
    
    Remove an event watch function added with SDL_AddEventWatch()
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_DelEventWatch(filter_c, userdata_c)

def delHintCallback(name, callback, userdata):
    """
    ``void SDL_DelHintCallback(char const *, void SDL_DelHintCallback(void *, char const *, char const *, char const *), void *)``
    
    Remove a function watching a particular hint.
    
    :param name: The hint being watched
    :param callback: The function being called when the hint value changes
    :param userdata: A pointer being passed to the callback function
    """
    name_c = u8(name)
    callback_c = unbox(callback, 'void(*)(void *, char const *, char const *, char const *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_DelHintCallback(name_c, callback_c, userdata_c)

def delay(ms):
    """
    ``void SDL_Delay(unsigned int)``
    
    Wait a specified number of milliseconds before returning.
    """
    ms_c = ms
    lib.SDL_Delay(ms_c)

def destroyCond(cond):
    """
    ``void SDL_DestroyCond(SDL_cond *)``
    
    Destroy a condition variable.
    """
    cond_c = unbox(cond, 'SDL_cond *')
    lib.SDL_DestroyCond(cond_c)

def destroyMutex(mutex):
    """
    ``void SDL_DestroyMutex(SDL_mutex *)``
    
    Destroy a mutex.
    """
    mutex_c = unbox(mutex, 'SDL_mutex *')
    lib.SDL_DestroyMutex(mutex_c)

def destroyRenderer(renderer):
    """
    ``void SDL_DestroyRenderer(SDL_Renderer *)``
    
    Destroy the rendering context for a window and free associated
    textures.
    
    See also SDL_CreateRenderer()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    lib.SDL_DestroyRenderer(renderer_c)

def destroySemaphore(sem):
    """
    ``void SDL_DestroySemaphore(SDL_sem *)``
    
    Destroy a semaphore.
    """
    sem_c = unbox(sem, 'SDL_sem *')
    lib.SDL_DestroySemaphore(sem_c)

def destroyTexture(texture):
    """
    ``void SDL_DestroyTexture(SDL_Texture *)``
    
    Destroy the specified texture.
    
    See also SDL_CreateTexture()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    lib.SDL_DestroyTexture(texture_c)

def destroyWindow(window):
    """
    ``void SDL_DestroyWindow(SDL_Window *)``
    
    Destroy a window.
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_DestroyWindow(window_c)

def detachThread(thread):
    """
    ``void SDL_DetachThread(SDL_Thread *)``
    
    A thread may be "detached" to signify that it should not remain until
    another thread has called SDL_WaitThread() on it. Detaching a thread
    is useful for long-running threads that nothing needs to synchronize
    with or further manage. When a detached thread is done, it simply goes
    away.
    
    There is no way to recover the return code of a detached thread. If
    you need this, don't detach the thread and instead use
    SDL_WaitThread().
    
    Once a thread is detached, you should usually assume the SDL_Thread
    isn't safe to reference again, as it will become invalid immediately
    upon the detached thread's exit, instead of remaining until someone
    has called SDL_WaitThread() to finally clean it up. As such, don't
    detach the same thread more than once.
    
    If a thread has already exited when passed to SDL_DetachThread(), it
    will stop waiting for a call to SDL_WaitThread() and clean up
    immediately. It is not safe to detach a thread that might be used with
    SDL_WaitThread().
    
    You may not call SDL_WaitThread() on a thread that has been detached.
    Use either that function or this one, but not both, or behavior is
    undefined.
    
    It is safe to pass NULL to this function; it is a no-op.
    """
    thread_c = unbox(thread, 'SDL_Thread *')
    lib.SDL_DetachThread(thread_c)

def disableScreenSaver():
    """
    ``void SDL_DisableScreenSaver(void)``
    
    Prevent the screen from being blanked by a screensaver.
    
    See also SDL_IsScreenSaverEnabled()
    """
    lib.SDL_DisableScreenSaver()

def enableScreenSaver():
    """
    ``void SDL_EnableScreenSaver(void)``
    
    Allow the screen to be blanked by a screensaver.
    
    See also SDL_IsScreenSaverEnabled()
    """
    lib.SDL_EnableScreenSaver()

def enclosePoints(points, count, clip, result):
    """
    ``SDL_bool SDL_EnclosePoints(SDL_Point const *, int, SDL_Rect const *, SDL_Rect *)``
    
    Calculate a minimal rectangle enclosing a set of points.
    
    :return: SDL_TRUE if any points were within the clipping rect
    """
    points_c = unbox(points, 'SDL_Point const *')
    count_c = count
    clip_c = unbox(clip, 'SDL_Rect const *')
    result_c = unbox(result, 'SDL_Rect *')
    rc = lib.SDL_EnclosePoints(points_c, count_c, clip_c, result_c)
    return rc

def error(code):
    """
    ``int SDL_Error(SDL_errorcode)``
    """
    code_c = code
    rc = lib.SDL_Error(code_c)
    return rc

def eventState(type, state):
    """
    ``unsigned char SDL_EventState(unsigned int, int)``
    
    This function allows you to set the state of processing certain
    events.If state is set to SDL_IGNORE, that event will be automatically
    dropped from the event queue and will not event be filtered.
    
    If state is set to SDL_ENABLE, that event will be processed normally.
    
    If state is set to SDL_QUERY, SDL_EventState() will return the current
    processing state of the specified event.
    """
    type_c = type
    state_c = state
    rc = lib.SDL_EventState(type_c, state_c)
    return rc

def fillRect(dst, rect, color):
    """
    ``int SDL_FillRect(SDL_Surface *, SDL_Rect const *, unsigned int)``
    
    Performs a fast fill of the given rectangle with color.
    
    If rect is NULL, the whole surface will be filled with color.
    
    The color should be a pixel of the format used by the surface, and can
    be generated by the SDL_MapRGB() function.
    
    :return: 0 on success, or -1 on error.
    """
    dst_c = unbox(dst, 'SDL_Surface *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    color_c = color
    rc = lib.SDL_FillRect(dst_c, rect_c, color_c)
    if rc == -1: raise SDLError()
    return rc

def fillRects(dst, rects, count, color):
    """
    ``int SDL_FillRects(SDL_Surface *, SDL_Rect const *, int, unsigned int)``
    """
    dst_c = unbox(dst, 'SDL_Surface *')
    rects_c = unbox(rects, 'SDL_Rect const *')
    count_c = count
    color_c = color
    rc = lib.SDL_FillRects(dst_c, rects_c, count_c, color_c)
    return rc

def filterEvents(filter, userdata):
    """
    ``void SDL_FilterEvents(int SDL_FilterEvents(void *, SDL_Event *), void *)``
    
    Run the filter function on the current event queue, removing any
    events for which the filter returns 0.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_FilterEvents(filter_c, userdata_c)

def flushEvent(type):
    """
    ``void SDL_FlushEvent(unsigned int)``
    
    This function clears events from the event queue
    """
    type_c = type
    lib.SDL_FlushEvent(type_c)

def flushEvents(minType, maxType):
    """
    ``void SDL_FlushEvents(unsigned int, unsigned int)``
    """
    minType_c = minType
    maxType_c = maxType
    lib.SDL_FlushEvents(minType_c, maxType_c)

def freeCursor(cursor):
    """
    ``void SDL_FreeCursor(SDL_Cursor *)``
    
    Frees a cursor created with SDL_CreateCursor().
    
    See also SDL_CreateCursor()
    """
    cursor_c = unbox(cursor, 'SDL_Cursor *')
    lib.SDL_FreeCursor(cursor_c)

def freeFormat(format):
    """
    ``void SDL_FreeFormat(SDL_PixelFormat *)``
    
    Free an SDL_PixelFormat structure.
    """
    format_c = unbox(format, 'SDL_PixelFormat *')
    lib.SDL_FreeFormat(format_c)

def freePalette(palette):
    """
    ``void SDL_FreePalette(SDL_Palette *)``
    
    Free a palette created with SDL_AllocPalette().
    
    See also SDL_AllocPalette()
    """
    palette_c = unbox(palette, 'SDL_Palette *')
    lib.SDL_FreePalette(palette_c)

def freeRW(area):
    """
    ``void SDL_FreeRW(SDL_RWops *)``
    """
    area_c = unbox(area, 'SDL_RWops *')
    lib.SDL_FreeRW(area_c)

def freeSurface(surface):
    """
    ``void SDL_FreeSurface(SDL_Surface *)``
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    lib.SDL_FreeSurface(surface_c)

def freeWAV(audio_buf=None):
    """
    ``void SDL_FreeWAV(unsigned char *)``
    
    This function frees data previously allocated with SDL_LoadWAV_RW()
    """
    audio_buf_c = unbox(audio_buf, 'unsigned char *')
    lib.SDL_FreeWAV(audio_buf_c)
    return audio_buf_c[0]

def GL_BindTexture(texture, texw=None, texh=None):
    """
    ``int SDL_GL_BindTexture(SDL_Texture *, float *, float *)``
    
    Bind the texture to the current OpenGL/ES/ES2 context for use with
    OpenGL instructions.
    
    :param texture: The SDL texture to bind
    :param texw: A pointer to a float that will be filled with the texture
        width
    :param texh: A pointer to a float that will be filled with the texture
        height
    :return: 0 on success, or -1 if the operation is not supported
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    texw_c = unbox(texw, 'float *')
    texh_c = unbox(texh, 'float *')
    rc = lib.SDL_GL_BindTexture(texture_c, texw_c, texh_c)
    return (rc, texw_c[0], texh_c[0])

def GL_CreateContext(window):
    """
    ``void * SDL_GL_CreateContext(SDL_Window *)``
    
    Create an OpenGL context for use with an OpenGL window, and make it
    current.
    
    See also SDL_GL_DeleteContext()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GL_CreateContext(window_c)
    return rc

def GL_DeleteContext(context):
    """
    ``void SDL_GL_DeleteContext(void *)``
    
    Delete an OpenGL context.
    
    See also SDL_GL_CreateContext()
    """
    context_c = unbox(context, 'void *')
    lib.SDL_GL_DeleteContext(context_c)

def GL_ExtensionSupported(extension):
    """
    ``SDL_bool SDL_GL_ExtensionSupported(char const *)``
    
    Return true if an OpenGL extension is supported for the current
    context.
    """
    extension_c = u8(extension)
    rc = lib.SDL_GL_ExtensionSupported(extension_c)
    return rc

def GL_GetAttribute(attr, value=None):
    """
    ``int SDL_GL_GetAttribute(SDL_GLattr, int *)``
    
    Get the actual value for an attribute from the current context.
    """
    attr_c = attr
    value_c = unbox(value, 'int *')
    rc = lib.SDL_GL_GetAttribute(attr_c, value_c)
    return (rc, value_c[0])

def GL_GetCurrentContext():
    """
    ``void * SDL_GL_GetCurrentContext(void)``
    
    Get the currently active OpenGL context.
    """
    rc = lib.SDL_GL_GetCurrentContext()
    return rc

def GL_GetCurrentWindow():
    """
    ``SDL_Window * SDL_GL_GetCurrentWindow(void)``
    
    Get the currently active OpenGL window.
    """
    rc = lib.SDL_GL_GetCurrentWindow()
    return Window(rc)

def GL_GetDrawableSize(window, w=None, h=None):
    """
    ``void SDL_GL_GetDrawableSize(SDL_Window *, int *, int *)``
    
    Get the size of a window's underlying drawable (for use with
    glViewport).
    
    :param window: Window from which the drawable size should be queried
    :param w: Pointer to variable for storing the width, may be NULL
    :param h: Pointer to variable for storing the height, may be NULL
    
    This may differ from SDL_GetWindowSize if we're rendering to a high-
    DPI drawable, i.e. the window was created with
    SDL_WINDOW_ALLOW_HIGHDPI on a platform with high-DPI support (Apple
    calls this "Retina"), and not disabled by the
    SDL_HINT_VIDEO_HIGHDPI_DISABLED hint.
    
    See also SDL_GetWindowSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    lib.SDL_GL_GetDrawableSize(window_c, w_c, h_c)
    return (w_c[0], h_c[0])

def GL_GetProcAddress(proc):
    """
    ``void * SDL_GL_GetProcAddress(char const *)``
    
    Get the address of an OpenGL function.
    """
    proc_c = u8(proc)
    rc = lib.SDL_GL_GetProcAddress(proc_c)
    return rc

def GL_GetSwapInterval():
    """
    ``int SDL_GL_GetSwapInterval(void)``
    
    Get the swap interval for the current OpenGL context.
    
    :return: 0 if there is no vertical retrace synchronization, 1 if the
        buffer swap is synchronized with the vertical retrace, and -1 if
        late swaps happen immediately instead of waiting for the next
        retrace. If the system can't determine the swap interval, or there
        isn't a valid current context, this will return 0 as a safe
        default.
    
    See also SDL_GL_SetSwapInterval()
    """
    rc = lib.SDL_GL_GetSwapInterval()
    return rc

def GL_LoadLibrary(path):
    """
    ``int SDL_GL_LoadLibrary(char const *)``
    
    Dynamically load an OpenGL library.
    
    :param path: The platform dependent OpenGL library name, or NULL to
        open the default OpenGL library.
    :return: 0 on success, or -1 if the library couldn't be loaded.
    
    This should be done after initializing the video driver, but before
    creating any OpenGL windows. If no OpenGL library is loaded, the
    default library will be loaded upon creation of the first OpenGL
    window.
    
    If you do this, you need to retrieve all of the GL functions used in
    your program from the dynamic library using SDL_GL_GetProcAddress().
    
    See also SDL_GL_GetProcAddress()
    """
    path_c = u8(path)
    rc = lib.SDL_GL_LoadLibrary(path_c)
    return rc

def GL_MakeCurrent(window, context):
    """
    ``int SDL_GL_MakeCurrent(SDL_Window *, void *)``
    
    Set up an OpenGL context for rendering into an OpenGL window.
    
    The context must have been created with a compatible window.
    """
    window_c = unbox(window, 'SDL_Window *')
    context_c = unbox(context, 'void *')
    rc = lib.SDL_GL_MakeCurrent(window_c, context_c)
    return rc

def GL_ResetAttributes():
    """
    ``void SDL_GL_ResetAttributes(void)``
    
    Reset all previously set OpenGL context attributes to their default
    values.
    """
    lib.SDL_GL_ResetAttributes()

def GL_SetAttribute(attr, value):
    """
    ``int SDL_GL_SetAttribute(SDL_GLattr, int)``
    
    Set an OpenGL window attribute before window creation.
    """
    attr_c = attr
    value_c = value
    rc = lib.SDL_GL_SetAttribute(attr_c, value_c)
    return rc

def GL_SetSwapInterval(interval):
    """
    ``int SDL_GL_SetSwapInterval(int)``
    
    Set the swap interval for the current OpenGL context.
    
    :param interval: 0 for immediate updates, 1 for updates synchronized
        with the vertical retrace. If the system supports it, you may
        specify -1 to allow late swaps to happen immediately instead of
        waiting for the next retrace.
    :return: 0 on success, or -1 if setting the swap interval is not
        supported.
    
    See also SDL_GL_GetSwapInterval()
    """
    interval_c = interval
    rc = lib.SDL_GL_SetSwapInterval(interval_c)
    return rc

def GL_SwapWindow(window):
    """
    ``void SDL_GL_SwapWindow(SDL_Window *)``
    
    Swap the OpenGL buffers for a window, if double-buffering is
    supported.
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_GL_SwapWindow(window_c)

def GL_UnbindTexture(texture):
    """
    ``int SDL_GL_UnbindTexture(SDL_Texture *)``
    
    Unbind a texture from the current OpenGL/ES/ES2 context.
    
    :param texture: The SDL texture to unbind
    :return: 0 on success, or -1 if the operation is not supported
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    rc = lib.SDL_GL_UnbindTexture(texture_c)
    return rc

def GL_UnloadLibrary():
    """
    ``void SDL_GL_UnloadLibrary(void)``
    
    Unload the OpenGL library previously loaded by SDL_GL_LoadLibrary().
    
    See also SDL_GL_LoadLibrary()
    """
    lib.SDL_GL_UnloadLibrary()

def gameControllerAddMapping(mappingString):
    """
    ``int SDL_GameControllerAddMapping(char const *)``
    
    Add or update an existing mapping configuration
    
    :return: 1 if mapping is added, 0 if updated, -1 on error
    """
    mappingString_c = u8(mappingString)
    rc = lib.SDL_GameControllerAddMapping(mappingString_c)
    if rc == -1: raise SDLError()
    return rc

def gameControllerAddMappingsFromRW(rw, freerw):
    """
    ``int SDL_GameControllerAddMappingsFromRW(SDL_RWops *, int)``
    
    To count the number of game controllers in the system for the
    following: int nJoysticks = SDL_NumJoysticks(); int nGameControllers =
    0; for ( int i = 0; i < nJoysticks; i++ ) { if (
    SDL_IsGameController(i) ) { nGameControllers++; } }
    
    Using the SDL_HINT_GAMECONTROLLERCONFIG hint or the
    SDL_GameControllerAddMapping you can add support for controllers SDL
    is unaware of or cause an existing controller to have a different
    binding. The format is: guid,name,mappings
    
    Where GUID is the string value from SDL_JoystickGetGUIDString(), name
    is the human readable string for the device and mappings are
    controller mappings to joystick ones. Under Windows there is a
    reserved GUID of "xinput" that covers any XInput devices. The mapping
    format for joystick is: bX - a joystick button, index X hX.Y - hat X
    with value Y aX - axis X of the joystick Buttons can be used as a
    controller axis and vice versa.
    
    This string shows an example of a valid mapping for a controller
    "341a3608000000000000504944564944,Afterglow PS3 Controller,a:b1,b:b2,y
    :b3,x:b0,start:b9,guide:b12,back:b8,dpup:h0.1,dpleft:h0.8,dpdown:h0.4,
    dpright:h0.2,leftshoulder:b4,rightshoulder:b5,leftstick:b10,rightstick
    :b11,leftx:a0,lefty:a1,rightx:a2,righty:a3,lefttrigger:b6,righttrigger
    :b7", Load a set of mappings from a seekable SDL data stream (memory
    or file), filtered by the current SDL_GetPlatform() A community
    sourced database of controllers is available at https://raw.github.com
    /gabomdq/SDL_GameControllerDB/master/gamecontrollerdb.txt
    
    If freerw is non-zero, the stream will be closed after being read.
    
    :return: number of mappings added, -1 on error
    """
    rw_c = unbox(rw, 'SDL_RWops *')
    freerw_c = freerw
    rc = lib.SDL_GameControllerAddMappingsFromRW(rw_c, freerw_c)
    if rc == -1: raise SDLError()
    return rc

def gameControllerClose(gamecontroller):
    """
    ``void SDL_GameControllerClose(SDL_GameController *)``
    
    Close a controller previously opened with SDL_GameControllerOpen().
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    lib.SDL_GameControllerClose(gamecontroller_c)

def gameControllerEventState(state):
    """
    ``int SDL_GameControllerEventState(int)``
    
    Enable/disable controller event polling.
    
    If controller events are disabled, you must call
    SDL_GameControllerUpdate() yourself and check the state of the
    controller when you want controller information.
    
    The state can be one of SDL_QUERY, SDL_ENABLE or SDL_IGNORE.
    """
    state_c = state
    rc = lib.SDL_GameControllerEventState(state_c)
    return rc

def gameControllerGetAttached(gamecontroller):
    """
    ``SDL_bool SDL_GameControllerGetAttached(SDL_GameController *)``
    
    Returns SDL_TRUE if the controller has been opened and currently
    connected, or SDL_FALSE if it has not.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetAttached(gamecontroller_c)
    return rc

def gameControllerGetAxis(gamecontroller, axis):
    """
    ``int16_t SDL_GameControllerGetAxis(SDL_GameController *, SDL_GameControllerAxis)``
    
    Get the current state of an axis control on a game controller.
    
    The state is a value ranging from -32768 to 32767.
    
    The axis indices start at index 0.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    axis_c = axis
    rc = lib.SDL_GameControllerGetAxis(gamecontroller_c, axis_c)
    return rc

def gameControllerGetAxisFromString(pchString):
    """
    ``SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(char const *)``
    
    turn this string into a axis mapping
    """
    pchString_c = u8(pchString)
    rc = lib.SDL_GameControllerGetAxisFromString(pchString_c)
    return rc

def gameControllerGetBindForAxis(gamecontroller, axis):
    """
    ``SDL_GameControllerButtonBind SDL_GameControllerGetBindForAxis(SDL_GameController *, SDL_GameControllerAxis)``
    
    Get the SDL joystick layer binding for this controller button mapping
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    axis_c = axis
    rc = lib.SDL_GameControllerGetBindForAxis(gamecontroller_c, axis_c)
    return GameControllerButtonBind(rc)

def gameControllerGetBindForButton(gamecontroller, button):
    """
    ``SDL_GameControllerButtonBind SDL_GameControllerGetBindForButton(SDL_GameController *, SDL_GameControllerButton)``
    
    Get the SDL joystick layer binding for this controller button mapping
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    button_c = button
    rc = lib.SDL_GameControllerGetBindForButton(gamecontroller_c, button_c)
    return GameControllerButtonBind(rc)

def gameControllerGetButton(gamecontroller, button):
    """
    ``unsigned char SDL_GameControllerGetButton(SDL_GameController *, SDL_GameControllerButton)``
    
    Get the current state of a button on a game controller.
    
    The button indices start at index 0.
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    button_c = button
    rc = lib.SDL_GameControllerGetButton(gamecontroller_c, button_c)
    return rc

def gameControllerGetButtonFromString(pchString):
    """
    ``SDL_GameControllerButton SDL_GameControllerGetButtonFromString(char const *)``
    
    turn this string into a button mapping
    """
    pchString_c = u8(pchString)
    rc = lib.SDL_GameControllerGetButtonFromString(pchString_c)
    return rc

def gameControllerGetJoystick(gamecontroller):
    """
    ``SDL_Joystick * SDL_GameControllerGetJoystick(SDL_GameController *)``
    
    Get the underlying joystick object used by a controller
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerGetJoystick(gamecontroller_c)
    return Joystick(rc)

def gameControllerGetStringForAxis(axis):
    """
    ``char const * SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis)``
    
    turn this axis enum into a string mapping
    """
    axis_c = axis
    rc = lib.SDL_GameControllerGetStringForAxis(axis_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerGetStringForButton(button):
    """
    ``char const * SDL_GameControllerGetStringForButton(SDL_GameControllerButton)``
    
    turn this button enum into a string mapping
    """
    button_c = button
    rc = lib.SDL_GameControllerGetStringForButton(button_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerMapping(gamecontroller):
    """
    ``char * SDL_GameControllerMapping(SDL_GameController *)``
    
    Get a mapping string for an open GameController
    
    :return: the mapping string. Must be freed with SDL_free. Returns NULL
        if no mapping is available
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerMapping(gamecontroller_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerMappingForGUID(guid):
    """
    ``char * SDL_GameControllerMappingForGUID(SDL_JoystickGUID)``
    
    Get a mapping string for a GUID
    
    :return: the mapping string. Must be freed with SDL_free. Returns NULL
        if no mapping is available
    """
    guid_c = unbox(guid, 'SDL_JoystickGUID')
    rc = lib.SDL_GameControllerMappingForGUID(guid_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerName(gamecontroller):
    """
    ``char const * SDL_GameControllerName(SDL_GameController *)``
    
    Return the name for this currently opened controller
    """
    gamecontroller_c = unbox(gamecontroller, 'SDL_GameController *')
    rc = lib.SDL_GameControllerName(gamecontroller_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerNameForIndex(joystick_index):
    """
    ``char const * SDL_GameControllerNameForIndex(int)``
    
    Get the implementation dependent name of a game controller. This can
    be called before any controllers are opened. If no name can be found,
    this function returns NULL.
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_GameControllerNameForIndex(joystick_index_c)
    return ffi.string(rc).decode('utf-8')

def gameControllerOpen(joystick_index):
    """
    ``SDL_GameController * SDL_GameControllerOpen(int)``
    
    Open a game controller for use. The index passed as an argument refers
    to the N'th game controller on the system. This index is the value
    which will identify this controller in future controller events.
    
    :return: A controller identifier, or NULL if an error occurred.
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_GameControllerOpen(joystick_index_c)
    if rc == ffi.NULL: raise SDLError()
    return GameController(rc)

def gameControllerUpdate():
    """
    ``void SDL_GameControllerUpdate(void)``
    
    Update the current state of the open game controllers.
    
    This is called automatically by the event loop if any game controller
    events are enabled.
    """
    lib.SDL_GameControllerUpdate()

def getAssertionHandler(puserdata):
    """
    ``SDL_assert_state(* SDL_GetAssertionHandler(void * *))(SDL_assert_data const *, void *)``
    
    Get the current assertion handler.
    
    This returns the function pointer that is called when an assertion is
    triggered. This is either the value last passed to
    SDL_SetAssertionHandler(), or if no application-specified function is
    set, is equivalent to calling SDL_GetDefaultAssertionHandler().
    
    :param puserdata: Pointer to a void*, which will store the "userdata"
        pointer that was passed to SDL_SetAssertionHandler(). This value
        will always be NULL for the default handler. If you don't care
        about this data, it is safe to pass a NULL pointer to this
        function to ignore it.
    :return: The SDL_AssertionHandler that is called when an assert
        triggers.
    """
    puserdata_c = unbox(puserdata, 'void * *')
    rc = lib.SDL_GetAssertionHandler(puserdata_c)
    return assert_state(rc)

def getAssertionReport():
    """
    ``SDL_assert_data const * SDL_GetAssertionReport(void)``
    
    Get a list of all assertion failures.
    
    Get all assertions triggered since last call to
    SDL_ResetAssertionReport(), or the start of the program.
    
    The proper way to examine this data looks something like this:
    
    const SDL_assert_data *item = SDL_GetAssertionReport(); while (item) {
    printf("'%s', %s (%s:%d), triggered %u times, always ignore: %s.\n",
    item->condition, item->function, item->filename, item->linenum,
    item->trigger_count, item->always_ignore ? "yes" : "no"); item =
    item->next; }
    
    :return: List of all assertions.
    
    See also SDL_ResetAssertionReport
    """
    rc = lib.SDL_GetAssertionReport()
    return assert_data(rc)

def getAudioDeviceName(index, iscapture):
    """
    ``char const * SDL_GetAudioDeviceName(int, int)``
    
    Get the human-readable name of a specific audio device. Must be a
    value between 0 and (number of audio devices-1). Only valid after a
    successfully initializing the audio subsystem. The values returned by
    this function reflect the latest call to SDL_GetNumAudioDevices();
    recall that function to redetect available hardware.
    
    The string returned by this function is UTF-8 encoded, read-only, and
    managed internally. You are not to free it. If you need to keep the
    string for any length of time, you should make your own copy of it, as
    it will be invalid next time any of several other SDL functions is
    called.
    """
    index_c = index
    iscapture_c = iscapture
    rc = lib.SDL_GetAudioDeviceName(index_c, iscapture_c)
    return ffi.string(rc).decode('utf-8')

def getAudioDeviceStatus(dev):
    """
    ``SDL_AudioStatus SDL_GetAudioDeviceStatus(unsigned int)``
    """
    dev_c = dev
    rc = lib.SDL_GetAudioDeviceStatus(dev_c)
    return rc

def getAudioDriver(index):
    """
    ``char const * SDL_GetAudioDriver(int)``
    """
    index_c = index
    rc = lib.SDL_GetAudioDriver(index_c)
    return ffi.string(rc).decode('utf-8')

def getAudioStatus():
    """
    ``SDL_AudioStatus SDL_GetAudioStatus(void)``
    """
    rc = lib.SDL_GetAudioStatus()
    return rc

def getBasePath():
    """
    ``char * SDL_GetBasePath(void)``
    
    Get the path where the application resides.
    
    Get the "base path". This is the directory where the application was
    run from, which is probably the installation directory, and may or may
    not be the process's current working directory.
    
    This returns an absolute path in UTF-8 encoding, and is guaranteed to
    end with a path separator ('\' on Windows, '/' most other places).
    
    The pointer returned by this function is owned by you. Please call
    SDL_free() on the pointer when you are done with it, or it will be a
    memory leak. This is not necessarily a fast call, though, so you
    should call this once near startup and save the string if you need it.
    
    Some platforms can't determine the application's path, and on other
    platforms, this might be meaningless. In such cases, this function
    will return NULL.
    
    :return: String of base dir in UTF-8 encoding, or NULL on error.
    
    See also SDL_GetPrefPath
    """
    rc = lib.SDL_GetBasePath()
    if rc == ffi.NULL: raise SDLError()
    return ffi.string(rc).decode('utf-8')

def getCPUCacheLineSize():
    """
    ``int SDL_GetCPUCacheLineSize(void)``
    
    This function returns the L1 cache line size of the CPU
    
    This is useful for determining multi-threaded structure padding or
    SIMD prefetch sizes.
    """
    rc = lib.SDL_GetCPUCacheLineSize()
    return rc

def getCPUCount():
    """
    ``int SDL_GetCPUCount(void)``
    
    This function returns the number of CPU cores available.
    """
    rc = lib.SDL_GetCPUCount()
    return rc

def getClipRect(surface, rect):
    """
    ``void SDL_GetClipRect(SDL_Surface *, SDL_Rect *)``
    
    Gets the clipping rectangle for the destination surface in a blit.
    
    rect must be a pointer to a valid rectangle which will be filled with
    the correct values.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    rect_c = unbox(rect, 'SDL_Rect *')
    lib.SDL_GetClipRect(surface_c, rect_c)

def getClipboardText():
    """
    ``char * SDL_GetClipboardText(void)``
    
    Get UTF-8 text from the clipboard, which must be freed with SDL_free()
    
    See also SDL_SetClipboardText()
    """
    rc = lib.SDL_GetClipboardText()
    return ffi.string(rc).decode('utf-8')

def getClosestDisplayMode(displayIndex, mode, closest):
    """
    ``SDL_DisplayMode * SDL_GetClosestDisplayMode(int, SDL_DisplayMode const *, SDL_DisplayMode *)``
    
    Get the closest match to the requested display mode.
    
    :param displayIndex: The index of display from which mode should be
        queried.
    :param mode: The desired display mode
    :param closest: A pointer to a display mode to be filled in with the
        closest match of the available display modes.
    :return: The passed in value
    
    The available display modes are scanned, and closest is filled in with
    the closest mode matching the requested mode and returned. The mode
    format and refresh_rate default to the desktop mode if they are 0. The
    modes are scanned with size being first priority, format being second
    priority, and finally checking the refresh_rate. If all the available
    modes are too small, then NULL is returned.
    
    See also SDL_GetNumDisplayModes()
    """
    displayIndex_c = displayIndex
    mode_c = unbox(mode, 'SDL_DisplayMode const *')
    closest_c = unbox(closest, 'SDL_DisplayMode *')
    rc = lib.SDL_GetClosestDisplayMode(displayIndex_c, mode_c, closest_c)
    return DisplayMode(rc)

def getColorKey(surface, key=None):
    """
    ``int SDL_GetColorKey(SDL_Surface *, unsigned int *)``
    
    Gets the color key (transparent pixel) in a blittable surface.
    
    :param surface: The surface to update
    :param key: A pointer filled in with the transparent pixel in the
        native surface format
    :return: 0 on success, or -1 if the surface is not valid or colorkey
        is not enabled.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    key_c = unbox(key, 'unsigned int *')
    rc = lib.SDL_GetColorKey(surface_c, key_c)
    return (rc, key_c[0])

def getCurrentAudioDriver():
    """
    ``char const * SDL_GetCurrentAudioDriver(void)``
    
    This function returns the name of the current audio driver, or NULL if
    no driver has been initialized.
    """
    rc = lib.SDL_GetCurrentAudioDriver()
    return ffi.string(rc).decode('utf-8')

def getCurrentDisplayMode(displayIndex, mode):
    """
    ``int SDL_GetCurrentDisplayMode(int, SDL_DisplayMode *)``
    
    Fill in information about the current display mode.
    """
    displayIndex_c = displayIndex
    mode_c = unbox(mode, 'SDL_DisplayMode *')
    rc = lib.SDL_GetCurrentDisplayMode(displayIndex_c, mode_c)
    return rc

def getCurrentVideoDriver():
    """
    ``char const * SDL_GetCurrentVideoDriver(void)``
    
    Returns the name of the currently initialized video driver.
    
    :return: The name of the current video driver or NULL if no driver has
        been initialized
    
    See also SDL_GetNumVideoDrivers()
    """
    rc = lib.SDL_GetCurrentVideoDriver()
    return ffi.string(rc).decode('utf-8')

def getCursor():
    """
    ``SDL_Cursor * SDL_GetCursor(void)``
    
    Return the active cursor.
    """
    rc = lib.SDL_GetCursor()
    return Cursor(rc)

def getDefaultAssertionHandler():
    """
    ``SDL_assert_state(* SDL_GetDefaultAssertionHandler(void))(SDL_assert_data const *, void *)``
    
    Get the default assertion handler.
    
    This returns the function pointer that is called by default when an
    assertion is triggered. This is an internal function provided by SDL,
    that is used for assertions when SDL_SetAssertionHandler() hasn't been
    used to provide a different function.
    
    :return: The default SDL_AssertionHandler that is called when an
        assert triggers.
    """
    rc = lib.SDL_GetDefaultAssertionHandler()
    return assert_state(rc)

def getDefaultCursor():
    """
    ``SDL_Cursor * SDL_GetDefaultCursor(void)``
    
    Return the default cursor.
    """
    rc = lib.SDL_GetDefaultCursor()
    return Cursor(rc)

def getDesktopDisplayMode(displayIndex, mode):
    """
    ``int SDL_GetDesktopDisplayMode(int, SDL_DisplayMode *)``
    
    Fill in information about the desktop display mode.
    """
    displayIndex_c = displayIndex
    mode_c = unbox(mode, 'SDL_DisplayMode *')
    rc = lib.SDL_GetDesktopDisplayMode(displayIndex_c, mode_c)
    return rc

def getDisplayBounds(displayIndex, rect):
    """
    ``int SDL_GetDisplayBounds(int, SDL_Rect *)``
    
    Get the desktop area represented by a display, with the primary
    display located at 0,0.
    
    :return: 0 on success, or -1 if the index is out of range.
    
    See also SDL_GetNumVideoDisplays()
    """
    displayIndex_c = displayIndex
    rect_c = unbox(rect, 'SDL_Rect *')
    rc = lib.SDL_GetDisplayBounds(displayIndex_c, rect_c)
    return rc

def getDisplayMode(displayIndex, modeIndex, mode):
    """
    ``int SDL_GetDisplayMode(int, int, SDL_DisplayMode *)``
    
    Fill in information about a specific display mode.
    
    The display modes are sorted in this priority: bits per pixel -> more
    colors to fewer colors
    
    width -> largest to smallest
    
    height -> largest to smallest
    
    refresh rate -> highest to lowest
    
    See also SDL_GetNumDisplayModes()
    """
    displayIndex_c = displayIndex
    modeIndex_c = modeIndex
    mode_c = unbox(mode, 'SDL_DisplayMode *')
    rc = lib.SDL_GetDisplayMode(displayIndex_c, modeIndex_c, mode_c)
    return rc

def getDisplayName(displayIndex):
    """
    ``char const * SDL_GetDisplayName(int)``
    
    Get the name of a display in UTF-8 encoding.
    
    :return: The name of a display, or NULL for an invalid display index.
    
    See also SDL_GetNumVideoDisplays()
    """
    displayIndex_c = displayIndex
    rc = lib.SDL_GetDisplayName(displayIndex_c)
    return ffi.string(rc).decode('utf-8')

def getError():
    """
    ``char const * SDL_GetError(void)``
    """
    rc = lib.SDL_GetError()
    return ffi.string(rc).decode('utf-8')

def getEventFilter(filter, userdata):
    """
    ``SDL_bool SDL_GetEventFilter(int(* *)(void *, SDL_Event *), void * *)``
    
    Return the current event filter - can be used to "chain" filters. If
    there is no event filter set, this function returns SDL_FALSE.
    """
    filter_c = unbox(filter, 'int(* *)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void * *')
    rc = lib.SDL_GetEventFilter(filter_c, userdata_c)
    return rc

def getHint(name):
    """
    ``char const * SDL_GetHint(char const *)``
    
    Get a hint.
    
    :return: The string value of a hint variable.
    """
    name_c = u8(name)
    rc = lib.SDL_GetHint(name_c)
    return ffi.string(rc).decode('utf-8')

def getKeyFromName(name):
    """
    ``int32_t SDL_GetKeyFromName(char const *)``
    
    Get a key code from a human-readable name.
    
    :return: key code, or SDLK_UNKNOWN if the name wasn't recognized
    
    See also SDL_Keycode
    """
    name_c = u8(name)
    rc = lib.SDL_GetKeyFromName(name_c)
    return rc

def getKeyFromScancode(scancode):
    """
    ``int32_t SDL_GetKeyFromScancode(SDL_Scancode)``
    
    Get the key code corresponding to the given scancode according to the
    current keyboard layout.
    
    See SDL_Keycode for details.
    
    See also SDL_GetKeyName()
    """
    scancode_c = scancode
    rc = lib.SDL_GetKeyFromScancode(scancode_c)
    return rc

def getKeyName(key):
    """
    ``char const * SDL_GetKeyName(int32_t)``
    
    Get a human-readable name for a key.
    
    :return: A pointer to a UTF-8 string that stays valid at least until
        the next call to this function. If you need it around any longer,
        you must copy it. If the key doesn't have a name, this function
        returns an empty string ("").
    
    See also SDL_Key
    """
    key_c = key
    rc = lib.SDL_GetKeyName(key_c)
    return ffi.string(rc).decode('utf-8')

def getKeyboardFocus():
    """
    ``SDL_Window * SDL_GetKeyboardFocus(void)``
    
    Get the window which currently has keyboard focus.
    """
    rc = lib.SDL_GetKeyboardFocus()
    return Window(rc)

def getKeyboardState(numkeys=None):
    """
    ``unsigned char const * SDL_GetKeyboardState(int *)``
    
    Get a snapshot of the current state of the keyboard.
    
    :param numkeys: if non-NULL, receives the length of the returned
        array.
    :return: An array of key states. Indexes into this array are obtained
        by using
    
    Example:::
    
       const Uint8 *state = SDL_GetKeyboardState(NULL);
       if ( state[SDL_SCANCODE_RETURN] )   {
           printf("<RETURN> is pressed.\n");
       }
    
    """
    numkeys_c = unbox(numkeys, 'int *')
    rc = lib.SDL_GetKeyboardState(numkeys_c)
    return (rc, numkeys_c[0])

def getModState():
    """
    ``SDL_Keymod SDL_GetModState(void)``
    
    Get the current key modifier state for the keyboard.
    """
    rc = lib.SDL_GetModState()
    return rc

def getMouseFocus():
    """
    ``SDL_Window * SDL_GetMouseFocus(void)``
    
    Get the window which currently has mouse focus.
    """
    rc = lib.SDL_GetMouseFocus()
    return Window(rc)

def getMouseState(x=None, y=None):
    """
    ``unsigned int SDL_GetMouseState(int *, int *)``
    
    Retrieve the current state of the mouse.
    
    The current button state is returned as a button bitmask, which can be
    tested using the SDL_BUTTON(X) macros, and x and y are set to the
    mouse cursor position relative to the focus window for the currently
    selected mouse. You can pass NULL for either x or y.
    """
    x_c = unbox(x, 'int *')
    y_c = unbox(y, 'int *')
    rc = lib.SDL_GetMouseState(x_c, y_c)
    return (rc, x_c[0], y_c[0])

def getNumAudioDevices(iscapture):
    """
    ``int SDL_GetNumAudioDevices(int)``
    
    Get the number of available devices exposed by the current driver.
    Only valid after a successfully initializing the audio subsystem.
    Returns -1 if an explicit list of devices can't be determined; this is
    not an error. For example, if SDL is set up to talk to a remote audio
    server, it can't list every one available on the Internet, but it will
    still allow a specific host to be specified to SDL_OpenAudioDevice().
    
    In many common cases, when this function returns a value <= 0, it can
    still successfully open the default device (NULL for first argument of
    SDL_OpenAudioDevice()).
    """
    iscapture_c = iscapture
    rc = lib.SDL_GetNumAudioDevices(iscapture_c)
    return rc

def getNumAudioDrivers():
    """
    ``int SDL_GetNumAudioDrivers(void)``
    """
    rc = lib.SDL_GetNumAudioDrivers()
    return rc

def getNumDisplayModes(displayIndex):
    """
    ``int SDL_GetNumDisplayModes(int)``
    
    Returns the number of available display modes.
    
    See also SDL_GetDisplayMode()
    """
    displayIndex_c = displayIndex
    rc = lib.SDL_GetNumDisplayModes(displayIndex_c)
    return rc

def getNumRenderDrivers():
    """
    ``int SDL_GetNumRenderDrivers(void)``
    
    Get the number of 2D rendering drivers available for the current
    display.
    
    A render driver is a set of code that handles rendering and texture
    management on a particular display. Normally there is only one, but
    some drivers may have several available with different capabilities.
    
    See also SDL_GetRenderDriverInfo()
    """
    rc = lib.SDL_GetNumRenderDrivers()
    return rc

def getNumTouchDevices():
    """
    ``int SDL_GetNumTouchDevices(void)``
    
    Get the number of registered touch devices.
    """
    rc = lib.SDL_GetNumTouchDevices()
    return rc

def getNumTouchFingers(touchID):
    """
    ``int SDL_GetNumTouchFingers(int64_t)``
    
    Get the number of active fingers for a given touch device.
    """
    touchID_c = touchID
    rc = lib.SDL_GetNumTouchFingers(touchID_c)
    return rc

def getNumVideoDisplays():
    """
    ``int SDL_GetNumVideoDisplays(void)``
    
    Returns the number of available video displays.
    
    See also SDL_GetDisplayBounds()
    """
    rc = lib.SDL_GetNumVideoDisplays()
    return rc

def getNumVideoDrivers():
    """
    ``int SDL_GetNumVideoDrivers(void)``
    
    Get the number of video drivers compiled into SDL.
    
    See also SDL_GetVideoDriver()
    """
    rc = lib.SDL_GetNumVideoDrivers()
    return rc

def getPerformanceCounter():
    """
    ``unsigned long SDL_GetPerformanceCounter(void)``
    
    Get the current value of the high resolution counter.
    """
    rc = lib.SDL_GetPerformanceCounter()
    return rc

def getPerformanceFrequency():
    """
    ``unsigned long SDL_GetPerformanceFrequency(void)``
    
    Get the count per second of the high resolution counter.
    """
    rc = lib.SDL_GetPerformanceFrequency()
    return rc

def getPixelFormatName(format):
    """
    ``char const * SDL_GetPixelFormatName(unsigned int)``
    
    Get the human readable name of a pixel format.
    """
    format_c = format
    rc = lib.SDL_GetPixelFormatName(format_c)
    return ffi.string(rc).decode('utf-8')

def getPlatform():
    """
    ``char const * SDL_GetPlatform(void)``
    
    Gets the name of the platform.
    """
    rc = lib.SDL_GetPlatform()
    return ffi.string(rc).decode('utf-8')

def getPowerInfo(secs=None, pct=None):
    """
    ``SDL_PowerState SDL_GetPowerInfo(int *, int *)``
    
    Get the current power supply details.
    
    :param secs: Seconds of battery life left. You can pass a NULL here if
        you don't care. Will return -1 if we can't determine a value, or
        we're not running on a battery.
    :param pct: Percentage of battery life left, between 0 and 100. You
        can pass a NULL here if you don't care. Will return -1 if we can't
        determine a value, or we're not running on a battery.
    :return: The state of the battery (if any).
    """
    secs_c = unbox(secs, 'int *')
    pct_c = unbox(pct, 'int *')
    rc = lib.SDL_GetPowerInfo(secs_c, pct_c)
    return (rc, secs_c[0], pct_c[0])

def getPrefPath(org, app):
    """
    ``char * SDL_GetPrefPath(char const *, char const *)``
    
    Get the user-and-app-specific path where files can be written.
    
    Get the "pref dir". This is meant to be where users can write personal
    files (preferences and save games, etc) that are specific to your
    application. This directory is unique per user, per application.
    
    This function will decide the appropriate location in the native
    filesystem, create the directory if necessary, and return a string of
    the absolute path to the directory in UTF-8 encoding.
    
    On Windows, the string might look like:
    "C:\\Users\\bob\\AppData\\Roaming\\My Company\\My Program Name\\"
    
    On Linux, the string might look like: "/home/bob/.local/share/My
    Program Name/"
    
    On Mac OS X, the string might look like:
    "/Users/bob/Library/Application Support/My Program Name/"
    
    (etc.)
    
    You specify the name of your organization (if it's not a real
    organization, your name or an Internet domain you own might do) and
    the name of your application. These should be untranslated proper
    names.
    
    Both the org and app strings may become part of a directory name, so
    please follow these rules:
    
    Try to use the same org string (including case-sensitivity) for all
    your applications that use this function.
    
    Always use a unique app string for each one, and make sure it never
    changes for an app once you've decided on it.
    
    Unicode characters are legal, as long as it's UTF-8 encoded, but...
    
    ...only use letters, numbers, and spaces. Avoid punctuation like "Game
    Name 2: Bad Guy's Revenge!" ... "Game Name 2" is sufficient.
    
    This returns an absolute path in UTF-8 encoding, and is guaranteed to
    end with a path separator ('\' on Windows, '/' most other places).
    
    The pointer returned by this function is owned by you. Please call
    SDL_free() on the pointer when you are done with it, or it will be a
    memory leak. This is not necessarily a fast call, though, so you
    should call this once near startup and save the string if you need it.
    
    You should assume the path returned by this function is the only safe
    place to write files (and that SDL_GetBasePath(), while it might be
    writable, or even the parent of the returned path, aren't where you
    should be writing things).
    
    Some platforms can't determine the pref path, and on other platforms,
    this might be meaningless. In such cases, this function will return
    NULL.
    
    :param org: The name of your organization.
    :param app: The name of your application.
    :return: UTF-8 string of user dir in platform-dependent notation. NULL
        if there's a problem (creating directory failed, etc).
    
    See also SDL_GetBasePath
    """
    org_c = u8(org)
    app_c = u8(app)
    rc = lib.SDL_GetPrefPath(org_c, app_c)
    return ffi.string(rc).decode('utf-8')

def getRGB(pixel, format, r=None, g=None, b=None):
    """
    ``void SDL_GetRGB(unsigned int, SDL_PixelFormat const *, unsigned char *, unsigned char *, unsigned char *)``
    
    Get the RGB components from a pixel of the specified format.
    
    See also SDL_GetRGBA
    """
    pixel_c = pixel
    format_c = unbox(format, 'SDL_PixelFormat const *')
    r_c = unbox(r, 'unsigned char *')
    g_c = unbox(g, 'unsigned char *')
    b_c = unbox(b, 'unsigned char *')
    lib.SDL_GetRGB(pixel_c, format_c, r_c, g_c, b_c)
    return (r_c[0], g_c[0], b_c[0])

def getRGBA(pixel, format, r=None, g=None, b=None, a=None):
    """
    ``void SDL_GetRGBA(unsigned int, SDL_PixelFormat const *, unsigned char *, unsigned char *, unsigned char *, unsigned char *)``
    
    Get the RGBA components from a pixel of the specified format.
    
    See also SDL_GetRGB
    """
    pixel_c = pixel
    format_c = unbox(format, 'SDL_PixelFormat const *')
    r_c = unbox(r, 'unsigned char *')
    g_c = unbox(g, 'unsigned char *')
    b_c = unbox(b, 'unsigned char *')
    a_c = unbox(a, 'unsigned char *')
    lib.SDL_GetRGBA(pixel_c, format_c, r_c, g_c, b_c, a_c)
    return (r_c[0], g_c[0], b_c[0], a_c[0])

def getRelativeMouseMode():
    """
    ``SDL_bool SDL_GetRelativeMouseMode(void)``
    
    Query whether relative mouse mode is enabled.
    
    See also SDL_SetRelativeMouseMode()
    """
    rc = lib.SDL_GetRelativeMouseMode()
    return rc

def getRelativeMouseState(x=None, y=None):
    """
    ``unsigned int SDL_GetRelativeMouseState(int *, int *)``
    
    Retrieve the relative state of the mouse.
    
    The current button state is returned as a button bitmask, which can be
    tested using the SDL_BUTTON(X) macros, and x and y are set to the
    mouse deltas since the last call to SDL_GetRelativeMouseState().
    """
    x_c = unbox(x, 'int *')
    y_c = unbox(y, 'int *')
    rc = lib.SDL_GetRelativeMouseState(x_c, y_c)
    return (rc, x_c[0], y_c[0])

def getRenderDrawBlendMode(renderer, blendMode):
    """
    ``int SDL_GetRenderDrawBlendMode(SDL_Renderer *, SDL_BlendMode *)``
    
    Get the blend mode used for drawing operations.
    
    :param renderer: The renderer from which blend mode should be queried.
    :param blendMode: A pointer filled in with the current blend mode.
    :return: 0 on success, or -1 on error
    
    See also SDL_SetRenderDrawBlendMode()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    blendMode_c = unbox(blendMode, 'SDL_BlendMode *')
    rc = lib.SDL_GetRenderDrawBlendMode(renderer_c, blendMode_c)
    if rc == -1: raise SDLError()
    return rc

def getRenderDrawColor(renderer, r=None, g=None, b=None, a=None):
    """
    ``int SDL_GetRenderDrawColor(SDL_Renderer *, unsigned char *, unsigned char *, unsigned char *, unsigned char *)``
    
    Get the color used for drawing operations (Rect, Line and Clear).
    
    :param renderer: The renderer from which drawing color should be
        queried.
    :param r: A pointer to the red value used to draw on the rendering
        target.
    :param g: A pointer to the green value used to draw on the rendering
        target.
    :param b: A pointer to the blue value used to draw on the rendering
        target.
    :param a: A pointer to the alpha value used to draw on the rendering
        target, usually SDL_ALPHA_OPAQUE (255).
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    r_c = unbox(r, 'unsigned char *')
    g_c = unbox(g, 'unsigned char *')
    b_c = unbox(b, 'unsigned char *')
    a_c = unbox(a, 'unsigned char *')
    rc = lib.SDL_GetRenderDrawColor(renderer_c, r_c, g_c, b_c, a_c)
    if rc == -1: raise SDLError()
    return (rc, r_c[0], g_c[0], b_c[0], a_c[0])

def getRenderDriverInfo(index, info):
    """
    ``int SDL_GetRenderDriverInfo(int, SDL_RendererInfo *)``
    
    Get information about a specific 2D rendering driver for the current
    display.
    
    :param index: The index of the driver to query information about.
    :param info: A pointer to an SDL_RendererInfo struct to be filled with
        information on the rendering driver.
    :return: 0 on success, -1 if the index was out of range.
    
    See also SDL_CreateRenderer()
    """
    index_c = index
    info_c = unbox(info, 'SDL_RendererInfo *')
    rc = lib.SDL_GetRenderDriverInfo(index_c, info_c)
    return rc

def getRenderTarget(renderer):
    """
    ``SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *)``
    
    Get the current render target or NULL for the default render target.
    
    :return: The current render target
    
    See also SDL_SetRenderTarget()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rc = lib.SDL_GetRenderTarget(renderer_c)
    return Texture(rc)

def getRenderer(window):
    """
    ``SDL_Renderer * SDL_GetRenderer(SDL_Window *)``
    
    Get the renderer associated with a window.
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetRenderer(window_c)
    return Renderer(rc)

def getRendererInfo(renderer, info):
    """
    ``int SDL_GetRendererInfo(SDL_Renderer *, SDL_RendererInfo *)``
    
    Get information about a rendering context.
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    info_c = unbox(info, 'SDL_RendererInfo *')
    rc = lib.SDL_GetRendererInfo(renderer_c, info_c)
    return rc

def getRendererOutputSize(renderer, w=None, h=None):
    """
    ``int SDL_GetRendererOutputSize(SDL_Renderer *, int *, int *)``
    
    Get the output size of a rendering context.
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    rc = lib.SDL_GetRendererOutputSize(renderer_c, w_c, h_c)
    return (rc, w_c[0], h_c[0])

def getRevision():
    """
    ``char const * SDL_GetRevision(void)``
    
    Get the code revision of SDL that is linked against your program.
    
    Returns an arbitrary string (a hash value) uniquely identifying the
    exact revision of the SDL library in use, and is only useful in
    comparing against other revisions. It is NOT an incrementing number.
    """
    rc = lib.SDL_GetRevision()
    return ffi.string(rc).decode('utf-8')

def getRevisionNumber():
    """
    ``int SDL_GetRevisionNumber(void)``
    
    Get the revision number of SDL that is linked against your program.
    
    Returns a number uniquely identifying the exact revision of the SDL
    library in use. It is an incrementing number based on commits to
    hg.libsdl.org.
    """
    rc = lib.SDL_GetRevisionNumber()
    return rc

def getScancodeFromKey(key):
    """
    ``SDL_Scancode SDL_GetScancodeFromKey(int32_t)``
    
    Get the scancode corresponding to the given key code according to the
    current keyboard layout.
    
    See SDL_Scancode for details.
    
    See also SDL_GetScancodeName()
    """
    key_c = key
    rc = lib.SDL_GetScancodeFromKey(key_c)
    return rc

def getScancodeFromName(name):
    """
    ``SDL_Scancode SDL_GetScancodeFromName(char const *)``
    
    Get a scancode from a human-readable name.
    
    :return: scancode, or SDL_SCANCODE_UNKNOWN if the name wasn't
        recognized
    
    See also SDL_Scancode
    """
    name_c = u8(name)
    rc = lib.SDL_GetScancodeFromName(name_c)
    return rc

def getScancodeName(scancode):
    """
    ``char const * SDL_GetScancodeName(SDL_Scancode)``
    
    Get a human-readable name for a scancode.
    
    :return: A pointer to the name for the scancode. If the scancode
        doesn't have a name, this function returns an empty string ("").
    
    See also SDL_Scancode
    """
    scancode_c = scancode
    rc = lib.SDL_GetScancodeName(scancode_c)
    return ffi.string(rc).decode('utf-8')

def getSurfaceAlphaMod(surface, alpha=None):
    """
    ``int SDL_GetSurfaceAlphaMod(SDL_Surface *, unsigned char *)``
    
    Get the additional alpha value used in blit operations.
    
    :param surface: The surface to query.
    :param alpha: A pointer filled in with the current alpha value.
    :return: 0 on success, or -1 if the surface is not valid.
    
    See also SDL_SetSurfaceAlphaMod()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    alpha_c = unbox(alpha, 'unsigned char *')
    rc = lib.SDL_GetSurfaceAlphaMod(surface_c, alpha_c)
    return (rc, alpha_c[0])

def getSurfaceBlendMode(surface, blendMode):
    """
    ``int SDL_GetSurfaceBlendMode(SDL_Surface *, SDL_BlendMode *)``
    
    Get the blend mode used for blit operations.
    
    :param surface: The surface to query.
    :param blendMode: A pointer filled in with the current blend mode.
    :return: 0 on success, or -1 if the surface is not valid.
    
    See also SDL_SetSurfaceBlendMode()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    blendMode_c = unbox(blendMode, 'SDL_BlendMode *')
    rc = lib.SDL_GetSurfaceBlendMode(surface_c, blendMode_c)
    return rc

def getSurfaceColorMod(surface, r=None, g=None, b=None):
    """
    ``int SDL_GetSurfaceColorMod(SDL_Surface *, unsigned char *, unsigned char *, unsigned char *)``
    
    Get the additional color value used in blit operations.
    
    :param surface: The surface to query.
    :param r: A pointer filled in with the current red color value.
    :param g: A pointer filled in with the current green color value.
    :param b: A pointer filled in with the current blue color value.
    :return: 0 on success, or -1 if the surface is not valid.
    
    See also SDL_SetSurfaceColorMod()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    r_c = unbox(r, 'unsigned char *')
    g_c = unbox(g, 'unsigned char *')
    b_c = unbox(b, 'unsigned char *')
    rc = lib.SDL_GetSurfaceColorMod(surface_c, r_c, g_c, b_c)
    return (rc, r_c[0], g_c[0], b_c[0])

def getSystemRAM():
    """
    ``int SDL_GetSystemRAM(void)``
    
    This function returns the amount of RAM configured in the system, in
    MB.
    """
    rc = lib.SDL_GetSystemRAM()
    return rc

def getTextureAlphaMod(texture, alpha=None):
    """
    ``int SDL_GetTextureAlphaMod(SDL_Texture *, unsigned char *)``
    
    Get the additional alpha value used in render copy operations.
    
    :param texture: The texture to query.
    :param alpha: A pointer filled in with the current alpha value.
    :return: 0 on success, or -1 if the texture is not valid.
    
    See also SDL_SetTextureAlphaMod()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    alpha_c = unbox(alpha, 'unsigned char *')
    rc = lib.SDL_GetTextureAlphaMod(texture_c, alpha_c)
    return (rc, alpha_c[0])

def getTextureBlendMode(texture, blendMode):
    """
    ``int SDL_GetTextureBlendMode(SDL_Texture *, SDL_BlendMode *)``
    
    Get the blend mode used for texture copy operations.
    
    :param texture: The texture to query.
    :param blendMode: A pointer filled in with the current blend mode.
    :return: 0 on success, or -1 if the texture is not valid.
    
    See also SDL_SetTextureBlendMode()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    blendMode_c = unbox(blendMode, 'SDL_BlendMode *')
    rc = lib.SDL_GetTextureBlendMode(texture_c, blendMode_c)
    return rc

def getTextureColorMod(texture, r=None, g=None, b=None):
    """
    ``int SDL_GetTextureColorMod(SDL_Texture *, unsigned char *, unsigned char *, unsigned char *)``
    
    Get the additional color value used in render copy operations.
    
    :param texture: The texture to query.
    :param r: A pointer filled in with the current red color value.
    :param g: A pointer filled in with the current green color value.
    :param b: A pointer filled in with the current blue color value.
    :return: 0 on success, or -1 if the texture is not valid.
    
    See also SDL_SetTextureColorMod()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    r_c = unbox(r, 'unsigned char *')
    g_c = unbox(g, 'unsigned char *')
    b_c = unbox(b, 'unsigned char *')
    rc = lib.SDL_GetTextureColorMod(texture_c, r_c, g_c, b_c)
    return (rc, r_c[0], g_c[0], b_c[0])

def getThreadID(thread):
    """
    ``unsigned long SDL_GetThreadID(SDL_Thread *)``
    
    Get the thread identifier for the specified thread.
    
    Equivalent to SDL_ThreadID() if the specified thread is NULL.
    """
    thread_c = unbox(thread, 'SDL_Thread *')
    rc = lib.SDL_GetThreadID(thread_c)
    return rc

def getThreadName(thread):
    """
    ``char const * SDL_GetThreadName(SDL_Thread *)``
    
    Get the thread name, as it was specified in SDL_CreateThread(). This
    function returns a pointer to a UTF-8 string that names the specified
    thread, or NULL if it doesn't have a name. This is internal memory,
    not to be free()'d by the caller, and remains valid until the
    specified thread is cleaned up by SDL_WaitThread().
    """
    thread_c = unbox(thread, 'SDL_Thread *')
    rc = lib.SDL_GetThreadName(thread_c)
    return ffi.string(rc).decode('utf-8')

def getTicks():
    """
    ``unsigned int SDL_GetTicks(void)``
    
    Get the number of milliseconds since the SDL library initialization.
    
    This value wraps if the program runs for more than ~49 days.
    """
    rc = lib.SDL_GetTicks()
    return rc

def getTouchDevice(index):
    """
    ``int64_t SDL_GetTouchDevice(int)``
    
    Get the touch ID with the given index, or 0 if the index is invalid.
    """
    index_c = index
    rc = lib.SDL_GetTouchDevice(index_c)
    return rc

def getTouchFinger(touchID, index):
    """
    ``SDL_Finger * SDL_GetTouchFinger(int64_t, int)``
    
    Get the finger object of the given touch, with the given index.
    """
    touchID_c = touchID
    index_c = index
    rc = lib.SDL_GetTouchFinger(touchID_c, index_c)
    return Finger(rc)

def getVersion(ver):
    """
    ``void SDL_GetVersion(SDL_version *)``
    
    Get the version of SDL that is linked against your program.
    
    If you are linking to SDL dynamically, then it is possible that the
    current version will be different than the version you compiled
    against. This function returns the current version, while
    SDL_VERSION() is a macro that tells you what version you compiled
    with.
    
    ::
    
       SDL_version compiled;
       SDL_version linked;
    
    
    
       SDL_VERSION(&compiled);
       SDL_GetVersion(&linked);
       printf("We compiled against SDL version %d.%d.%d ...\n",
              compiled.major, compiled.minor, compiled.patch);
       printf("But we linked against SDL version %d.%d.%d.\n",
              linked.major, linked.minor, linked.patch);
    
    
    This function may be called safely at any time, even before
    SDL_Init().
    
    See also SDL_VERSION
    """
    ver_c = unbox(ver, 'SDL_version *')
    lib.SDL_GetVersion(ver_c)

def getVideoDriver(index):
    """
    ``char const * SDL_GetVideoDriver(int)``
    
    Get the name of a built in video driver.
    
    The video drivers are presented in the order in which they are
    normally checked during initialization.
    
    See also SDL_GetNumVideoDrivers()
    """
    index_c = index
    rc = lib.SDL_GetVideoDriver(index_c)
    return ffi.string(rc).decode('utf-8')

def getWindowBrightness(window):
    """
    ``float SDL_GetWindowBrightness(SDL_Window *)``
    
    Get the brightness (gamma correction) for a window.
    
    :return: The last brightness value passed to
    
    See also SDL_SetWindowBrightness()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowBrightness(window_c)
    return rc

def getWindowData(window, name):
    """
    ``void * SDL_GetWindowData(SDL_Window *, char const *)``
    
    Retrieve the data pointer associated with a window.
    
    :param window: The window to query.
    :param name: The name of the pointer.
    :return: The value associated with 'name'
    
    See also SDL_SetWindowData()
    """
    window_c = unbox(window, 'SDL_Window *')
    name_c = u8(name)
    rc = lib.SDL_GetWindowData(window_c, name_c)
    return rc

def getWindowDisplayIndex(window):
    """
    ``int SDL_GetWindowDisplayIndex(SDL_Window *)``
    
    Get the display index associated with a window.
    
    :return: the display index of the display containing the center of the
        window, or -1 on error.
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowDisplayIndex(window_c)
    if rc == -1: raise SDLError()
    return rc

def getWindowDisplayMode(window, mode):
    """
    ``int SDL_GetWindowDisplayMode(SDL_Window *, SDL_DisplayMode *)``
    
    Fill in information about the display mode used when a fullscreen
    window is visible.
    
    See also SDL_SetWindowDisplayMode()
    """
    window_c = unbox(window, 'SDL_Window *')
    mode_c = unbox(mode, 'SDL_DisplayMode *')
    rc = lib.SDL_GetWindowDisplayMode(window_c, mode_c)
    return rc

def getWindowFlags(window):
    """
    ``unsigned int SDL_GetWindowFlags(SDL_Window *)``
    
    Get the window flags.
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowFlags(window_c)
    return rc

def getWindowFromID(id):
    """
    ``SDL_Window * SDL_GetWindowFromID(unsigned int)``
    
    Get a window from a stored ID, or NULL if it doesn't exist.
    """
    id_c = id
    rc = lib.SDL_GetWindowFromID(id_c)
    return Window(rc)

def getWindowGammaRamp(window, red=None, green=None, blue=None):
    """
    ``int SDL_GetWindowGammaRamp(SDL_Window *, unsigned short *, unsigned short *, unsigned short *)``
    
    Get the gamma ramp for a window.
    
    :param window: The window from which the gamma ramp should be queried.
    :param red: A pointer to a 256 element array of 16-bit quantities to
        hold the translation table for the red channel, or NULL.
    :param green: A pointer to a 256 element array of 16-bit quantities to
        hold the translation table for the green channel, or NULL.
    :param blue: A pointer to a 256 element array of 16-bit quantities to
        hold the translation table for the blue channel, or NULL.
    :return: 0 on success, or -1 if gamma ramps are unsupported.
    
    See also SDL_SetWindowGammaRamp()
    """
    window_c = unbox(window, 'SDL_Window *')
    red_c = unbox(red, 'unsigned short *', nullable=True)
    green_c = unbox(green, 'unsigned short *', nullable=True)
    blue_c = unbox(blue, 'unsigned short *', nullable=True)
    rc = lib.SDL_GetWindowGammaRamp(window_c, red_c, green_c, blue_c)
    return (rc, red_c[0], green_c[0], blue_c[0])

def getWindowGrab(window):
    """
    ``SDL_bool SDL_GetWindowGrab(SDL_Window *)``
    
    Get a window's input grab mode.
    
    :return: This returns SDL_TRUE if input is grabbed, and SDL_FALSE
        otherwise.
    
    See also SDL_SetWindowGrab()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowGrab(window_c)
    return rc

def getWindowID(window):
    """
    ``unsigned int SDL_GetWindowID(SDL_Window *)``
    
    Get the numeric ID of a window, for logging purposes.
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowID(window_c)
    return rc

def getWindowMaximumSize(window, w=None, h=None):
    """
    ``void SDL_GetWindowMaximumSize(SDL_Window *, int *, int *)``
    
    Get the maximum size of a window's client area.
    
    :param window: The window to query.
    :param w: Pointer to variable for storing the maximum width, may be
        NULL
    :param h: Pointer to variable for storing the maximum height, may be
        NULL
    
    See also SDL_GetWindowMinimumSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    lib.SDL_GetWindowMaximumSize(window_c, w_c, h_c)
    return (w_c[0], h_c[0])

def getWindowMinimumSize(window, w=None, h=None):
    """
    ``void SDL_GetWindowMinimumSize(SDL_Window *, int *, int *)``
    
    Get the minimum size of a window's client area.
    
    :param window: The window to query.
    :param w: Pointer to variable for storing the minimum width, may be
        NULL
    :param h: Pointer to variable for storing the minimum height, may be
        NULL
    
    See also SDL_GetWindowMaximumSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    lib.SDL_GetWindowMinimumSize(window_c, w_c, h_c)
    return (w_c[0], h_c[0])

def getWindowPixelFormat(window):
    """
    ``unsigned int SDL_GetWindowPixelFormat(SDL_Window *)``
    
    Get the pixel format associated with the window.
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowPixelFormat(window_c)
    return rc

def getWindowPosition(window, x=None, y=None):
    """
    ``void SDL_GetWindowPosition(SDL_Window *, int *, int *)``
    
    Get the position of a window.
    
    :param window: The window to query.
    :param x: Pointer to variable for storing the x position, may be NULL
    :param y: Pointer to variable for storing the y position, may be NULL
    
    See also SDL_SetWindowPosition()
    """
    window_c = unbox(window, 'SDL_Window *')
    x_c = unbox(x, 'int *')
    y_c = unbox(y, 'int *')
    lib.SDL_GetWindowPosition(window_c, x_c, y_c)
    return (x_c[0], y_c[0])

def getWindowSize(window, w=None, h=None):
    """
    ``void SDL_GetWindowSize(SDL_Window *, int *, int *)``
    
    Get the size of a window's client area.
    
    :param window: The window to query.
    :param w: Pointer to variable for storing the width, may be NULL
    :param h: Pointer to variable for storing the height, may be NULL
    
    See also SDL_SetWindowSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    lib.SDL_GetWindowSize(window_c, w_c, h_c)
    return (w_c[0], h_c[0])

def getWindowSurface(window):
    """
    ``SDL_Surface * SDL_GetWindowSurface(SDL_Window *)``
    
    Get the SDL surface associated with the window.
    
    :return: The window's framebuffer surface, or NULL on error.
    
    A new surface will be created with the optimal format for the window,
    if necessary. This surface will be freed when the window is destroyed.
    
    You may not combine this with 3D or the rendering API on this window.
    
    See also SDL_UpdateWindowSurface()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowSurface(window_c)
    if rc == ffi.NULL: raise SDLError()
    return Surface(rc)

def getWindowTitle(window):
    """
    ``char const * SDL_GetWindowTitle(SDL_Window *)``
    
    Get the title of a window, in UTF-8 format.
    
    See also SDL_SetWindowTitle()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_GetWindowTitle(window_c)
    return ffi.string(rc).decode('utf-8')

def hapticClose(haptic):
    """
    ``void SDL_HapticClose(SDL_Haptic *)``
    
    Closes a Haptic device previously opened with SDL_HapticOpen().
    
    :param haptic: Haptic device to close.
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    lib.SDL_HapticClose(haptic_c)

def hapticDestroyEffect(haptic, effect):
    """
    ``void SDL_HapticDestroyEffect(SDL_Haptic *, int)``
    
    Destroys a haptic effect on the device.
    
    This will stop the effect if it's running. Effects are automatically
    destroyed when the device is closed.
    
    :param haptic: Device to destroy the effect on.
    :param effect: Identifier of the effect to destroy.
    
    See also SDL_HapticNewEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    lib.SDL_HapticDestroyEffect(haptic_c, effect_c)

def hapticEffectSupported(haptic, effect):
    """
    ``int SDL_HapticEffectSupported(SDL_Haptic *, SDL_HapticEffect *)``
    
    Checks to see if effect is supported by haptic.
    
    :param haptic: Haptic device to check on.
    :param effect: Effect to check to see if it is supported.
    :return: SDL_TRUE if effect is supported, SDL_FALSE if it isn't or -1
        on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = unbox(effect, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticEffectSupported(haptic_c, effect_c)
    return rc

def hapticGetEffectStatus(haptic, effect):
    """
    ``int SDL_HapticGetEffectStatus(SDL_Haptic *, int)``
    
    Gets the status of the current effect on the haptic device.
    
    Device must support the SDL_HAPTIC_STATUS feature.
    
    :param haptic: Haptic device to query the effect status on.
    :param effect: Identifier of the effect to query its status.
    :return: 0 if it isn't playing, 1 if it is playing or -1 on error.
    
    See also SDL_HapticRunEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    rc = lib.SDL_HapticGetEffectStatus(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticIndex(haptic):
    """
    ``int SDL_HapticIndex(SDL_Haptic *)``
    
    Gets the index of a haptic device.
    
    :param haptic: Haptic device to get the index of.
    :return: The index of the haptic device or -1 on error.
    
    See also SDL_HapticOpen
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticIndex(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticName(device_index):
    """
    ``char const * SDL_HapticName(int)``
    
    Get the implementation dependent name of a Haptic device.
    
    This can be called before any joysticks are opened. If no name can be
    found, this function returns NULL.
    
    :param device_index: Index of the device to get its name.
    :return: Name of the device or NULL on error.
    
    See also SDL_NumHaptics
    """
    device_index_c = device_index
    rc = lib.SDL_HapticName(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return ffi.string(rc).decode('utf-8')

def hapticNewEffect(haptic, effect):
    """
    ``int SDL_HapticNewEffect(SDL_Haptic *, SDL_HapticEffect *)``
    
    Creates a new haptic effect on the device.
    
    :param haptic: Haptic device to create the effect on.
    :param effect: Properties of the effect to create.
    :return: The id of the effect on success or -1 on error.
    
    See also SDL_HapticUpdateEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = unbox(effect, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticNewEffect(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticNumAxes(haptic):
    """
    ``int SDL_HapticNumAxes(SDL_Haptic *)``
    
    Gets the number of haptic axes the device has.
    
    See also SDL_HapticDirection
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumAxes(haptic_c)
    return rc

def hapticNumEffects(haptic):
    """
    ``int SDL_HapticNumEffects(SDL_Haptic *)``
    
    Returns the number of effects a haptic device can store.
    
    On some platforms this isn't fully supported, and therefore is an
    approximation. Always check to see if your created effect was actually
    created and do not rely solely on SDL_HapticNumEffects().
    
    :param haptic: The haptic device to query effect max.
    :return: The number of effects the haptic device can store or -1 on
        error.
    
    See also SDL_HapticNumEffectsPlaying
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumEffects(haptic_c)
    return rc

def hapticNumEffectsPlaying(haptic):
    """
    ``int SDL_HapticNumEffectsPlaying(SDL_Haptic *)``
    
    Returns the number of effects a haptic device can play at the same
    time.
    
    This is not supported on all platforms, but will always return a
    value. Added here for the sake of completeness.
    
    :param haptic: The haptic device to query maximum playing effects.
    :return: The number of effects the haptic device can play at the same
        time or -1 on error.
    
    See also SDL_HapticNumEffects
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticNumEffectsPlaying(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticOpen(device_index):
    """
    ``SDL_Haptic * SDL_HapticOpen(int)``
    
    Opens a Haptic device for usage.
    
    The index passed as an argument refers to the N'th Haptic device on
    this system.
    
    When opening a haptic device, its gain will be set to maximum and
    autocenter will be disabled. To modify these values use
    SDL_HapticSetGain() and SDL_HapticSetAutocenter().
    
    :param device_index: Index of the device to open.
    :return: Device identifier or NULL on error.
    
    See also SDL_HapticIndex
    """
    device_index_c = device_index
    rc = lib.SDL_HapticOpen(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpenFromJoystick(joystick):
    """
    ``SDL_Haptic * SDL_HapticOpenFromJoystick(SDL_Joystick *)``
    
    Opens a Haptic device for usage from a Joystick device.
    
    You must still close the haptic device seperately. It will not be
    closed with the joystick.
    
    When opening from a joystick you should first close the haptic device
    before closing the joystick device. If not, on some implementations
    the haptic device will also get unallocated and you'll be unable to
    use force feedback on that device.
    
    :param joystick: Joystick to create a haptic device from.
    :return: A valid haptic device identifier on success or NULL on error.
    
    See also SDL_HapticOpen
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_HapticOpenFromJoystick(joystick_c)
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpenFromMouse():
    """
    ``SDL_Haptic * SDL_HapticOpenFromMouse(void)``
    
    Tries to open a haptic device from the current mouse.
    
    :return: The haptic device identifier or NULL on error.
    
    See also SDL_MouseIsHaptic
    """
    rc = lib.SDL_HapticOpenFromMouse()
    if rc == ffi.NULL: raise SDLError()
    return Haptic(rc)

def hapticOpened(device_index):
    """
    ``int SDL_HapticOpened(int)``
    
    Checks if the haptic device at index has been opened.
    
    :param device_index: Index to check to see if it has been opened.
    :return: 1 if it has been opened or 0 if it hasn't.
    
    See also SDL_HapticOpen
    """
    device_index_c = device_index
    rc = lib.SDL_HapticOpened(device_index_c)
    return rc

def hapticPause(haptic):
    """
    ``int SDL_HapticPause(SDL_Haptic *)``
    
    Pauses a haptic device.
    
    Device must support the SDL_HAPTIC_PAUSE feature. Call
    SDL_HapticUnpause() to resume playback.
    
    Do not modify the effects nor add new ones while the device is paused.
    That can cause all sorts of weird errors.
    
    :param haptic: Haptic device to pause.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticUnpause
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticPause(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticQuery(haptic):
    """
    ``unsigned int SDL_HapticQuery(SDL_Haptic *)``
    
    Gets the haptic devices supported features in bitwise matter.
    
    Example: ::
    
       if (SDL_HapticQuery(haptic) & SDL_HAPTIC_CONSTANT) {
           printf("We have constant haptic effect!");
       }
    
    
    :param haptic: The haptic device to query.
    :return: Haptic features in bitwise manner (OR'd).
    
    See also SDL_HapticNumEffects
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticQuery(haptic_c)
    return rc

def hapticRumbleInit(haptic):
    """
    ``int SDL_HapticRumbleInit(SDL_Haptic *)``
    
    Initializes the haptic device for simple rumble playback.
    
    :param haptic: Haptic device to initialize for simple rumble playback.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticOpen
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleInit(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumblePlay(haptic, strength, length):
    """
    ``int SDL_HapticRumblePlay(SDL_Haptic *, float, unsigned int)``
    
    Runs simple rumble on a haptic device.
    
    :param haptic: Haptic device to play rumble effect on.
    :param strength: Strength of the rumble to play as a 0-1 float value.
    :param length: Length of the rumble to play in milliseconds.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRumbleSupported
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    strength_c = strength
    length_c = length
    rc = lib.SDL_HapticRumblePlay(haptic_c, strength_c, length_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumbleStop(haptic):
    """
    ``int SDL_HapticRumbleStop(SDL_Haptic *)``
    
    Stops the simple rumble on a haptic device.
    
    :param haptic: Haptic to stop the rumble on.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRumbleSupported
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleStop(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticRumbleSupported(haptic):
    """
    ``int SDL_HapticRumbleSupported(SDL_Haptic *)``
    
    Checks to see if rumble is supported on a haptic device.
    
    :param haptic: Haptic device to check to see if it supports rumble.
    :return: SDL_TRUE if effect is supported, SDL_FALSE if it isn't or -1
        on error.
    
    See also SDL_HapticRumbleInit
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticRumbleSupported(haptic_c)
    return rc

def hapticRunEffect(haptic, effect, iterations):
    """
    ``int SDL_HapticRunEffect(SDL_Haptic *, int, unsigned int)``
    
    Runs the haptic effect on its associated haptic device.
    
    If iterations are SDL_HAPTIC_INFINITY, it'll run the effect over and
    over repeating the envelope (attack and fade) every time. If you only
    want the effect to last forever, set SDL_HAPTIC_INFINITY in the
    effect's length parameter.
    
    :param haptic: Haptic device to run the effect on.
    :param effect: Identifier of the haptic effect to run.
    :param iterations: Number of iterations to run the effect. Use
        SDL_HAPTIC_INFINITY for infinity.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticStopEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    iterations_c = iterations
    rc = lib.SDL_HapticRunEffect(haptic_c, effect_c, iterations_c)
    if rc == -1: raise SDLError()
    return rc

def hapticSetAutocenter(haptic, autocenter):
    """
    ``int SDL_HapticSetAutocenter(SDL_Haptic *, int)``
    
    Sets the global autocenter of the device.
    
    Autocenter should be between 0 and 100. Setting it to 0 will disable
    autocentering.
    
    Device must support the SDL_HAPTIC_AUTOCENTER feature.
    
    :param haptic: Haptic device to set autocentering on.
    :param autocenter: Value to set autocenter to, 0 disables
        autocentering.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    autocenter_c = autocenter
    rc = lib.SDL_HapticSetAutocenter(haptic_c, autocenter_c)
    if rc == -1: raise SDLError()
    return rc

def hapticSetGain(haptic, gain):
    """
    ``int SDL_HapticSetGain(SDL_Haptic *, int)``
    
    Sets the global gain of the device.
    
    Device must support the SDL_HAPTIC_GAIN feature.
    
    The user may specify the maximum gain by setting the environment
    variable SDL_HAPTIC_GAIN_MAX which should be between 0 and 100. All
    calls to SDL_HapticSetGain() will scale linearly using
    SDL_HAPTIC_GAIN_MAX as the maximum.
    
    :param haptic: Haptic device to set the gain on.
    :param gain: Value to set the gain to, should be between 0 and 100.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticQuery
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    gain_c = gain
    rc = lib.SDL_HapticSetGain(haptic_c, gain_c)
    if rc == -1: raise SDLError()
    return rc

def hapticStopAll(haptic):
    """
    ``int SDL_HapticStopAll(SDL_Haptic *)``
    
    Stops all the currently playing effects on a haptic device.
    
    :param haptic: Haptic device to stop.
    :return: 0 on success or -1 on error.
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticStopAll(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticStopEffect(haptic, effect):
    """
    ``int SDL_HapticStopEffect(SDL_Haptic *, int)``
    
    Stops the haptic effect on its associated haptic device.
    
    :param haptic: Haptic device to stop the effect on.
    :param effect: Identifier of the effect to stop.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticRunEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    rc = lib.SDL_HapticStopEffect(haptic_c, effect_c)
    if rc == -1: raise SDLError()
    return rc

def hapticUnpause(haptic):
    """
    ``int SDL_HapticUnpause(SDL_Haptic *)``
    
    Unpauses a haptic device.
    
    Call to unpause after SDL_HapticPause().
    
    :param haptic: Haptic device to pause.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticPause
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    rc = lib.SDL_HapticUnpause(haptic_c)
    if rc == -1: raise SDLError()
    return rc

def hapticUpdateEffect(haptic, effect, data):
    """
    ``int SDL_HapticUpdateEffect(SDL_Haptic *, int, SDL_HapticEffect *)``
    
    Updates the properties of an effect.
    
    Can be used dynamically, although behaviour when dynamically changing
    direction may be strange. Specifically the effect may reupload itself
    and start playing from the start. You cannot change the type either
    when running SDL_HapticUpdateEffect().
    
    :param haptic: Haptic device that has the effect.
    :param effect: Effect to update.
    :param data: New effect properties to use.
    :return: 0 on success or -1 on error.
    
    See also SDL_HapticNewEffect
    """
    haptic_c = unbox(haptic, 'SDL_Haptic *')
    effect_c = effect
    data_c = unbox(data, 'SDL_HapticEffect *')
    rc = lib.SDL_HapticUpdateEffect(haptic_c, effect_c, data_c)
    if rc == -1: raise SDLError()
    return rc

def has3DNow():
    """
    ``SDL_bool SDL_Has3DNow(void)``
    
    This function returns true if the CPU has 3DNow! features.
    """
    rc = lib.SDL_Has3DNow()
    return rc

def hasAVX():
    """
    ``SDL_bool SDL_HasAVX(void)``
    
    This function returns true if the CPU has AVX features.
    """
    rc = lib.SDL_HasAVX()
    return rc

def hasAltiVec():
    """
    ``SDL_bool SDL_HasAltiVec(void)``
    
    This function returns true if the CPU has AltiVec features.
    """
    rc = lib.SDL_HasAltiVec()
    return rc

def hasClipboardText():
    """
    ``SDL_bool SDL_HasClipboardText(void)``
    
    Returns a flag indicating whether the clipboard exists and contains a
    text string that is non-empty.
    
    See also SDL_GetClipboardText()
    """
    rc = lib.SDL_HasClipboardText()
    return rc

def hasEvent(type):
    """
    ``SDL_bool SDL_HasEvent(unsigned int)``
    
    Checks to see if certain event types are in the event queue.
    """
    type_c = type
    rc = lib.SDL_HasEvent(type_c)
    return rc

def hasEvents(minType, maxType):
    """
    ``SDL_bool SDL_HasEvents(unsigned int, unsigned int)``
    """
    minType_c = minType
    maxType_c = maxType
    rc = lib.SDL_HasEvents(minType_c, maxType_c)
    return rc

def hasIntersection(A, B):
    """
    ``SDL_bool SDL_HasIntersection(SDL_Rect const *, SDL_Rect const *)``
    
    Determine whether two rectangles intersect.
    
    :return: SDL_TRUE if there is an intersection, SDL_FALSE otherwise.
    """
    A_c = unbox(A, 'SDL_Rect const *')
    B_c = unbox(B, 'SDL_Rect const *')
    rc = lib.SDL_HasIntersection(A_c, B_c)
    return rc

def hasMMX():
    """
    ``SDL_bool SDL_HasMMX(void)``
    
    This function returns true if the CPU has MMX features.
    """
    rc = lib.SDL_HasMMX()
    return rc

def hasRDTSC():
    """
    ``SDL_bool SDL_HasRDTSC(void)``
    
    This function returns true if the CPU has the RDTSC instruction.
    """
    rc = lib.SDL_HasRDTSC()
    return rc

def hasSSE():
    """
    ``SDL_bool SDL_HasSSE(void)``
    
    This function returns true if the CPU has SSE features.
    """
    rc = lib.SDL_HasSSE()
    return rc

def hasSSE2():
    """
    ``SDL_bool SDL_HasSSE2(void)``
    
    This function returns true if the CPU has SSE2 features.
    """
    rc = lib.SDL_HasSSE2()
    return rc

def hasSSE3():
    """
    ``SDL_bool SDL_HasSSE3(void)``
    
    This function returns true if the CPU has SSE3 features.
    """
    rc = lib.SDL_HasSSE3()
    return rc

def hasSSE41():
    """
    ``SDL_bool SDL_HasSSE41(void)``
    
    This function returns true if the CPU has SSE4.1 features.
    """
    rc = lib.SDL_HasSSE41()
    return rc

def hasSSE42():
    """
    ``SDL_bool SDL_HasSSE42(void)``
    
    This function returns true if the CPU has SSE4.2 features.
    """
    rc = lib.SDL_HasSSE42()
    return rc

def hasScreenKeyboardSupport():
    """
    ``SDL_bool SDL_HasScreenKeyboardSupport(void)``
    
    Returns whether the platform has some screen keyboard support.
    
    :return: SDL_TRUE if some keyboard support is available else
        SDL_FALSE.
    
    Not all screen keyboard functions are supported on all platforms.
    
    See also SDL_IsScreenKeyboardShown()
    """
    rc = lib.SDL_HasScreenKeyboardSupport()
    return rc

def hideWindow(window):
    """
    ``void SDL_HideWindow(SDL_Window *)``
    
    Hide a window.
    
    See also SDL_ShowWindow()
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_HideWindow(window_c)

def init(flags):
    """
    ``int SDL_Init(unsigned int)``
    
    This function initializes the subsystems specified by flags Unless the
    SDL_INIT_NOPARACHUTE flag is set, it will install cleanup signal
    handlers for some commonly ignored fatal signals (like SIGSEGV).
    """
    flags_c = flags
    rc = lib.SDL_Init(flags_c)
    return rc

def initSubSystem(flags):
    """
    ``int SDL_InitSubSystem(unsigned int)``
    
    This function initializes specific SDL subsystems
    """
    flags_c = flags
    rc = lib.SDL_InitSubSystem(flags_c)
    return rc

def intersectRect(A, B, result):
    """
    ``SDL_bool SDL_IntersectRect(SDL_Rect const *, SDL_Rect const *, SDL_Rect *)``
    
    Calculate the intersection of two rectangles.
    
    :return: SDL_TRUE if there is an intersection, SDL_FALSE otherwise.
    """
    A_c = unbox(A, 'SDL_Rect const *')
    B_c = unbox(B, 'SDL_Rect const *')
    result_c = unbox(result, 'SDL_Rect *')
    rc = lib.SDL_IntersectRect(A_c, B_c, result_c)
    return rc

def intersectRectAndLine(rect, X1=None, Y1=None, X2=None, Y2=None):
    """
    ``SDL_bool SDL_IntersectRectAndLine(SDL_Rect const *, int *, int *, int *, int *)``
    
    Calculate the intersection of a rectangle and line segment.
    
    :return: SDL_TRUE if there is an intersection, SDL_FALSE otherwise.
    """
    rect_c = unbox(rect, 'SDL_Rect const *')
    X1_c = unbox(X1, 'int *')
    Y1_c = unbox(Y1, 'int *')
    X2_c = unbox(X2, 'int *')
    Y2_c = unbox(Y2, 'int *')
    rc = lib.SDL_IntersectRectAndLine(rect_c, X1_c, Y1_c, X2_c, Y2_c)
    return (rc, X1_c[0], Y1_c[0], X2_c[0], Y2_c[0])

def isGameController(joystick_index):
    """
    ``SDL_bool SDL_IsGameController(int)``
    
    Is the joystick on this index supported by the game controller
    interface?
    """
    joystick_index_c = joystick_index
    rc = lib.SDL_IsGameController(joystick_index_c)
    return rc

def isScreenKeyboardShown(window):
    """
    ``SDL_bool SDL_IsScreenKeyboardShown(SDL_Window *)``
    
    Returns whether the screen keyboard is shown for given window.
    
    :param window: The window for which screen keyboard should be queried.
    :return: SDL_TRUE if screen keyboard is shown else SDL_FALSE.
    
    See also SDL_HasScreenKeyboardSupport()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_IsScreenKeyboardShown(window_c)
    return rc

def isScreenSaverEnabled():
    """
    ``SDL_bool SDL_IsScreenSaverEnabled(void)``
    
    Returns whether the screensaver is currently enabled (default on).
    
    See also SDL_EnableScreenSaver()
    """
    rc = lib.SDL_IsScreenSaverEnabled()
    return rc

def isTextInputActive():
    """
    ``SDL_bool SDL_IsTextInputActive(void)``
    
    Return whether or not Unicode text input events are enabled.
    
    See also SDL_StartTextInput()
    """
    rc = lib.SDL_IsTextInputActive()
    return rc

def joystickClose(joystick):
    """
    ``void SDL_JoystickClose(SDL_Joystick *)``
    
    Close a joystick previously opened with SDL_JoystickOpen().
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    lib.SDL_JoystickClose(joystick_c)

def joystickEventState(state):
    """
    ``int SDL_JoystickEventState(int)``
    
    Enable/disable joystick event polling.
    
    If joystick events are disabled, you must call SDL_JoystickUpdate()
    yourself and check the state of the joystick when you want joystick
    information.
    
    The state can be one of SDL_QUERY, SDL_ENABLE or SDL_IGNORE.
    """
    state_c = state
    rc = lib.SDL_JoystickEventState(state_c)
    return rc

def joystickGetAttached(joystick):
    """
    ``SDL_bool SDL_JoystickGetAttached(SDL_Joystick *)``
    
    Returns SDL_TRUE if the joystick has been opened and currently
    connected, or SDL_FALSE if it has not.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetAttached(joystick_c)
    return rc

def joystickGetAxis(joystick, axis):
    """
    ``int16_t SDL_JoystickGetAxis(SDL_Joystick *, int)``
    
    Get the current state of an axis control on a joystick.
    
    The state is a value ranging from -32768 to 32767.
    
    The axis indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    axis_c = axis
    rc = lib.SDL_JoystickGetAxis(joystick_c, axis_c)
    return rc

def joystickGetBall(joystick, ball, dx=None, dy=None):
    """
    ``int SDL_JoystickGetBall(SDL_Joystick *, int, int *, int *)``
    
    Get the ball axis change since the last poll.
    
    :return: 0, or -1 if you passed it invalid parameters.
    
    The ball indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    ball_c = ball
    dx_c = unbox(dx, 'int *')
    dy_c = unbox(dy, 'int *')
    rc = lib.SDL_JoystickGetBall(joystick_c, ball_c, dx_c, dy_c)
    return (rc, dx_c[0], dy_c[0])

def joystickGetButton(joystick, button):
    """
    ``unsigned char SDL_JoystickGetButton(SDL_Joystick *, int)``
    
    Get the current state of a button on a joystick.
    
    The button indices start at index 0.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    button_c = button
    rc = lib.SDL_JoystickGetButton(joystick_c, button_c)
    return rc

def joystickGetDeviceGUID(device_index):
    """
    ``SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int)``
    
    Return the GUID for the joystick at this index
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickGetDeviceGUID(device_index_c)
    return JoystickGUID(rc)

def joystickGetGUID(joystick):
    """
    ``SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick *)``
    
    Return the GUID for this opened joystick
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickGetGUID(joystick_c)
    return JoystickGUID(rc)

def joystickGetGUIDFromString(pchGUID):
    """
    ``SDL_JoystickGUID SDL_JoystickGetGUIDFromString(char const *)``
    
    convert a string into a joystick formatted guid
    """
    pchGUID_c = u8(pchGUID)
    rc = lib.SDL_JoystickGetGUIDFromString(pchGUID_c)
    return JoystickGUID(rc)

def joystickGetGUIDString(guid, pszGUID, cbGUID):
    """
    ``void SDL_JoystickGetGUIDString(SDL_JoystickGUID, char *, int)``
    
    Return a string representation for this guid. pszGUID must point to at
    least 33 bytes (32 for the string plus a NULL terminator).
    """
    guid_c = unbox(guid, 'SDL_JoystickGUID')
    pszGUID_c = u8(pszGUID)
    cbGUID_c = cbGUID
    lib.SDL_JoystickGetGUIDString(guid_c, pszGUID_c, cbGUID_c)

def joystickGetHat(joystick, hat):
    """
    ``unsigned char SDL_JoystickGetHat(SDL_Joystick *, int)``
    
    Get the current state of a POV hat on a joystick.
    
    The hat indices start at index 0.
    
    :return: The return value is one of the following positions:
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    hat_c = hat
    rc = lib.SDL_JoystickGetHat(joystick_c, hat_c)
    return rc

def joystickInstanceID(joystick):
    """
    ``int32_t SDL_JoystickInstanceID(SDL_Joystick *)``
    
    Get the instance ID of an opened joystick or -1 if the joystick is
    invalid.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickInstanceID(joystick_c)
    return rc

def joystickIsHaptic(joystick):
    """
    ``int SDL_JoystickIsHaptic(SDL_Joystick *)``
    
    Checks to see if a joystick has haptic features.
    
    :param joystick: Joystick to test for haptic capabilities.
    :return: 1 if the joystick is haptic, 0 if it isn't or -1 if an error
        ocurred.
    
    See also SDL_HapticOpenFromJoystick
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickIsHaptic(joystick_c)
    return rc

def joystickName(joystick):
    """
    ``char const * SDL_JoystickName(SDL_Joystick *)``
    
    Return the name for this currently opened joystick. If no name can be
    found, this function returns NULL.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickName(joystick_c)
    return ffi.string(rc).decode('utf-8')

def joystickNameForIndex(device_index):
    """
    ``char const * SDL_JoystickNameForIndex(int)``
    
    Get the implementation dependent name of a joystick. This can be
    called before any joysticks are opened. If no name can be found, this
    function returns NULL.
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickNameForIndex(device_index_c)
    return ffi.string(rc).decode('utf-8')

def joystickNumAxes(joystick):
    """
    ``int SDL_JoystickNumAxes(SDL_Joystick *)``
    
    Get the number of general axis controls on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumAxes(joystick_c)
    return rc

def joystickNumBalls(joystick):
    """
    ``int SDL_JoystickNumBalls(SDL_Joystick *)``
    
    Get the number of trackballs on a joystick.
    
    Joystick trackballs have only relative motion events associated with
    them and their state cannot be polled.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumBalls(joystick_c)
    return rc

def joystickNumButtons(joystick):
    """
    ``int SDL_JoystickNumButtons(SDL_Joystick *)``
    
    Get the number of buttons on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumButtons(joystick_c)
    return rc

def joystickNumHats(joystick):
    """
    ``int SDL_JoystickNumHats(SDL_Joystick *)``
    
    Get the number of POV hats on a joystick.
    """
    joystick_c = unbox(joystick, 'SDL_Joystick *')
    rc = lib.SDL_JoystickNumHats(joystick_c)
    return rc

def joystickOpen(device_index):
    """
    ``SDL_Joystick * SDL_JoystickOpen(int)``
    
    Open a joystick for use. The index passed as an argument refers tothe
    N'th joystick on the system. This index is the value which will
    identify this joystick in future joystick events.
    
    :return: A joystick identifier, or NULL if an error occurred.
    """
    device_index_c = device_index
    rc = lib.SDL_JoystickOpen(device_index_c)
    if rc == ffi.NULL: raise SDLError()
    return Joystick(rc)

def joystickUpdate():
    """
    ``void SDL_JoystickUpdate(void)``
    
    Update the current state of the open joysticks.
    
    This is called automatically by the event loop if any joystick events
    are enabled.
    """
    lib.SDL_JoystickUpdate()

def loadBMP_RW(src, freesrc):
    """
    ``SDL_Surface * SDL_LoadBMP_RW(SDL_RWops *, int)``
    
    Load a surface from a seekable SDL data stream (memory or file).
    
    If freesrc is non-zero, the stream will be closed after being read.
    
    The new surface should be freed with SDL_FreeSurface().
    
    :return: the new surface, or NULL if there was an error.
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    rc = lib.SDL_LoadBMP_RW(src_c, freesrc_c)
    if rc == ffi.NULL: raise SDLError()
    return Surface(rc)

def loadDollarTemplates(touchId, src):
    """
    ``int SDL_LoadDollarTemplates(int64_t, SDL_RWops *)``
    
    Load Dollar Gesture templates from a file.
    """
    touchId_c = touchId
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_LoadDollarTemplates(touchId_c, src_c)
    return rc

def loadFunction(handle, name):
    """
    ``void * SDL_LoadFunction(void *, char const *)``
    
    Given an object handle, this function looks up the address of the
    named function in the shared object and returns it. This address is no
    longer valid after calling SDL_UnloadObject().
    """
    handle_c = unbox(handle, 'void *')
    name_c = u8(name)
    rc = lib.SDL_LoadFunction(handle_c, name_c)
    return rc

def loadObject(sofile):
    """
    ``void * SDL_LoadObject(char const *)``
    
    This function dynamically loads a shared object and returns a pointer
    to the object handle (or NULL if there was an error). The 'sofile'
    parameter is a system dependent name of the object file.
    """
    sofile_c = u8(sofile)
    rc = lib.SDL_LoadObject(sofile_c)
    if rc == ffi.NULL: raise SDLError()
    return rc

def loadWAV_RW(src, freesrc, spec, audio_buf, audio_len=None):
    """
    ``SDL_AudioSpec * SDL_LoadWAV_RW(SDL_RWops *, int, SDL_AudioSpec *, unsigned char * *, unsigned int *)``
    
    This function loads a WAVE from the data source, automatically freeing
    that source if freesrc is non-zero. For example, to load a WAVE file,
    you could do: ::
    
           SDL_LoadWAV_RW(SDL_RWFromFile("sample.wav", "rb"), 1, ...);
    
    
    If this function succeeds, it returns the given SDL_AudioSpec, filled
    with the audio data format of the wave data, and sets *audio_buf to a
    malloc()'d buffer containing the audio data, and sets *audio_len to
    the length of that audio buffer, in bytes. You need to free the audio
    buffer with SDL_FreeWAV() when you are done with it.
    
    This function returns NULL and sets the SDL error message if the wave
    file cannot be opened, uses an unknown data format, or is corrupt.
    Currently raw and MS-ADPCM WAVE files are supported.
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    spec_c = unbox(spec, 'SDL_AudioSpec *')
    audio_buf_c = unbox(audio_buf, 'unsigned char * *')
    audio_len_c = unbox(audio_len, 'unsigned int *')
    rc = lib.SDL_LoadWAV_RW(src_c, freesrc_c, spec_c, audio_buf_c, audio_len_c)
    if rc == ffi.NULL: raise SDLError()
    return (AudioSpec(rc), audio_len_c[0])

def lockAudio():
    """
    ``void SDL_LockAudio(void)``
    """
    lib.SDL_LockAudio()

def lockAudioDevice(dev):
    """
    ``void SDL_LockAudioDevice(unsigned int)``
    """
    dev_c = dev
    lib.SDL_LockAudioDevice(dev_c)

def lockMutex(mutex):
    """
    ``int SDL_LockMutex(SDL_mutex *)``
    """
    mutex_c = unbox(mutex, 'SDL_mutex *')
    rc = lib.SDL_LockMutex(mutex_c)
    return rc

def lockSurface(surface):
    """
    ``int SDL_LockSurface(SDL_Surface *)``
    
    Sets up a surface for directly accessing the pixels.
    
    Between calls to SDL_LockSurface() / SDL_UnlockSurface(), you can
    write to and read from surface->pixels, using the pixel format stored
    in surface->format. Once you are done accessing the surface, you
    should use SDL_UnlockSurface() to release it.
    
    Not all surfaces require locking. If SDL_MUSTLOCK(surface) evaluates
    to 0, then you can read and write to the surface at any time, and the
    pixel format of the surface will not change.
    
    No operating system or library calls should be made between
    lock/unlock pairs, as critical system locks may be held during this
    time.
    
    SDL_LockSurface() returns 0, or -1 if the surface couldn't be locked.
    
    See also SDL_UnlockSurface()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    rc = lib.SDL_LockSurface(surface_c)
    return rc

def lockTexture(texture, rect, pixels, pitch=None):
    """
    ``int SDL_LockTexture(SDL_Texture *, SDL_Rect const *, void * *, int *)``
    
    Lock a portion of the texture for write-only pixel access.
    
    :param texture: The texture to lock for access, which was created with
        SDL_TEXTUREACCESS_STREAMING.
    :param rect: A pointer to the rectangle to lock for access. If the
        rect is NULL, the entire texture will be locked.
    :param pixels: This is filled in with a pointer to the locked pixels,
        appropriately offset by the locked area.
    :param pitch: This is filled in with the pitch of the locked pixels.
    :return: 0 on success, or -1 if the texture is not valid or was not
        created with
    
    See also SDL_UnlockTexture()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    pixels_c = unbox(pixels, 'void * *')
    pitch_c = unbox(pitch, 'int *')
    rc = lib.SDL_LockTexture(texture_c, rect_c, pixels_c, pitch_c)
    return (rc, pitch_c[0])

def log(fmt):
    """
    ``void SDL_Log(char const *, ...)``
    
    Log a message with SDL_LOG_CATEGORY_APPLICATION and
    SDL_LOG_PRIORITY_INFO.
    """
    fmt_c = u8(fmt)
    lib.SDL_Log(fmt_c)

def logCritical(category, fmt):
    """
    ``void SDL_LogCritical(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_CRITICAL.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogCritical(category_c, fmt_c)

def logDebug(category, fmt):
    """
    ``void SDL_LogDebug(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_DEBUG.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogDebug(category_c, fmt_c)

def logError(category, fmt):
    """
    ``void SDL_LogError(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_ERROR.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogError(category_c, fmt_c)

def logGetOutputFunction(callback, userdata):
    """
    ``void SDL_LogGetOutputFunction(void(* *)(void *, int, SDL_LogPriority, char const *), void * *)``
    
    Get the current log output function.
    """
    callback_c = unbox(callback, 'void(* *)(void *, int, SDL_LogPriority, char const *)')
    userdata_c = unbox(userdata, 'void * *')
    lib.SDL_LogGetOutputFunction(callback_c, userdata_c)

def logGetPriority(category):
    """
    ``SDL_LogPriority SDL_LogGetPriority(int)``
    
    Get the priority of a particular log category.
    """
    category_c = category
    rc = lib.SDL_LogGetPriority(category_c)
    return rc

def logInfo(category, fmt):
    """
    ``void SDL_LogInfo(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_INFO.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogInfo(category_c, fmt_c)

def logMessage(category, priority, fmt):
    """
    ``void SDL_LogMessage(int, SDL_LogPriority, char const *, ...)``
    
    Log a message with the specified category and priority.
    """
    category_c = category
    priority_c = priority
    fmt_c = u8(fmt)
    lib.SDL_LogMessage(category_c, priority_c, fmt_c)

def logResetPriorities():
    """
    ``void SDL_LogResetPriorities(void)``
    
    Reset all priorities to default.
    
    This is called in SDL_Quit().
    """
    lib.SDL_LogResetPriorities()

def logSetAllPriority(priority):
    """
    ``void SDL_LogSetAllPriority(SDL_LogPriority)``
    
    Set the priority of all log categories.
    """
    priority_c = priority
    lib.SDL_LogSetAllPriority(priority_c)

def logSetOutputFunction(callback, userdata):
    """
    ``void SDL_LogSetOutputFunction(void SDL_LogSetOutputFunction(void *, int, SDL_LogPriority, char const *), void *)``
    
    This function allows you to replace the default log output function
    with one of your own.
    """
    callback_c = unbox(callback, 'void(*)(void *, int, SDL_LogPriority, char const *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_LogSetOutputFunction(callback_c, userdata_c)

def logSetPriority(category, priority):
    """
    ``void SDL_LogSetPriority(int, SDL_LogPriority)``
    
    Set the priority of a particular log category.
    """
    category_c = category
    priority_c = priority
    lib.SDL_LogSetPriority(category_c, priority_c)

def logVerbose(category, fmt):
    """
    ``void SDL_LogVerbose(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_VERBOSE.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogVerbose(category_c, fmt_c)

def logWarn(category, fmt):
    """
    ``void SDL_LogWarn(int, char const *, ...)``
    
    Log a message with SDL_LOG_PRIORITY_WARN.
    """
    category_c = category
    fmt_c = u8(fmt)
    lib.SDL_LogWarn(category_c, fmt_c)

def lowerBlit(src, srcrect, dst, dstrect):
    """
    ``int SDL_LowerBlit(SDL_Surface *, SDL_Rect *, SDL_Surface *, SDL_Rect *)``
    
    This is a semi-private blit function and it performs low-level surface
    blitting only.
    """
    src_c = unbox(src, 'SDL_Surface *')
    srcrect_c = unbox(srcrect, 'SDL_Rect *')
    dst_c = unbox(dst, 'SDL_Surface *')
    dstrect_c = unbox(dstrect, 'SDL_Rect *')
    rc = lib.SDL_LowerBlit(src_c, srcrect_c, dst_c, dstrect_c)
    return rc

def lowerBlitScaled(src, srcrect, dst, dstrect):
    """
    ``int SDL_LowerBlitScaled(SDL_Surface *, SDL_Rect *, SDL_Surface *, SDL_Rect *)``
    
    This is a semi-private blit function and it performs low-level surface
    scaled blitting only.
    """
    src_c = unbox(src, 'SDL_Surface *')
    srcrect_c = unbox(srcrect, 'SDL_Rect *')
    dst_c = unbox(dst, 'SDL_Surface *')
    dstrect_c = unbox(dstrect, 'SDL_Rect *')
    rc = lib.SDL_LowerBlitScaled(src_c, srcrect_c, dst_c, dstrect_c)
    return rc

def mapRGB(format, r, g, b):
    """
    ``unsigned int SDL_MapRGB(SDL_PixelFormat const *, unsigned char, unsigned char, unsigned char)``
    
    Maps an RGB triple to an opaque pixel value for a given pixel format.
    
    See also SDL_MapRGBA
    """
    format_c = unbox(format, 'SDL_PixelFormat const *')
    r_c = r
    g_c = g
    b_c = b
    rc = lib.SDL_MapRGB(format_c, r_c, g_c, b_c)
    return rc

def mapRGBA(format, r, g, b, a):
    """
    ``unsigned int SDL_MapRGBA(SDL_PixelFormat const *, unsigned char, unsigned char, unsigned char, unsigned char)``
    
    Maps an RGBA quadruple to a pixel value for a given pixel format.
    
    See also SDL_MapRGB
    """
    format_c = unbox(format, 'SDL_PixelFormat const *')
    r_c = r
    g_c = g
    b_c = b
    a_c = a
    rc = lib.SDL_MapRGBA(format_c, r_c, g_c, b_c, a_c)
    return rc

def masksToPixelFormatEnum(bpp, Rmask, Gmask, Bmask, Amask):
    """
    ``unsigned int SDL_MasksToPixelFormatEnum(int, unsigned int, unsigned int, unsigned int, unsigned int)``
    
    Convert a bpp and RGBA masks to an enumerated pixel format.
    
    :return: The pixel format, or
    
    See also SDL_PixelFormatEnumToMasks()
    """
    bpp_c = bpp
    Rmask_c = Rmask
    Gmask_c = Gmask
    Bmask_c = Bmask
    Amask_c = Amask
    rc = lib.SDL_MasksToPixelFormatEnum(bpp_c, Rmask_c, Gmask_c, Bmask_c, Amask_c)
    return rc

def maximizeWindow(window):
    """
    ``void SDL_MaximizeWindow(SDL_Window *)``
    
    Make a window as large as possible.
    
    See also SDL_RestoreWindow()
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_MaximizeWindow(window_c)

def minimizeWindow(window):
    """
    ``void SDL_MinimizeWindow(SDL_Window *)``
    
    Minimize a window to an iconic representation.
    
    See also SDL_RestoreWindow()
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_MinimizeWindow(window_c)

def mixAudio(dst, src, len, volume):
    """
    ``void SDL_MixAudio(unsigned char *, unsigned char const *, unsigned int, int)``
    
    This takes two audio buffers of the playing audio format and mixes
    them, performing addition, volume adjustment, and overflow clipping.
    The volume ranges from 0 - 128, and should be set to SDL_MIX_MAXVOLUME
    for full audio volume. Note this does not change hardware volume. This
    is provided for convenience  you can mix your own audio data.
    """
    dst_c = unbox(dst, 'unsigned char *')
    src_c = unbox(src, 'unsigned char const *')
    len_c = len
    volume_c = volume
    lib.SDL_MixAudio(dst_c, src_c, len_c, volume_c)

def mixAudioFormat(dst, src, format, len, volume):
    """
    ``void SDL_MixAudioFormat(unsigned char *, unsigned char const *, unsigned short, unsigned int, int)``
    
    This works like SDL_MixAudio(), but you specify the audio format
    instead of using the format of audio device 1. Thus it can be used
    when no audio device is open at all.
    """
    dst_c = unbox(dst, 'unsigned char *')
    src_c = unbox(src, 'unsigned char const *')
    format_c = format
    len_c = len
    volume_c = volume
    lib.SDL_MixAudioFormat(dst_c, src_c, format_c, len_c, volume_c)

def mouseIsHaptic():
    """
    ``int SDL_MouseIsHaptic(void)``
    
    Gets whether or not the current mouse has haptic capabilities.
    
    :return: SDL_TRUE if the mouse is haptic, SDL_FALSE if it isn't.
    
    See also SDL_HapticOpenFromMouse
    """
    rc = lib.SDL_MouseIsHaptic()
    return rc

def numHaptics():
    """
    ``int SDL_NumHaptics(void)``
    
    Count the number of haptic devices attached to the system.
    
    :return: Number of haptic devices detected on the system.
    """
    rc = lib.SDL_NumHaptics()
    return rc

def numJoysticks():
    """
    ``int SDL_NumJoysticks(void)``
    
    Count the number of joysticks attached to the system right now
    """
    rc = lib.SDL_NumJoysticks()
    return rc

def openAudio(desired, obtained):
    """
    ``int SDL_OpenAudio(SDL_AudioSpec *, SDL_AudioSpec *)``
    
    This function opens the audio device with the desired parameters, and
    returns 0 if successful, placing the actual hardware parameters in the
    structure pointed to by obtained. If obtained is NULL, the audio data
    passed to the callback function will be guaranteed to be in the
    requested format, and will be automatically converted to the hardware
    audio format if necessary. This function returns -1 if it failed to
    open the audio device, or couldn't set up the audio thread.
    
    When filling in the desired audio spec structure,desired->freq should
    be the desired audio frequency in samples-per- second.
    
    desired->format should be the desired audio format.
    
    desired->samples is the desired size of the audio buffer, in samples.
    This number should be a power of two, and may be adjusted by the audio
    driver to a value more suitable for the hardware. Good values seem to
    range between 512 and 8096 inclusive, depending on the application and
    CPU speed. Smaller values yield faster response time, but can lead to
    underflow if the application is doing heavy processing and cannot fill
    the audio buffer in time. A stereo sample consists of both right and
    left channels in LR ordering. Note that the number of samples is
    directly related to time by the following formula:::
    
    ms = (samples*1000)/freq
    
    desired->size is the size in bytes of the audio buffer, and is
    calculated by SDL_OpenAudio().
    
    desired->silence is the value used to set the buffer to silence, and
    is calculated by SDL_OpenAudio().
    
    desired->callback should be set to a function that will be called when
    the audio device is ready for more data. It is passed a pointer to the
    audio buffer, and the length in bytes of the audio buffer. This
    function usually runs in a separate thread, and so you should protect
    data structures that it accesses by calling SDL_LockAudio() and
    SDL_UnlockAudio() in your code.
    
    desired->userdata is passed as the first parameter to your callback
    function.
    
    The audio device starts out playing silence when it's opened, and
    should be enabled for playing by calling SDL_PauseAudio(0) when you
    are ready for your audio callback function to be called. Since the
    audio driver may modify the requested size of the audio buffer, you
    should allocate any local mixing buffers after you open the audio
    device.
    """
    desired_c = unbox(desired, 'SDL_AudioSpec *')
    obtained_c = unbox(obtained, 'SDL_AudioSpec *')
    rc = lib.SDL_OpenAudio(desired_c, obtained_c)
    return rc

def openAudioDevice(device, iscapture, desired, obtained, allowed_changes):
    """
    ``unsigned int SDL_OpenAudioDevice(char const *, int, SDL_AudioSpec const *, SDL_AudioSpec *, int)``
    
    Open a specific audio device. Passing in a device name of NULL
    requests the most reasonable default (and is equivalent to calling
    SDL_OpenAudio()).
    
    The device name is a UTF-8 string reported by
    SDL_GetAudioDeviceName(), but some drivers allow arbitrary and driver-
    specific strings, such as a hostname/IP address for a remote audio
    server, or a filename in the diskaudio driver.
    
    :return: 0 on error, a valid device ID that is >= 2 on success.
    
    SDL_OpenAudio(), unlike this function, always acts on device ID 1.
    """
    device_c = u8(device)
    iscapture_c = iscapture
    desired_c = unbox(desired, 'SDL_AudioSpec const *')
    obtained_c = unbox(obtained, 'SDL_AudioSpec *')
    allowed_changes_c = allowed_changes
    rc = lib.SDL_OpenAudioDevice(device_c, iscapture_c, desired_c, obtained_c, allowed_changes_c)
    if rc == 0: raise SDLError()
    return rc

def pauseAudio(pause_on):
    """
    ``void SDL_PauseAudio(int)``
    """
    pause_on_c = pause_on
    lib.SDL_PauseAudio(pause_on_c)

def pauseAudioDevice(dev, pause_on):
    """
    ``void SDL_PauseAudioDevice(unsigned int, int)``
    """
    dev_c = dev
    pause_on_c = pause_on
    lib.SDL_PauseAudioDevice(dev_c, pause_on_c)

def peepEvents(events, numevents, action, minType, maxType):
    """
    ``int SDL_PeepEvents(SDL_Event *, int, SDL_eventaction, unsigned int, unsigned int)``
    
    Checks the event queue for messages and optionally returns them.
    
    If action is SDL_ADDEVENT, up to numevents events will be added to the
    back of the event queue.
    
    If action is SDL_PEEKEVENT, up to numevents events at the front of the
    event queue, within the specified minimum and maximum type, will be
    returned and will not be removed from the queue.
    
    If action is SDL_GETEVENT, up to numevents events at the front of the
    event queue, within the specified minimum and maximum type, will be
    returned and will be removed from the queue.
    
    :return: The number of events actually stored, or -1 if there was an
        error.
    
    This function is thread-safe.
    """
    events_c = unbox(events, 'SDL_Event *')
    numevents_c = numevents
    action_c = action
    minType_c = minType
    maxType_c = maxType
    rc = lib.SDL_PeepEvents(events_c, numevents_c, action_c, minType_c, maxType_c)
    return rc

def pixelFormatEnumToMasks(format, bpp=None, Rmask=None, Gmask=None, Bmask=None, Amask=None):
    """
    ``SDL_bool SDL_PixelFormatEnumToMasks(unsigned int, int *, unsigned int *, unsigned int *, unsigned int *, unsigned int *)``
    
    Convert one of the enumerated pixel formats to a bpp and RGBA masks.
    
    :return: SDL_TRUE, or SDL_FALSE if the conversion wasn't possible.
    
    See also SDL_MasksToPixelFormatEnum()
    """
    format_c = format
    bpp_c = unbox(bpp, 'int *')
    Rmask_c = unbox(Rmask, 'unsigned int *')
    Gmask_c = unbox(Gmask, 'unsigned int *')
    Bmask_c = unbox(Bmask, 'unsigned int *')
    Amask_c = unbox(Amask, 'unsigned int *')
    rc = lib.SDL_PixelFormatEnumToMasks(format_c, bpp_c, Rmask_c, Gmask_c, Bmask_c, Amask_c)
    return (rc, bpp_c[0], Rmask_c[0], Gmask_c[0], Bmask_c[0], Amask_c[0])

def pollEvent(event):
    """
    ``int SDL_PollEvent(SDL_Event *)``
    
    Polls for currently pending events.
    
    :return: 1 if there are any pending events, or 0 if there are none
        available.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_PollEvent(event_c)
    return rc

def pumpEvents():
    """
    ``void SDL_PumpEvents(void)``
    
    Pumps the event loop, gathering events from the input devices.
    
    This function updates the event queue and internal input device state.
    
    This should only be run in the thread that sets the video mode.
    """
    lib.SDL_PumpEvents()

def pushEvent(event):
    """
    ``int SDL_PushEvent(SDL_Event *)``
    
    Add an event to the event queue.
    
    :return: 1 on success, 0 if the event was filtered, or -1 if the event
        queue was full or there was some other error.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_PushEvent(event_c)
    return rc

def queryTexture(texture, format=None, access=None, w=None, h=None):
    """
    ``int SDL_QueryTexture(SDL_Texture *, unsigned int *, int *, int *, int *)``
    
    Query the attributes of a texture.
    
    :param texture: A texture to be queried.
    :param format: A pointer filled in with the raw format of the texture.
        The actual format may differ, but pixel transfers will use this
        format.
    :param access: A pointer filled in with the actual access to the
        texture.
    :param w: A pointer filled in with the width of the texture in pixels.
    :param h: A pointer filled in with the height of the texture in
        pixels.
    :return: 0 on success, or -1 if the texture is not valid.
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    format_c = unbox(format, 'unsigned int *')
    access_c = unbox(access, 'int *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    rc = lib.SDL_QueryTexture(texture_c, format_c, access_c, w_c, h_c)
    return (rc, format_c[0], access_c[0], w_c[0], h_c[0])

def quit():
    """
    ``void SDL_Quit(void)``
    
    This function cleans up all initialized subsystems. You should call it
    upon all exit conditions.
    """
    lib.SDL_Quit()

def quitSubSystem(flags):
    """
    ``void SDL_QuitSubSystem(unsigned int)``
    
    This function cleans up specific SDL subsystems
    """
    flags_c = flags
    lib.SDL_QuitSubSystem(flags_c)

def RWFromConstMem(mem, size):
    """
    ``SDL_RWops * SDL_RWFromConstMem(void const *, int)``
    """
    mem_c = unbox(mem, 'void const *')
    size_c = size
    rc = lib.SDL_RWFromConstMem(mem_c, size_c)
    if rc == ffi.NULL: raise SDLError()
    return RWops(rc)

def RWFromFP(fp, autoclose):
    """
    ``SDL_RWops * SDL_RWFromFP(FILE *, SDL_bool)``
    """
    fp_c = unbox(fp, 'FILE *')
    autoclose_c = autoclose
    rc = lib.SDL_RWFromFP(fp_c, autoclose_c)
    if rc == ffi.NULL: raise SDLError()
    return RWops(rc)

def RWFromFile(file, mode):
    """
    ``SDL_RWops * SDL_RWFromFile(char const *, char const *)``
    """
    file_c = u8(file)
    mode_c = u8(mode)
    rc = lib.SDL_RWFromFile(file_c, mode_c)
    if rc == ffi.NULL: raise SDLError()
    return RWops(rc)

def RWFromMem(mem, size):
    """
    ``SDL_RWops * SDL_RWFromMem(void *, int)``
    """
    mem_c = unbox(mem, 'void *')
    size_c = size
    rc = lib.SDL_RWFromMem(mem_c, size_c)
    if rc == ffi.NULL: raise SDLError()
    return RWops(rc)

def raiseWindow(window):
    """
    ``void SDL_RaiseWindow(SDL_Window *)``
    
    Raise a window above other windows and set the input focus.
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_RaiseWindow(window_c)

def readBE16(src):
    """
    ``unsigned short SDL_ReadBE16(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadBE16(src_c)
    return rc

def readBE32(src):
    """
    ``unsigned int SDL_ReadBE32(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadBE32(src_c)
    return rc

def readBE64(src):
    """
    ``unsigned long SDL_ReadBE64(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadBE64(src_c)
    return rc

def readLE16(src):
    """
    ``unsigned short SDL_ReadLE16(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadLE16(src_c)
    return rc

def readLE32(src):
    """
    ``unsigned int SDL_ReadLE32(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadLE32(src_c)
    return rc

def readLE64(src):
    """
    ``unsigned long SDL_ReadLE64(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadLE64(src_c)
    return rc

def readU8(src):
    """
    ``unsigned char SDL_ReadU8(SDL_RWops *)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    rc = lib.SDL_ReadU8(src_c)
    return rc

def recordGesture(touchId):
    """
    ``int SDL_RecordGesture(int64_t)``
    
    Begin Recording a gesture on the specified touch, or all touches (-1)
    """
    touchId_c = touchId
    rc = lib.SDL_RecordGesture(touchId_c)
    return rc

def rectEmpty(r):
    """
    ``SDL_bool SDL_RectEmpty(SDL_Rect const *)``
    
    Returns true if the rectangle has no area.
    """
    r_c = unbox(r, 'SDL_Rect const *')
    rc = lib.SDL_RectEmpty(r_c)
    return rc

def rectEquals(a, b):
    """
    ``SDL_bool SDL_RectEquals(SDL_Rect const *, SDL_Rect const *)``
    
    Returns true if the two rectangles are equal.
    """
    a_c = unbox(a, 'SDL_Rect const *')
    b_c = unbox(b, 'SDL_Rect const *')
    rc = lib.SDL_RectEquals(a_c, b_c)
    return rc

def registerEvents(numevents):
    """
    ``unsigned int SDL_RegisterEvents(int)``
    
    This function allocates a set of user-defined events, and returns the
    beginning event number for that set of events.
    
    If there aren't enough user-defined events left, this function returns
    (Uint32)-1
    """
    numevents_c = numevents
    rc = lib.SDL_RegisterEvents(numevents_c)
    return rc

def removeTimer(id):
    """
    ``SDL_bool SDL_RemoveTimer(int)``
    
    Remove a timer knowing its ID.
    
    :return: A boolean value indicating success or failure.
    
    It is not safe to remove a timer multiple times.
    """
    id_c = id
    rc = lib.SDL_RemoveTimer(id_c)
    return rc

def renderClear(renderer):
    """
    ``int SDL_RenderClear(SDL_Renderer *)``
    
    Clear the current rendering target with the drawing color.
    
    This function clears the entire rendering target, ignoring the
    viewport.
    
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rc = lib.SDL_RenderClear(renderer_c)
    if rc == -1: raise SDLError()
    return rc

def renderCopy(renderer, texture, srcrect, dstrect):
    """
    ``int SDL_RenderCopy(SDL_Renderer *, SDL_Texture *, SDL_Rect const *, SDL_Rect const *)``
    
    Copy a portion of the texture to the current rendering target.
    
    :param renderer: The renderer which should copy parts of a texture.
    :param texture: The source texture.
    :param srcrect: A pointer to the source rectangle, or NULL for the
        entire texture.
    :param dstrect: A pointer to the destination rectangle, or NULL for
        the entire rendering target.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    texture_c = unbox(texture, 'SDL_Texture *')
    srcrect_c = unbox(srcrect, 'SDL_Rect const *', nullable=True)
    dstrect_c = unbox(dstrect, 'SDL_Rect const *', nullable=True)
    rc = lib.SDL_RenderCopy(renderer_c, texture_c, srcrect_c, dstrect_c)
    if rc == -1: raise SDLError()
    return rc

def renderCopyEx(renderer, texture, srcrect, dstrect, angle, center, flip):
    """
    ``int SDL_RenderCopyEx(SDL_Renderer *, SDL_Texture *, SDL_Rect const *, SDL_Rect const *, double, SDL_Point const *, SDL_RendererFlip)``
    
    Copy a portion of the source texture to the current rendering target,
    rotating it by angle around the given center.
    
    :param renderer: The renderer which should copy parts of a texture.
    :param texture: The source texture.
    :param srcrect: A pointer to the source rectangle, or NULL for the
        entire texture.
    :param dstrect: A pointer to the destination rectangle, or NULL for
        the entire rendering target.
    :param angle: An angle in degrees that indicates the rotation that
        will be applied to dstrect
    :param center: A pointer to a point indicating the point around which
        dstrect will be rotated (if NULL, rotation will be done aroud
        dstrect.w/2, dstrect.h/2)
    :param flip: An SDL_RendererFlip value stating which flipping actions
        should be performed on the texture
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    texture_c = unbox(texture, 'SDL_Texture *')
    srcrect_c = unbox(srcrect, 'SDL_Rect const *', nullable=True)
    dstrect_c = unbox(dstrect, 'SDL_Rect const *', nullable=True)
    angle_c = angle
    center_c = unbox(center, 'SDL_Point const *', nullable=True)
    flip_c = flip
    rc = lib.SDL_RenderCopyEx(renderer_c, texture_c, srcrect_c, dstrect_c, angle_c, center_c, flip_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawLine(renderer, x1, y1, x2, y2):
    """
    ``int SDL_RenderDrawLine(SDL_Renderer *, int, int, int, int)``
    
    Draw a line on the current rendering target.
    
    :param renderer: The renderer which should draw a line.
    :param x1: The x coordinate of the start point.
    :param y1: The y coordinate of the start point.
    :param x2: The x coordinate of the end point.
    :param y2: The y coordinate of the end point.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    x1_c = x1
    y1_c = y1
    x2_c = x2
    y2_c = y2
    rc = lib.SDL_RenderDrawLine(renderer_c, x1_c, y1_c, x2_c, y2_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawLines(renderer, points, count):
    """
    ``int SDL_RenderDrawLines(SDL_Renderer *, SDL_Point const *, int)``
    
    Draw a series of connected lines on the current rendering target.
    
    :param renderer: The renderer which should draw multiple lines.
    :param points: The points along the lines
    :param count: The number of points, drawing count-1 lines
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    points_c = unbox(points, 'SDL_Point const *')
    count_c = count
    rc = lib.SDL_RenderDrawLines(renderer_c, points_c, count_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawPoint(renderer, x, y):
    """
    ``int SDL_RenderDrawPoint(SDL_Renderer *, int, int)``
    
    Draw a point on the current rendering target.
    
    :param renderer: The renderer which should draw a point.
    :param x: The x coordinate of the point.
    :param y: The y coordinate of the point.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    x_c = x
    y_c = y
    rc = lib.SDL_RenderDrawPoint(renderer_c, x_c, y_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawPoints(renderer, points, count):
    """
    ``int SDL_RenderDrawPoints(SDL_Renderer *, SDL_Point const *, int)``
    
    Draw multiple points on the current rendering target.
    
    :param renderer: The renderer which should draw multiple points.
    :param points: The points to draw
    :param count: The number of points to draw
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    points_c = unbox(points, 'SDL_Point const *')
    count_c = count
    rc = lib.SDL_RenderDrawPoints(renderer_c, points_c, count_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawRect(renderer, rect):
    """
    ``int SDL_RenderDrawRect(SDL_Renderer *, SDL_Rect const *)``
    
    Draw a rectangle on the current rendering target.
    
    :param renderer: The renderer which should draw a rectangle.
    :param rect: A pointer to the destination rectangle, or NULL to
        outline the entire rendering target.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect const *', nullable=True)
    rc = lib.SDL_RenderDrawRect(renderer_c, rect_c)
    if rc == -1: raise SDLError()
    return rc

def renderDrawRects(renderer, rects, count):
    """
    ``int SDL_RenderDrawRects(SDL_Renderer *, SDL_Rect const *, int)``
    
    Draw some number of rectangles on the current rendering target.
    
    :param renderer: The renderer which should draw multiple rectangles.
    :param rects: A pointer to an array of destination rectangles.
    :param count: The number of rectangles.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rects_c = unbox(rects, 'SDL_Rect const *')
    count_c = count
    rc = lib.SDL_RenderDrawRects(renderer_c, rects_c, count_c)
    if rc == -1: raise SDLError()
    return rc

def renderFillRect(renderer, rect):
    """
    ``int SDL_RenderFillRect(SDL_Renderer *, SDL_Rect const *)``
    
    Fill a rectangle on the current rendering target with the drawing
    color.
    
    :param renderer: The renderer which should fill a rectangle.
    :param rect: A pointer to the destination rectangle, or NULL for the
        entire rendering target.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect const *', nullable=True)
    rc = lib.SDL_RenderFillRect(renderer_c, rect_c)
    if rc == -1: raise SDLError()
    return rc

def renderFillRects(renderer, rects, count):
    """
    ``int SDL_RenderFillRects(SDL_Renderer *, SDL_Rect const *, int)``
    
    Fill some number of rectangles on the current rendering target with
    the drawing color.
    
    :param renderer: The renderer which should fill multiple rectangles.
    :param rects: A pointer to an array of destination rectangles.
    :param count: The number of rectangles.
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rects_c = unbox(rects, 'SDL_Rect const *')
    count_c = count
    rc = lib.SDL_RenderFillRects(renderer_c, rects_c, count_c)
    if rc == -1: raise SDLError()
    return rc

def renderGetClipRect(renderer, rect):
    """
    ``void SDL_RenderGetClipRect(SDL_Renderer *, SDL_Rect *)``
    
    Get the clip rectangle for the current target.
    
    :param renderer: The renderer from which clip rectangle should be
        queried.
    :param rect: A pointer filled in with the current clip rectangle, or
        an empty rectangle if clipping is disabled.
    
    See also SDL_RenderSetClipRect()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect *')
    lib.SDL_RenderGetClipRect(renderer_c, rect_c)

def renderGetLogicalSize(renderer, w=None, h=None):
    """
    ``void SDL_RenderGetLogicalSize(SDL_Renderer *, int *, int *)``
    
    Get device independent resolution for rendering.
    
    :param renderer: The renderer from which resolution should be queried.
    :param w: A pointer filled with the width of the logical resolution
    :param h: A pointer filled with the height of the logical resolution
    
    See also SDL_RenderSetLogicalSize()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    lib.SDL_RenderGetLogicalSize(renderer_c, w_c, h_c)
    return (w_c[0], h_c[0])

def renderGetScale(renderer, scaleX=None, scaleY=None):
    """
    ``void SDL_RenderGetScale(SDL_Renderer *, float *, float *)``
    
    Get the drawing scale for the current target.
    
    :param renderer: The renderer from which drawing scale should be
        queried.
    :param scaleX: A pointer filled in with the horizontal scaling factor
    :param scaleY: A pointer filled in with the vertical scaling factor
    
    See also SDL_RenderSetScale()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    scaleX_c = unbox(scaleX, 'float *')
    scaleY_c = unbox(scaleY, 'float *')
    lib.SDL_RenderGetScale(renderer_c, scaleX_c, scaleY_c)
    return (scaleX_c[0], scaleY_c[0])

def renderGetViewport(renderer, rect):
    """
    ``void SDL_RenderGetViewport(SDL_Renderer *, SDL_Rect *)``
    
    Get the drawing area for the current target.
    
    See also SDL_RenderSetViewport()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect *')
    lib.SDL_RenderGetViewport(renderer_c, rect_c)

def renderPresent(renderer):
    """
    ``void SDL_RenderPresent(SDL_Renderer *)``
    
    Update the screen with rendering performed.
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    lib.SDL_RenderPresent(renderer_c)

def renderReadPixels(renderer, rect, format, pixels, pitch):
    """
    ``int SDL_RenderReadPixels(SDL_Renderer *, SDL_Rect const *, unsigned int, void *, int)``
    
    Read pixels from the current rendering target.
    
    :param renderer: The renderer from which pixels should be read.
    :param rect: A pointer to the rectangle to read, or NULL for the
        entire render target.
    :param format: The desired format of the pixel data, or 0 to use the
        format of the rendering target
    :param pixels: A pointer to be filled in with the pixel data
    :param pitch: The pitch of the pixels parameter.
    :return: 0 on success, or -1 if pixel reading is not supported.
    
    This is a very slow operation, and should not be used frequently.
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect const *', nullable=True)
    format_c = format
    pixels_c = unbox(pixels, 'void *')
    pitch_c = pitch
    rc = lib.SDL_RenderReadPixels(renderer_c, rect_c, format_c, pixels_c, pitch_c)
    return rc

def renderSetClipRect(renderer, rect):
    """
    ``int SDL_RenderSetClipRect(SDL_Renderer *, SDL_Rect const *)``
    
    Set the clip rectangle for the current target.
    
    :param renderer: The renderer for which clip rectangle should be set.
    :param rect: A pointer to the rectangle to set as the clip rectangle,
        or NULL to disable clipping.
    :return: 0 on success, or -1 on error
    
    See also SDL_RenderGetClipRect()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect const *', nullable=True)
    rc = lib.SDL_RenderSetClipRect(renderer_c, rect_c)
    if rc == -1: raise SDLError()
    return rc

def renderSetLogicalSize(renderer, w, h):
    """
    ``int SDL_RenderSetLogicalSize(SDL_Renderer *, int, int)``
    
    Set device independent resolution for rendering.
    
    :param renderer: The renderer for which resolution should be set.
    :param w: The width of the logical resolution
    :param h: The height of the logical resolution
    
    This function uses the viewport and scaling functionality to allow a
    fixed logical resolution for rendering, regardless of the actual
    output resolution. If the actual output resolution doesn't have the
    same aspect ratio the output rendering will be centered within the
    output display.
    
    If the output display is a window, mouse events in the window will be
    filtered and scaled so they seem to arrive within the logical
    resolution.
    
    If this function results in scaling or subpixel drawing by the
    rendering backend, it will be handled using the appropriate quality
    hints.
    
    See also SDL_RenderGetLogicalSize()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    w_c = w
    h_c = h
    rc = lib.SDL_RenderSetLogicalSize(renderer_c, w_c, h_c)
    return rc

def renderSetScale(renderer, scaleX, scaleY):
    """
    ``int SDL_RenderSetScale(SDL_Renderer *, float, float)``
    
    Set the drawing scale for rendering on the current target.
    
    :param renderer: The renderer for which the drawing scale should be
        set.
    :param scaleX: The horizontal scaling factor
    :param scaleY: The vertical scaling factor
    
    The drawing coordinates are scaled by the x/y scaling factors before
    they are used by the renderer. This allows resolution independent
    drawing with a single coordinate system.
    
    If this results in scaling or subpixel drawing by the rendering
    backend, it will be handled using the appropriate quality hints. For
    best results use integer scaling factors.
    
    See also SDL_RenderGetScale()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    scaleX_c = scaleX
    scaleY_c = scaleY
    rc = lib.SDL_RenderSetScale(renderer_c, scaleX_c, scaleY_c)
    return rc

def renderSetViewport(renderer, rect):
    """
    ``int SDL_RenderSetViewport(SDL_Renderer *, SDL_Rect const *)``
    
    Set the drawing area for rendering on the current target.
    
    :param renderer: The renderer for which the drawing area should be
        set.
    :param rect: The rectangle representing the drawing area, or NULL to
        set the viewport to the entire target.
    
    The x,y of the viewport rect represents the origin for rendering.
    
    :return: 0 on success, or -1 on error
    
    If the window associated with the renderer is resized, the viewport is
    automatically reset.
    
    See also SDL_RenderGetViewport()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    rc = lib.SDL_RenderSetViewport(renderer_c, rect_c)
    if rc == -1: raise SDLError()
    return rc

def renderTargetSupported(renderer):
    """
    ``SDL_bool SDL_RenderTargetSupported(SDL_Renderer *)``
    
    Determines whether a window supports the use of render targets.
    
    :param renderer: The renderer that will be checked
    :return: SDL_TRUE if supported, SDL_FALSE if not.
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    rc = lib.SDL_RenderTargetSupported(renderer_c)
    return rc

def reportAssertion():
    """
    ``SDL_assert_state SDL_ReportAssertion(SDL_assert_data *, char const *, char const *, int)``
    """
    rc = lib.SDL_ReportAssertion()
    return rc

def resetAssertionReport():
    """
    ``void SDL_ResetAssertionReport(void)``
    
    Reset the list of all assertion failures.
    
    Reset list of all assertions triggered.
    
    See also SDL_GetAssertionReport
    """
    lib.SDL_ResetAssertionReport()

def restoreWindow(window):
    """
    ``void SDL_RestoreWindow(SDL_Window *)``
    
    Restore the size and position of a minimized or maximized window.
    
    See also SDL_MaximizeWindow()
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_RestoreWindow(window_c)

def saveAllDollarTemplates(dst):
    """
    ``int SDL_SaveAllDollarTemplates(SDL_RWops *)``
    
    Save all currently loaded Dollar Gesture templates.
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    rc = lib.SDL_SaveAllDollarTemplates(dst_c)
    return rc

def saveBMP_RW(surface, dst, freedst):
    """
    ``int SDL_SaveBMP_RW(SDL_Surface *, SDL_RWops *, int)``
    
    Save a surface to a seekable SDL data stream (memory or file).
    
    If freedst is non-zero, the stream will be closed after being written.
    
    :return: 0 if successful or -1 if there was an error.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    dst_c = unbox(dst, 'SDL_RWops *')
    freedst_c = freedst
    rc = lib.SDL_SaveBMP_RW(surface_c, dst_c, freedst_c)
    return rc

def saveDollarTemplate(gestureId, dst):
    """
    ``int SDL_SaveDollarTemplate(int64_t, SDL_RWops *)``
    
    Save a currently loaded Dollar Gesture template.
    """
    gestureId_c = gestureId
    dst_c = unbox(dst, 'SDL_RWops *')
    rc = lib.SDL_SaveDollarTemplate(gestureId_c, dst_c)
    return rc

def semPost(sem):
    """
    ``int SDL_SemPost(SDL_sem *)``
    
    Atomically increases the semaphore's count (not blocking).
    
    :return: 0, or -1 on error.
    """
    sem_c = unbox(sem, 'SDL_sem *')
    rc = lib.SDL_SemPost(sem_c)
    if rc == -1: raise SDLError()
    return rc

def semTryWait(sem):
    """
    ``int SDL_SemTryWait(SDL_sem *)``
    
    Non-blocking variant of SDL_SemWait().
    
    :return: 0 if the wait succeeds,
    """
    sem_c = unbox(sem, 'SDL_sem *')
    rc = lib.SDL_SemTryWait(sem_c)
    return rc

def semValue(sem):
    """
    ``unsigned int SDL_SemValue(SDL_sem *)``
    
    Returns the current count of the semaphore.
    """
    sem_c = unbox(sem, 'SDL_sem *')
    rc = lib.SDL_SemValue(sem_c)
    return rc

def semWait(sem):
    """
    ``int SDL_SemWait(SDL_sem *)``
    
    This function suspends the calling thread until the semaphore pointed
    to by sem has a positive count. It then atomically decreases the
    semaphore count.
    """
    sem_c = unbox(sem, 'SDL_sem *')
    rc = lib.SDL_SemWait(sem_c)
    return rc

def semWaitTimeout(sem, ms):
    """
    ``int SDL_SemWaitTimeout(SDL_sem *, unsigned int)``
    
    Variant of SDL_SemWait() with a timeout in milliseconds.
    
    :return: 0 if the wait succeeds,
    
    On some platforms this function is implemented by looping with a delay
    of 1 ms, and so should be avoided if possible.
    """
    sem_c = unbox(sem, 'SDL_sem *')
    ms_c = ms
    rc = lib.SDL_SemWaitTimeout(sem_c, ms_c)
    return rc

def setAssertionHandler(handler, userdata):
    """
    ``void SDL_SetAssertionHandler(SDL_assert_state SDL_SetAssertionHandler(SDL_assert_data const *, void *), void *)``
    
    Set an application-defined assertion handler.
    
    This allows an app to show its own assertion UI and/or force the
    response to an assertion failure. If the app doesn't provide this, SDL
    will try to do the right thing, popping up a system-specific GUI
    dialog, and probably minimizing any fullscreen windows.
    
    This callback may fire from any thread, but it runs wrapped in a
    mutex, so it will only fire from one thread at a time.
    
    Setting the callback to NULL restores SDL's original internal handler.
    
    This callback is NOT reset to SDL's internal handler upon SDL_Quit()!
    
    :return: SDL_assert_state value of how to handle the assertion
        failure.
    :param handler: Callback function, called when an assertion fails.
    :param userdata: A pointer passed to the callback as-is.
    """
    handler_c = unbox(handler, 'SDL_assert_state(*)(SDL_assert_data const *, void *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_SetAssertionHandler(handler_c, userdata_c)

def setClipRect(surface, rect):
    """
    ``SDL_bool SDL_SetClipRect(SDL_Surface *, SDL_Rect const *)``
    
    Sets the clipping rectangle for the destination surface in a blit.
    
    If the clip rectangle is NULL, clipping will be disabled.
    
    If the clip rectangle doesn't intersect the surface, the function will
    return SDL_FALSE and blits will be completely clipped. Otherwise the
    function returns SDL_TRUE and blits to the surface will be clipped to
    the intersection of the surface area and the clipping rectangle.
    
    Note that blits are automatically clipped to the edges of the source
    and destination surfaces.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    rc = lib.SDL_SetClipRect(surface_c, rect_c)
    return rc

def setClipboardText(text):
    """
    ``int SDL_SetClipboardText(char const *)``
    
    Put UTF-8 text into the clipboard.
    
    See also SDL_GetClipboardText()
    """
    text_c = u8(text)
    rc = lib.SDL_SetClipboardText(text_c)
    return rc

def setColorKey(surface, flag, key):
    """
    ``int SDL_SetColorKey(SDL_Surface *, int, unsigned int)``
    
    Sets the color key (transparent pixel) in a blittable surface.
    
    :param surface: The surface to update
    :param flag: Non-zero to enable colorkey and 0 to disable colorkey
    :param key: The transparent pixel in the native surface format
    :return: 0 on success, or -1 if the surface is not valid
    
    You can pass SDL_RLEACCEL to enable RLE accelerated blits.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    flag_c = flag
    key_c = key
    rc = lib.SDL_SetColorKey(surface_c, flag_c, key_c)
    return rc

def setCursor(cursor):
    """
    ``void SDL_SetCursor(SDL_Cursor *)``
    
    Set the active cursor.
    """
    cursor_c = unbox(cursor, 'SDL_Cursor *')
    lib.SDL_SetCursor(cursor_c)

def setError(fmt):
    """
    ``int SDL_SetError(char const *, ...)``
    """
    fmt_c = u8(fmt)
    rc = lib.SDL_SetError(fmt_c)
    return rc

def setEventFilter(filter, userdata):
    """
    ``void SDL_SetEventFilter(int SDL_SetEventFilter(void *, SDL_Event *), void *)``
    
    Sets up a filter to process all events before they change internal
    state and are posted to the internal event queue.
    
    The filter is prototyped as: ::
    
           int SDL_EventFilter(void *userdata, SDL_Event * event);
    
    
    If the filter returns 1, then the event will be added to the internal
    queue. If it returns 0, then the event will be dropped from the queue,
    but the internal state will still be updated. This allows selective
    filtering of dynamically arriving events.
    
    Be very careful of what you do in the event filter function, as it may
    run in a different thread!
    
    There is one caveat when dealing with the SDL_QuitEvent event type.
    The event filter is only called when the window manager desires to
    close the application window. If the event filter returns 1, then the
    window will be closed, otherwise the window will remain open if
    possible.
    
    If the quit event is generated by an interrupt signal, it will bypass
    the internal queue and be delivered to the application at the next
    event poll.
    """
    filter_c = unbox(filter, 'int(*)(void *, SDL_Event *)')
    userdata_c = unbox(userdata, 'void *')
    lib.SDL_SetEventFilter(filter_c, userdata_c)

def setHint(name, value):
    """
    ``SDL_bool SDL_SetHint(char const *, char const *)``
    
    Set a hint with normal priority.
    
    :return: SDL_TRUE if the hint was set, SDL_FALSE otherwise
    """
    name_c = u8(name)
    value_c = u8(value)
    rc = lib.SDL_SetHint(name_c, value_c)
    return rc

def setHintWithPriority(name, value, priority):
    """
    ``SDL_bool SDL_SetHintWithPriority(char const *, char const *, SDL_HintPriority)``
    
    Set a hint with a specific priority.
    
    The priority controls the behavior when setting a hint that already
    has a value. Hints will replace existing hints of their priority and
    lower. Environment variables are considered to have override priority.
    
    :return: SDL_TRUE if the hint was set, SDL_FALSE otherwise
    """
    name_c = u8(name)
    value_c = u8(value)
    priority_c = priority
    rc = lib.SDL_SetHintWithPriority(name_c, value_c, priority_c)
    return rc

def setMainReady():
    """
    ``void SDL_SetMainReady(void)``
    
    This is called by the real SDL main function to let the rest of the
    library know that initialization was done properly.
    
    Calling this yourself without knowing what you're doing can cause
    crashes and hard to diagnose problems with your application.
    """
    lib.SDL_SetMainReady()

def setModState(modstate):
    """
    ``void SDL_SetModState(SDL_Keymod)``
    
    Set the current key modifier state for the keyboard.
    
    This does not change the keyboard state, only the key modifier flags.
    """
    modstate_c = modstate
    lib.SDL_SetModState(modstate_c)

def setPaletteColors(palette, colors, firstcolor, ncolors):
    """
    ``int SDL_SetPaletteColors(SDL_Palette *, SDL_Color const *, int, int)``
    
    Set a range of colors in a palette.
    
    :param palette: The palette to modify.
    :param colors: An array of colors to copy into the palette.
    :param firstcolor: The index of the first palette entry to modify.
    :param ncolors: The number of entries to modify.
    :return: 0 on success, or -1 if not all of the colors could be set.
    """
    palette_c = unbox(palette, 'SDL_Palette *')
    colors_c = unbox(colors, 'SDL_Color const *')
    firstcolor_c = firstcolor
    ncolors_c = ncolors
    rc = lib.SDL_SetPaletteColors(palette_c, colors_c, firstcolor_c, ncolors_c)
    return rc

def setPixelFormatPalette(format, palette):
    """
    ``int SDL_SetPixelFormatPalette(SDL_PixelFormat *, SDL_Palette *)``
    
    Set the palette for a pixel format structure.
    """
    format_c = unbox(format, 'SDL_PixelFormat *')
    palette_c = unbox(palette, 'SDL_Palette *')
    rc = lib.SDL_SetPixelFormatPalette(format_c, palette_c)
    return rc

def setRelativeMouseMode(enabled):
    """
    ``int SDL_SetRelativeMouseMode(SDL_bool)``
    
    Set relative mouse mode.
    
    :param enabled: Whether or not to enable relative mode
    :return: 0 on success, or -1 if relative mode is not supported.
    
    While the mouse is in relative mode, the cursor is hidden, and the
    driver will try to report continuous motion in the current window.
    Only relative motion events will be delivered, the mouse position will
    not change.
    
    This function will flush any pending mouse motion.
    
    See also SDL_GetRelativeMouseMode()
    """
    enabled_c = enabled
    rc = lib.SDL_SetRelativeMouseMode(enabled_c)
    return rc

def setRenderDrawBlendMode(renderer, blendMode):
    """
    ``int SDL_SetRenderDrawBlendMode(SDL_Renderer *, SDL_BlendMode)``
    
    Set the blend mode used for drawing operations (Fill and Line).
    
    :param renderer: The renderer for which blend mode should be set.
    :param blendMode: SDL_BlendMode to use for blending.
    :return: 0 on success, or -1 on error
    
    If the blend mode is not supported, the closest supported mode is
    chosen.
    
    See also SDL_GetRenderDrawBlendMode()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    blendMode_c = blendMode
    rc = lib.SDL_SetRenderDrawBlendMode(renderer_c, blendMode_c)
    if rc == -1: raise SDLError()
    return rc

def setRenderDrawColor(renderer, r, g, b, a):
    """
    ``int SDL_SetRenderDrawColor(SDL_Renderer *, unsigned char, unsigned char, unsigned char, unsigned char)``
    
    Set the color used for drawing operations (Rect, Line and Clear).
    
    :param renderer: The renderer for which drawing color should be set.
    :param r: The red value used to draw on the rendering target.
    :param g: The green value used to draw on the rendering target.
    :param b: The blue value used to draw on the rendering target.
    :param a: The alpha value used to draw on the rendering target,
        usually SDL_ALPHA_OPAQUE (255).
    :return: 0 on success, or -1 on error
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    r_c = r
    g_c = g
    b_c = b
    a_c = a
    rc = lib.SDL_SetRenderDrawColor(renderer_c, r_c, g_c, b_c, a_c)
    if rc == -1: raise SDLError()
    return rc

def setRenderTarget(renderer, texture):
    """
    ``int SDL_SetRenderTarget(SDL_Renderer *, SDL_Texture *)``
    
    Set a texture as the current rendering target.
    
    :param renderer: The renderer.
    :param texture: The targeted texture, which must be created with the
        SDL_TEXTUREACCESS_TARGET flag, or NULL for the default render
        target
    :return: 0 on success, or -1 on error
    
    See also SDL_GetRenderTarget()
    """
    renderer_c = unbox(renderer, 'SDL_Renderer *')
    texture_c = unbox(texture, 'SDL_Texture *')
    rc = lib.SDL_SetRenderTarget(renderer_c, texture_c)
    if rc == -1: raise SDLError()
    return rc

def setSurfaceAlphaMod(surface, alpha):
    """
    ``int SDL_SetSurfaceAlphaMod(SDL_Surface *, unsigned char)``
    
    Set an additional alpha value used in blit operations.
    
    :param surface: The surface to update.
    :param alpha: The alpha value multiplied into blit operations.
    :return: 0 on success, or -1 if the surface is not valid.
    
    See also SDL_GetSurfaceAlphaMod()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    alpha_c = alpha
    rc = lib.SDL_SetSurfaceAlphaMod(surface_c, alpha_c)
    return rc

def setSurfaceBlendMode(surface, blendMode):
    """
    ``int SDL_SetSurfaceBlendMode(SDL_Surface *, SDL_BlendMode)``
    
    Set the blend mode used for blit operations.
    
    :param surface: The surface to update.
    :param blendMode: SDL_BlendMode to use for blit blending.
    :return: 0 on success, or -1 if the parameters are not valid.
    
    See also SDL_GetSurfaceBlendMode()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    blendMode_c = blendMode
    rc = lib.SDL_SetSurfaceBlendMode(surface_c, blendMode_c)
    return rc

def setSurfaceColorMod(surface, r, g, b):
    """
    ``int SDL_SetSurfaceColorMod(SDL_Surface *, unsigned char, unsigned char, unsigned char)``
    
    Set an additional color value used in blit operations.
    
    :param surface: The surface to update.
    :param r: The red color value multiplied into blit operations.
    :param g: The green color value multiplied into blit operations.
    :param b: The blue color value multiplied into blit operations.
    :return: 0 on success, or -1 if the surface is not valid.
    
    See also SDL_GetSurfaceColorMod()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    r_c = r
    g_c = g
    b_c = b
    rc = lib.SDL_SetSurfaceColorMod(surface_c, r_c, g_c, b_c)
    return rc

def setSurfacePalette(surface, palette):
    """
    ``int SDL_SetSurfacePalette(SDL_Surface *, SDL_Palette *)``
    
    Set the palette used by a surface.
    
    :return: 0, or -1 if the surface format doesn't use a palette.
    
    A single palette can be shared with many surfaces.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    palette_c = unbox(palette, 'SDL_Palette *')
    rc = lib.SDL_SetSurfacePalette(surface_c, palette_c)
    return rc

def setSurfaceRLE(surface, flag):
    """
    ``int SDL_SetSurfaceRLE(SDL_Surface *, int)``
    
    Sets the RLE acceleration hint for a surface.
    
    :return: 0 on success, or -1 if the surface is not valid
    
    If RLE is enabled, colorkey and alpha blending blits are much faster,
    but the surface must be locked before directly accessing the pixels.
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    flag_c = flag
    rc = lib.SDL_SetSurfaceRLE(surface_c, flag_c)
    return rc

def setTextInputRect(rect):
    """
    ``void SDL_SetTextInputRect(SDL_Rect *)``
    
    Set the rectangle used to type Unicode text inputs. This is used as a
    hint for IME and on-screen keyboard placement.
    
    See also SDL_StartTextInput()
    """
    rect_c = unbox(rect, 'SDL_Rect *')
    lib.SDL_SetTextInputRect(rect_c)

def setTextureAlphaMod(texture, alpha):
    """
    ``int SDL_SetTextureAlphaMod(SDL_Texture *, unsigned char)``
    
    Set an additional alpha value used in render copy operations.
    
    :param texture: The texture to update.
    :param alpha: The alpha value multiplied into copy operations.
    :return: 0 on success, or -1 if the texture is not valid or alpha
        modulation is not supported.
    
    See also SDL_GetTextureAlphaMod()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    alpha_c = alpha
    rc = lib.SDL_SetTextureAlphaMod(texture_c, alpha_c)
    return rc

def setTextureBlendMode(texture, blendMode):
    """
    ``int SDL_SetTextureBlendMode(SDL_Texture *, SDL_BlendMode)``
    
    Set the blend mode used for texture copy operations.
    
    :param texture: The texture to update.
    :param blendMode: SDL_BlendMode to use for texture blending.
    :return: 0 on success, or -1 if the texture is not valid or the blend
        mode is not supported.
    
    If the blend mode is not supported, the closest supported mode is
    chosen.
    
    See also SDL_GetTextureBlendMode()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    blendMode_c = blendMode
    rc = lib.SDL_SetTextureBlendMode(texture_c, blendMode_c)
    return rc

def setTextureColorMod(texture, r, g, b):
    """
    ``int SDL_SetTextureColorMod(SDL_Texture *, unsigned char, unsigned char, unsigned char)``
    
    Set an additional color value used in render copy operations.
    
    :param texture: The texture to update.
    :param r: The red color value multiplied into copy operations.
    :param g: The green color value multiplied into copy operations.
    :param b: The blue color value multiplied into copy operations.
    :return: 0 on success, or -1 if the texture is not valid or color
        modulation is not supported.
    
    See also SDL_GetTextureColorMod()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    r_c = r
    g_c = g
    b_c = b
    rc = lib.SDL_SetTextureColorMod(texture_c, r_c, g_c, b_c)
    return rc

def setThreadPriority(priority):
    """
    ``int SDL_SetThreadPriority(SDL_ThreadPriority)``
    
    Set the priority for the current thread
    """
    priority_c = priority
    rc = lib.SDL_SetThreadPriority(priority_c)
    return rc

def setWindowBordered(window, bordered):
    """
    ``void SDL_SetWindowBordered(SDL_Window *, SDL_bool)``
    
    Set the border state of a window.
    
    This will add or remove the window's SDL_WINDOW_BORDERLESS flag and
    add or remove the border from the actual window. This is a no-op if
    the window's border already matches the requested state.
    
    :param window: The window of which to change the border state.
    :param bordered: SDL_FALSE to remove border, SDL_TRUE to add border.
    
    You can't change the border state of a fullscreen window.
    
    See also SDL_GetWindowFlags()
    """
    window_c = unbox(window, 'SDL_Window *')
    bordered_c = bordered
    lib.SDL_SetWindowBordered(window_c, bordered_c)

def setWindowBrightness(window, brightness):
    """
    ``int SDL_SetWindowBrightness(SDL_Window *, float)``
    
    Set the brightness (gamma correction) for a window.
    
    :return: 0 on success, or -1 if setting the brightness isn't
        supported.
    
    See also SDL_GetWindowBrightness()
    """
    window_c = unbox(window, 'SDL_Window *')
    brightness_c = brightness
    rc = lib.SDL_SetWindowBrightness(window_c, brightness_c)
    return rc

def setWindowData(window, name, userdata):
    """
    ``void * SDL_SetWindowData(SDL_Window *, char const *, void *)``
    
    Associate an arbitrary named pointer with a window.
    
    :param window: The window to associate with the pointer.
    :param name: The name of the pointer.
    :param userdata: The associated pointer.
    :return: The previous value associated with 'name'
    
    The name is case-sensitive.
    
    See also SDL_GetWindowData()
    """
    window_c = unbox(window, 'SDL_Window *')
    name_c = u8(name)
    userdata_c = unbox(userdata, 'void *')
    rc = lib.SDL_SetWindowData(window_c, name_c, userdata_c)
    return rc

def setWindowDisplayMode(window, mode):
    """
    ``int SDL_SetWindowDisplayMode(SDL_Window *, SDL_DisplayMode const *)``
    
    Set the display mode used when a fullscreen window is visible.
    
    By default the window's dimensions and the desktop format and refresh
    rate are used.
    
    :param window: The window for which the display mode should be set.
    :param mode: The mode to use, or NULL for the default mode.
    :return: 0 on success, or -1 if setting the display mode failed.
    
    See also SDL_GetWindowDisplayMode()
    """
    window_c = unbox(window, 'SDL_Window *')
    mode_c = unbox(mode, 'SDL_DisplayMode const *')
    rc = lib.SDL_SetWindowDisplayMode(window_c, mode_c)
    return rc

def setWindowFullscreen(window, flags):
    """
    ``int SDL_SetWindowFullscreen(SDL_Window *, unsigned int)``
    
    Set a window's fullscreen state.
    
    :return: 0 on success, or -1 if setting the display mode failed.
    
    See also SDL_SetWindowDisplayMode()
    """
    window_c = unbox(window, 'SDL_Window *')
    flags_c = flags
    rc = lib.SDL_SetWindowFullscreen(window_c, flags_c)
    return rc

def setWindowGammaRamp(window, red=None, green=None, blue=None):
    """
    ``int SDL_SetWindowGammaRamp(SDL_Window *, unsigned short const *, unsigned short const *, unsigned short const *)``
    
    Set the gamma ramp for a window.
    
    :param window: The window for which the gamma ramp should be set.
    :param red: The translation table for the red channel, or NULL.
    :param green: The translation table for the green channel, or NULL.
    :param blue: The translation table for the blue channel, or NULL.
    :return: 0 on success, or -1 if gamma ramps are unsupported.
    
    Set the gamma translation table for the red, green, and blue channels
    of the video hardware. Each table is an array of 256 16-bit
    quantities, representing a mapping between the input and output for
    that channel. The input is the index into the array, and the output is
    the 16-bit gamma value at that index, scaled to the output color
    precision.
    
    See also SDL_GetWindowGammaRamp()
    """
    window_c = unbox(window, 'SDL_Window *')
    red_c = unbox(red, 'unsigned short const *')
    green_c = unbox(green, 'unsigned short const *')
    blue_c = unbox(blue, 'unsigned short const *')
    rc = lib.SDL_SetWindowGammaRamp(window_c, red_c, green_c, blue_c)
    return (rc, red_c[0], green_c[0], blue_c[0])

def setWindowGrab(window, grabbed):
    """
    ``void SDL_SetWindowGrab(SDL_Window *, SDL_bool)``
    
    Set a window's input grab mode.
    
    :param window: The window for which the input grab mode should be set.
    :param grabbed: This is SDL_TRUE to grab input, and SDL_FALSE to
        release input.
    
    See also SDL_GetWindowGrab()
    """
    window_c = unbox(window, 'SDL_Window *')
    grabbed_c = grabbed
    lib.SDL_SetWindowGrab(window_c, grabbed_c)

def setWindowIcon(window, icon):
    """
    ``void SDL_SetWindowIcon(SDL_Window *, SDL_Surface *)``
    
    Set the icon for a window.
    
    :param window: The window for which the icon should be set.
    :param icon: The icon for the window.
    """
    window_c = unbox(window, 'SDL_Window *')
    icon_c = unbox(icon, 'SDL_Surface *')
    lib.SDL_SetWindowIcon(window_c, icon_c)

def setWindowMaximumSize(window, max_w, max_h):
    """
    ``void SDL_SetWindowMaximumSize(SDL_Window *, int, int)``
    
    Set the maximum size of a window's client area.
    
    :param window: The window to set a new maximum size.
    :param max_w: The maximum width of the window, must be >0
    :param max_h: The maximum height of the window, must be >0
    
    You can't change the maximum size of a fullscreen window, it
    automatically matches the size of the display mode.
    
    See also SDL_GetWindowMaximumSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    max_w_c = max_w
    max_h_c = max_h
    lib.SDL_SetWindowMaximumSize(window_c, max_w_c, max_h_c)

def setWindowMinimumSize(window, min_w, min_h):
    """
    ``void SDL_SetWindowMinimumSize(SDL_Window *, int, int)``
    
    Set the minimum size of a window's client area.
    
    :param window: The window to set a new minimum size.
    :param min_w: The minimum width of the window, must be >0
    :param min_h: The minimum height of the window, must be >0
    
    You can't change the minimum size of a fullscreen window, it
    automatically matches the size of the display mode.
    
    See also SDL_GetWindowMinimumSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    min_w_c = min_w
    min_h_c = min_h
    lib.SDL_SetWindowMinimumSize(window_c, min_w_c, min_h_c)

def setWindowPosition(window, x, y):
    """
    ``void SDL_SetWindowPosition(SDL_Window *, int, int)``
    
    Set the position of a window.
    
    :param window: The window to reposition.
    :param x: The x coordinate of the window, SDL_WINDOWPOS_CENTERED, or
        SDL_WINDOWPOS_UNDEFINED.
    :param y: The y coordinate of the window, SDL_WINDOWPOS_CENTERED, or
        SDL_WINDOWPOS_UNDEFINED.
    
    The window coordinate origin is the upper left of the display.
    
    See also SDL_GetWindowPosition()
    """
    window_c = unbox(window, 'SDL_Window *')
    x_c = x
    y_c = y
    lib.SDL_SetWindowPosition(window_c, x_c, y_c)

def setWindowSize(window, w, h):
    """
    ``void SDL_SetWindowSize(SDL_Window *, int, int)``
    
    Set the size of a window's client area.
    
    :param window: The window to resize.
    :param w: The width of the window, must be >0
    :param h: The height of the window, must be >0
    
    You can't change the size of a fullscreen window, it automatically
    matches the size of the display mode.
    
    See also SDL_GetWindowSize()
    """
    window_c = unbox(window, 'SDL_Window *')
    w_c = w
    h_c = h
    lib.SDL_SetWindowSize(window_c, w_c, h_c)

def setWindowTitle(window, title):
    """
    ``void SDL_SetWindowTitle(SDL_Window *, char const *)``
    
    Set the title of a window, in UTF-8 format.
    
    See also SDL_GetWindowTitle()
    """
    window_c = unbox(window, 'SDL_Window *')
    title_c = u8(title)
    lib.SDL_SetWindowTitle(window_c, title_c)

def showCursor(toggle):
    """
    ``int SDL_ShowCursor(int)``
    
    Toggle whether or not the cursor is shown.
    
    :param toggle: 1 to show the cursor, 0 to hide it, -1 to query the
        current state.
    :return: 1 if the cursor is shown, or 0 if the cursor is hidden.
    """
    toggle_c = toggle
    rc = lib.SDL_ShowCursor(toggle_c)
    return rc

def showMessageBox(messageboxdata, buttonid=None):
    """
    ``int SDL_ShowMessageBox(SDL_MessageBoxData const *, int *)``
    
    Create a modal message box.
    
    :param messageboxdata: The SDL_MessageBoxData structure with title,
        text, etc.
    :param buttonid: The pointer to which user id of hit button should be
        copied.
    :return: -1 on error, otherwise 0 and buttonid contains user id of
        button hit or -1 if dialog was closed.
    
    This function should be called on the thread that created the parent
    window, or on the main thread if the messagebox has no parent. It will
    block execution of that thread until the user clicks a button or
    closes the messagebox.
    """
    messageboxdata_c = unbox(messageboxdata, 'SDL_MessageBoxData const *')
    buttonid_c = unbox(buttonid, 'int *')
    rc = lib.SDL_ShowMessageBox(messageboxdata_c, buttonid_c)
    if rc == -1: raise SDLError()
    return (rc, buttonid_c[0])

def showSimpleMessageBox(flags, title, message, window):
    """
    ``int SDL_ShowSimpleMessageBox(unsigned int, char const *, char const *, SDL_Window *)``
    
    Create a simple modal message box.
    
    :param flags: SDL_MessageBoxFlags
    :param title: UTF-8 title text
    :param message: UTF-8 message text
    :param window: The parent window, or NULL for no parent
    :return: 0 on success, -1 on error
    
    See also SDL_ShowMessageBox
    """
    flags_c = flags
    title_c = u8(title)
    message_c = u8(message)
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_ShowSimpleMessageBox(flags_c, title_c, message_c, window_c)
    if rc == -1: raise SDLError()
    return rc

def showWindow(window):
    """
    ``void SDL_ShowWindow(SDL_Window *)``
    
    Show a window.
    
    See also SDL_HideWindow()
    """
    window_c = unbox(window, 'SDL_Window *')
    lib.SDL_ShowWindow(window_c)

def softStretch(src, srcrect, dst, dstrect):
    """
    ``int SDL_SoftStretch(SDL_Surface *, SDL_Rect const *, SDL_Surface *, SDL_Rect const *)``
    
    Perform a fast, low quality, stretch blit between two surfaces of the
    same pixel format.
    
    This function uses a static buffer, and is not thread-safe.
    """
    src_c = unbox(src, 'SDL_Surface *')
    srcrect_c = unbox(srcrect, 'SDL_Rect const *')
    dst_c = unbox(dst, 'SDL_Surface *')
    dstrect_c = unbox(dstrect, 'SDL_Rect const *')
    rc = lib.SDL_SoftStretch(src_c, srcrect_c, dst_c, dstrect_c)
    return rc

def startTextInput():
    """
    ``void SDL_StartTextInput(void)``
    
    Start accepting Unicode text input events. This function will show the
    on-screen keyboard if supported.
    
    See also SDL_StopTextInput()
    """
    lib.SDL_StartTextInput()

def stopTextInput():
    """
    ``void SDL_StopTextInput(void)``
    
    Stop receiving any text input events. This function will hide the on-
    screen keyboard if supported.
    
    See also SDL_StartTextInput()
    """
    lib.SDL_StopTextInput()

def TLSCreate():
    """
    ``unsigned int SDL_TLSCreate(void)``
    
    Create an identifier that is globally visible to all threads but
    refers to data that is thread-specific.
    
    :return: The newly created thread local storage identifier, or 0 on
        error
    ::
    
       static SDL_SpinLock tls_lock;
       static SDL_TLSID thread_local_storage;
    
    
    
       void SetMyThreadData(void *value)
       {
           if (!thread_local_storage) {
               SDL_AtomicLock(&tls_lock);
               if (!thread_local_storage) {
                   thread_local_storage = SDL_TLSCreate();
               }
               SDL_AtomicUnLock(&tls_lock);
           }
           SDL_TLSSet(thread_local_storage, value);
       }
    
       void *GetMyThreadData(void)
       {
           return SDL_TLSGet(thread_local_storage);
       }
    
    
    See also SDL_TLSGet()
    """
    rc = lib.SDL_TLSCreate()
    return rc

def TLSGet(id):
    """
    ``void * SDL_TLSGet(unsigned int)``
    
    Get the value associated with a thread local storage ID for the
    current thread.
    
    :param id: The thread local storage ID
    :return: The value associated with the ID for the current thread, or
        NULL if no value has been set.
    
    See also SDL_TLSCreate()
    """
    id_c = id
    rc = lib.SDL_TLSGet(id_c)
    return rc

def TLSSet(id, value, destructor):
    """
    ``int SDL_TLSSet(unsigned int, void const *, void SDL_TLSSet(void *))``
    
    Set the value associated with a thread local storage ID for the
    current thread.
    
    :param id: The thread local storage ID
    :param value: The value to associate with the ID for the current
        thread
    :param destructor: A function called when the thread exits, to free
        the value.
    :return: 0 on success, -1 on error
    
    See also SDL_TLSCreate()
    """
    id_c = id
    value_c = unbox(value, 'void const *')
    destructor_c = unbox(destructor, 'void(*)(void *)')
    rc = lib.SDL_TLSSet(id_c, value_c, destructor_c)
    if rc == -1: raise SDLError()
    return rc

def threadID():
    """
    ``unsigned long SDL_ThreadID(void)``
    
    Get the thread identifier for the current thread.
    """
    rc = lib.SDL_ThreadID()
    return rc

def tryLockMutex(mutex):
    """
    ``int SDL_TryLockMutex(SDL_mutex *)``
    
    Try to lock the mutex
    
    :return: 0, SDL_MUTEX_TIMEDOUT, or -1 on error
    """
    mutex_c = unbox(mutex, 'SDL_mutex *')
    rc = lib.SDL_TryLockMutex(mutex_c)
    if rc == -1: raise SDLError()
    return rc

def unionRect(A, B, result):
    """
    ``void SDL_UnionRect(SDL_Rect const *, SDL_Rect const *, SDL_Rect *)``
    
    Calculate the union of two rectangles.
    """
    A_c = unbox(A, 'SDL_Rect const *')
    B_c = unbox(B, 'SDL_Rect const *')
    result_c = unbox(result, 'SDL_Rect *')
    lib.SDL_UnionRect(A_c, B_c, result_c)

def unloadObject(handle):
    """
    ``void SDL_UnloadObject(void *)``
    
    Unload a shared object from memory.
    """
    handle_c = unbox(handle, 'void *')
    lib.SDL_UnloadObject(handle_c)

def unlockAudio():
    """
    ``void SDL_UnlockAudio(void)``
    """
    lib.SDL_UnlockAudio()

def unlockAudioDevice(dev):
    """
    ``void SDL_UnlockAudioDevice(unsigned int)``
    """
    dev_c = dev
    lib.SDL_UnlockAudioDevice(dev_c)

def unlockMutex(mutex):
    """
    ``int SDL_UnlockMutex(SDL_mutex *)``
    """
    mutex_c = unbox(mutex, 'SDL_mutex *')
    rc = lib.SDL_UnlockMutex(mutex_c)
    return rc

def unlockSurface(surface):
    """
    ``void SDL_UnlockSurface(SDL_Surface *)``
    
    See also SDL_LockSurface()
    """
    surface_c = unbox(surface, 'SDL_Surface *')
    lib.SDL_UnlockSurface(surface_c)

def unlockTexture(texture):
    """
    ``void SDL_UnlockTexture(SDL_Texture *)``
    
    Unlock a texture, uploading the changes to video memory, if needed.
    
    See also SDL_LockTexture()
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    lib.SDL_UnlockTexture(texture_c)

def updateTexture(texture, rect, pixels, pitch):
    """
    ``int SDL_UpdateTexture(SDL_Texture *, SDL_Rect const *, void const *, int)``
    
    Update the given texture rectangle with new pixel data.
    
    :param texture: The texture to update
    :param rect: A pointer to the rectangle of pixels to update, or NULL
        to update the entire texture.
    :param pixels: The raw pixel data.
    :param pitch: The number of bytes between rows of pixel data.
    :return: 0 on success, or -1 if the texture is not valid.
    
    This is a fairly slow function.
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    pixels_c = unbox(pixels, 'void const *')
    pitch_c = pitch
    rc = lib.SDL_UpdateTexture(texture_c, rect_c, pixels_c, pitch_c)
    return rc

def updateWindowSurface(window):
    """
    ``int SDL_UpdateWindowSurface(SDL_Window *)``
    
    Copy the window surface to the screen.
    
    :return: 0 on success, or -1 on error.
    
    See also SDL_GetWindowSurface()
    """
    window_c = unbox(window, 'SDL_Window *')
    rc = lib.SDL_UpdateWindowSurface(window_c)
    if rc == -1: raise SDLError()
    return rc

def updateWindowSurfaceRects(window, rects, numrects):
    """
    ``int SDL_UpdateWindowSurfaceRects(SDL_Window *, SDL_Rect const *, int)``
    
    Copy a number of rectangles on the window surface to the screen.
    
    :return: 0 on success, or -1 on error.
    
    See also SDL_GetWindowSurface()
    """
    window_c = unbox(window, 'SDL_Window *')
    rects_c = unbox(rects, 'SDL_Rect const *')
    numrects_c = numrects
    rc = lib.SDL_UpdateWindowSurfaceRects(window_c, rects_c, numrects_c)
    if rc == -1: raise SDLError()
    return rc

def updateYUVTexture(texture, rect, Yplane, Ypitch, Uplane, Upitch, Vplane, Vpitch):
    """
    ``int SDL_UpdateYUVTexture(SDL_Texture *, SDL_Rect const *, unsigned char const *, int, unsigned char const *, int, unsigned char const *, int)``
    
    Update a rectangle within a planar YV12 or IYUV texture with new pixel
    data.
    
    :param texture: The texture to update
    :param rect: A pointer to the rectangle of pixels to update, or NULL
        to update the entire texture.
    :param Yplane: The raw pixel data for the Y plane.
    :param Ypitch: The number of bytes between rows of pixel data for the
        Y plane.
    :param Uplane: The raw pixel data for the U plane.
    :param Upitch: The number of bytes between rows of pixel data for the
        U plane.
    :param Vplane: The raw pixel data for the V plane.
    :param Vpitch: The number of bytes between rows of pixel data for the
        V plane.
    :return: 0 on success, or -1 if the texture is not valid.
    
    You can use SDL_UpdateTexture() as long as your pixel data is a
    contiguous block of Y and U/V planes in the proper order, but this
    function is available if your pixel data is not contiguous.
    """
    texture_c = unbox(texture, 'SDL_Texture *')
    rect_c = unbox(rect, 'SDL_Rect const *')
    Yplane_c = unbox(Yplane, 'unsigned char const *')
    Ypitch_c = Ypitch
    Uplane_c = unbox(Uplane, 'unsigned char const *')
    Upitch_c = Upitch
    Vplane_c = unbox(Vplane, 'unsigned char const *')
    Vpitch_c = Vpitch
    rc = lib.SDL_UpdateYUVTexture(texture_c, rect_c, Yplane_c, Ypitch_c, Uplane_c, Upitch_c, Vplane_c, Vpitch_c)
    return rc

def upperBlit(src, srcrect, dst, dstrect):
    """
    ``int SDL_UpperBlit(SDL_Surface *, SDL_Rect const *, SDL_Surface *, SDL_Rect *)``
    
    This is the public blit function, SDL_BlitSurface(), and it performs
    rectangle validation and clipping before passing it to SDL_LowerBlit()
    """
    src_c = unbox(src, 'SDL_Surface *')
    srcrect_c = unbox(srcrect, 'SDL_Rect const *', nullable=True)
    dst_c = unbox(dst, 'SDL_Surface *')
    dstrect_c = unbox(dstrect, 'SDL_Rect *', nullable=True)
    rc = lib.SDL_UpperBlit(src_c, srcrect_c, dst_c, dstrect_c)
    return rc

def upperBlitScaled(src, srcrect, dst, dstrect):
    """
    ``int SDL_UpperBlitScaled(SDL_Surface *, SDL_Rect const *, SDL_Surface *, SDL_Rect *)``
    
    This is the public scaled blit function, SDL_BlitScaled(), and it
    performs rectangle validation and clipping before passing it to
    SDL_LowerBlitScaled()
    """
    src_c = unbox(src, 'SDL_Surface *')
    srcrect_c = unbox(srcrect, 'SDL_Rect const *', nullable=True)
    dst_c = unbox(dst, 'SDL_Surface *')
    dstrect_c = unbox(dstrect, 'SDL_Rect *', nullable=True)
    rc = lib.SDL_UpperBlitScaled(src_c, srcrect_c, dst_c, dstrect_c)
    return rc

def videoInit(driver_name):
    """
    ``int SDL_VideoInit(char const *)``
    
    Initialize the video subsystem, optionally specifying a video driver.
    
    :param driver_name: Initialize a specific driver by name, or NULL for
        the default video driver.
    :return: 0 on success, -1 on error
    
    This function initializes the video subsystem; setting up a connection
    to the window manager, etc, and determines the available display modes
    and pixel formats, but does not initialize a window or graphics mode.
    
    See also SDL_VideoQuit()
    """
    driver_name_c = u8(driver_name)
    rc = lib.SDL_VideoInit(driver_name_c)
    if rc == -1: raise SDLError()
    return rc

def videoQuit():
    """
    ``void SDL_VideoQuit(void)``
    
    Shuts down the video subsystem.
    
    This function closes all windows, and restores the original video
    mode.
    
    See also SDL_VideoInit()
    """
    lib.SDL_VideoQuit()

def waitEvent(event):
    """
    ``int SDL_WaitEvent(SDL_Event *)``
    
    Waits indefinitely for the next available event.
    
    :return: 1, or 0 if there was an error while waiting for events.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    """
    event_c = unbox(event, 'SDL_Event *')
    rc = lib.SDL_WaitEvent(event_c)
    return rc

def waitEventTimeout(event, timeout):
    """
    ``int SDL_WaitEventTimeout(SDL_Event *, int)``
    
    Waits until the specified timeout (in milliseconds) for the next
    available event.
    
    :return: 1, or 0 if there was an error while waiting for events.
    :param event: If not NULL, the next event is removed from the queue
        and stored in that area.
    :param timeout: The timeout (in milliseconds) to wait for next event.
    """
    event_c = unbox(event, 'SDL_Event *')
    timeout_c = timeout
    rc = lib.SDL_WaitEventTimeout(event_c, timeout_c)
    return rc

def waitThread(thread, status=None):
    """
    ``void SDL_WaitThread(SDL_Thread *, int *)``
    
    Wait for a thread to finish. Threads that haven't been detached will
    remain (as a "zombie") until this function cleans them up. Not doing
    so is a resource leak.
    
    Once a thread has been cleaned up through this function, the
    SDL_Thread that references it becomes invalid and should not be
    referenced again. As such, only one thread may call SDL_WaitThread()
    on another.
    
    The return code for the thread function is placed in the area pointed
    to by status, if status is not NULL.
    
    You may not wait on a thread that has been used in a call to
    SDL_DetachThread(). Use either that function or this one, but not
    both, or behavior is undefined.
    
    It is safe to pass NULL to this function; it is a no-op.
    """
    thread_c = unbox(thread, 'SDL_Thread *')
    status_c = unbox(status, 'int *')
    lib.SDL_WaitThread(thread_c, status_c)
    return status_c[0]

def warpMouseInWindow(window, x, y):
    """
    ``void SDL_WarpMouseInWindow(SDL_Window *, int, int)``
    
    Moves the mouse to the given position within the window.
    
    :param window: The window to move the mouse into, or NULL for the
        current mouse focus
    :param x: The x coordinate within the window
    :param y: The y coordinate within the window
    
    This function generates a mouse motion event
    """
    window_c = unbox(window, 'SDL_Window *')
    x_c = x
    y_c = y
    lib.SDL_WarpMouseInWindow(window_c, x_c, y_c)

def wasInit(flags):
    """
    ``unsigned int SDL_WasInit(unsigned int)``
    
    This function returns a mask of the specified subsystems which have
    previously been initialized.
    
    If flags is 0, it returns a mask of all initialized subsystems.
    """
    flags_c = flags
    rc = lib.SDL_WasInit(flags_c)
    return rc

def writeBE16(dst, value):
    """
    ``size_t SDL_WriteBE16(SDL_RWops *, unsigned short)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteBE16(dst_c, value_c)
    return rc

def writeBE32(dst, value):
    """
    ``size_t SDL_WriteBE32(SDL_RWops *, unsigned int)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteBE32(dst_c, value_c)
    return rc

def writeBE64(dst, value):
    """
    ``size_t SDL_WriteBE64(SDL_RWops *, unsigned long)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteBE64(dst_c, value_c)
    return rc

def writeLE16(dst, value):
    """
    ``size_t SDL_WriteLE16(SDL_RWops *, unsigned short)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteLE16(dst_c, value_c)
    return rc

def writeLE32(dst, value):
    """
    ``size_t SDL_WriteLE32(SDL_RWops *, unsigned int)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteLE32(dst_c, value_c)
    return rc

def writeLE64(dst, value):
    """
    ``size_t SDL_WriteLE64(SDL_RWops *, unsigned long)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteLE64(dst_c, value_c)
    return rc

def writeU8(dst, value):
    """
    ``size_t SDL_WriteU8(SDL_RWops *, unsigned char)``
    """
    dst_c = unbox(dst, 'SDL_RWops *')
    value_c = value
    rc = lib.SDL_WriteU8(dst_c, value_c)
    return rc

def abs(x):
    """
    ``int SDL_abs(int)``
    """
    x_c = x
    rc = lib.SDL_abs(x_c)
    return rc

def calloc(nmemb, size):
    """
    ``void * SDL_calloc(size_t, size_t)``
    """
    nmemb_c = nmemb
    size_c = size
    rc = lib.SDL_calloc(nmemb_c, size_c)
    return rc

def free(mem):
    """
    ``void SDL_free(void *)``
    """
    mem_c = unbox(mem, 'void *')
    lib.SDL_free(mem_c)

def getenv(name):
    """
    ``char * SDL_getenv(char const *)``
    """
    name_c = u8(name)
    rc = lib.SDL_getenv(name_c)
    return ffi.string(rc).decode('utf-8')

def isdigit(x):
    """
    ``int SDL_isdigit(int)``
    """
    x_c = x
    rc = lib.SDL_isdigit(x_c)
    return rc

def isspace(x):
    """
    ``int SDL_isspace(int)``
    """
    x_c = x
    rc = lib.SDL_isspace(x_c)
    return rc

def malloc(size):
    """
    ``void * SDL_malloc(size_t)``
    """
    size_c = size
    rc = lib.SDL_malloc(size_c)
    return rc

def memcmp(s1, s2, len):
    """
    ``int SDL_memcmp(void const *, void const *, size_t)``
    """
    s1_c = unbox(s1, 'void const *')
    s2_c = unbox(s2, 'void const *')
    len_c = len
    rc = lib.SDL_memcmp(s1_c, s2_c, len_c)
    return rc

def memcpy(dst, src, len):
    """
    ``void * SDL_memcpy(void *, void const *, size_t)``
    """
    dst_c = unbox(dst, 'void *')
    src_c = unbox(src, 'void const *')
    len_c = len
    rc = lib.SDL_memcpy(dst_c, src_c, len_c)
    return rc

def memmove(dst, src, len):
    """
    ``void * SDL_memmove(void *, void const *, size_t)``
    """
    dst_c = unbox(dst, 'void *')
    src_c = unbox(src, 'void const *')
    len_c = len
    rc = lib.SDL_memmove(dst_c, src_c, len_c)
    return rc

def memset(dst, c, len):
    """
    ``void * SDL_memset(void *, int, size_t)``
    """
    dst_c = unbox(dst, 'void *')
    c_c = c
    len_c = len
    rc = lib.SDL_memset(dst_c, c_c, len_c)
    return rc

def qsort(base, nmemb, size, compare):
    """
    ``void SDL_qsort(void *, size_t, size_t, int SDL_qsort(void const *, void const *))``
    """
    base_c = unbox(base, 'void *')
    nmemb_c = nmemb
    size_c = size
    compare_c = unbox(compare, 'int(*)(void const *, void const *)')
    lib.SDL_qsort(base_c, nmemb_c, size_c, compare_c)

def realloc(mem, size):
    """
    ``void * SDL_realloc(void *, size_t)``
    """
    mem_c = unbox(mem, 'void *')
    size_c = size
    rc = lib.SDL_realloc(mem_c, size_c)
    return rc

def setenv(name, value, overwrite):
    """
    ``int SDL_setenv(char const *, char const *, int)``
    """
    name_c = u8(name)
    value_c = u8(value)
    overwrite_c = overwrite
    rc = lib.SDL_setenv(name_c, value_c, overwrite_c)
    return rc

def tolower(x):
    """
    ``int SDL_tolower(int)``
    """
    x_c = x
    rc = lib.SDL_tolower(x_c)
    return rc

def toupper(x):
    """
    ``int SDL_toupper(int)``
    """
    x_c = x
    rc = lib.SDL_toupper(x_c)
    return rc

PIXELFORMAT_UNKNOWN = lib.SDL_PIXELFORMAT_UNKNOWN
PIXELFORMAT_INDEX1LSB = lib.SDL_PIXELFORMAT_INDEX1LSB
PIXELFORMAT_INDEX1MSB = lib.SDL_PIXELFORMAT_INDEX1MSB
PIXELFORMAT_INDEX4LSB = lib.SDL_PIXELFORMAT_INDEX4LSB
PIXELFORMAT_INDEX4MSB = lib.SDL_PIXELFORMAT_INDEX4MSB
PIXELFORMAT_INDEX8 = lib.SDL_PIXELFORMAT_INDEX8
PIXELFORMAT_RGB332 = lib.SDL_PIXELFORMAT_RGB332
PIXELFORMAT_RGB444 = lib.SDL_PIXELFORMAT_RGB444
PIXELFORMAT_RGB555 = lib.SDL_PIXELFORMAT_RGB555
PIXELFORMAT_BGR555 = lib.SDL_PIXELFORMAT_BGR555
PIXELFORMAT_ARGB4444 = lib.SDL_PIXELFORMAT_ARGB4444
PIXELFORMAT_RGBA4444 = lib.SDL_PIXELFORMAT_RGBA4444
PIXELFORMAT_ABGR4444 = lib.SDL_PIXELFORMAT_ABGR4444
PIXELFORMAT_BGRA4444 = lib.SDL_PIXELFORMAT_BGRA4444
PIXELFORMAT_ARGB1555 = lib.SDL_PIXELFORMAT_ARGB1555
PIXELFORMAT_RGBA5551 = lib.SDL_PIXELFORMAT_RGBA5551
PIXELFORMAT_ABGR1555 = lib.SDL_PIXELFORMAT_ABGR1555
PIXELFORMAT_BGRA5551 = lib.SDL_PIXELFORMAT_BGRA5551
PIXELFORMAT_RGB565 = lib.SDL_PIXELFORMAT_RGB565
PIXELFORMAT_BGR565 = lib.SDL_PIXELFORMAT_BGR565
PIXELFORMAT_RGB24 = lib.SDL_PIXELFORMAT_RGB24
PIXELFORMAT_BGR24 = lib.SDL_PIXELFORMAT_BGR24
PIXELFORMAT_RGB888 = lib.SDL_PIXELFORMAT_RGB888
PIXELFORMAT_RGBX8888 = lib.SDL_PIXELFORMAT_RGBX8888
PIXELFORMAT_BGR888 = lib.SDL_PIXELFORMAT_BGR888
PIXELFORMAT_BGRX8888 = lib.SDL_PIXELFORMAT_BGRX8888
PIXELFORMAT_ARGB8888 = lib.SDL_PIXELFORMAT_ARGB8888
PIXELFORMAT_RGBA8888 = lib.SDL_PIXELFORMAT_RGBA8888
PIXELFORMAT_ABGR8888 = lib.SDL_PIXELFORMAT_ABGR8888
PIXELFORMAT_BGRA8888 = lib.SDL_PIXELFORMAT_BGRA8888
PIXELFORMAT_ARGB2101010 = lib.SDL_PIXELFORMAT_ARGB2101010
PIXELFORMAT_YV12 = lib.SDL_PIXELFORMAT_YV12
PIXELFORMAT_IYUV = lib.SDL_PIXELFORMAT_IYUV
PIXELFORMAT_YUY2 = lib.SDL_PIXELFORMAT_YUY2
PIXELFORMAT_UYVY = lib.SDL_PIXELFORMAT_UYVY
PIXELFORMAT_YVYU = lib.SDL_PIXELFORMAT_YVYU

K_UNKNOWN = lib.SDLK_UNKNOWN
K_RETURN = lib.SDLK_RETURN
K_ESCAPE = lib.SDLK_ESCAPE
K_BACKSPACE = lib.SDLK_BACKSPACE
K_TAB = lib.SDLK_TAB
K_SPACE = lib.SDLK_SPACE
K_EXCLAIM = lib.SDLK_EXCLAIM
K_QUOTEDBL = lib.SDLK_QUOTEDBL
K_HASH = lib.SDLK_HASH
K_PERCENT = lib.SDLK_PERCENT
K_DOLLAR = lib.SDLK_DOLLAR
K_AMPERSAND = lib.SDLK_AMPERSAND
K_QUOTE = lib.SDLK_QUOTE
K_LEFTPAREN = lib.SDLK_LEFTPAREN
K_RIGHTPAREN = lib.SDLK_RIGHTPAREN
K_ASTERISK = lib.SDLK_ASTERISK
K_PLUS = lib.SDLK_PLUS
K_COMMA = lib.SDLK_COMMA
K_MINUS = lib.SDLK_MINUS
K_PERIOD = lib.SDLK_PERIOD
K_SLASH = lib.SDLK_SLASH
K_0 = lib.SDLK_0
K_1 = lib.SDLK_1
K_2 = lib.SDLK_2
K_3 = lib.SDLK_3
K_4 = lib.SDLK_4
K_5 = lib.SDLK_5
K_6 = lib.SDLK_6
K_7 = lib.SDLK_7
K_8 = lib.SDLK_8
K_9 = lib.SDLK_9
K_COLON = lib.SDLK_COLON
K_SEMICOLON = lib.SDLK_SEMICOLON
K_LESS = lib.SDLK_LESS
K_EQUALS = lib.SDLK_EQUALS
K_GREATER = lib.SDLK_GREATER
K_QUESTION = lib.SDLK_QUESTION
K_AT = lib.SDLK_AT
K_LEFTBRACKET = lib.SDLK_LEFTBRACKET
K_BACKSLASH = lib.SDLK_BACKSLASH
K_RIGHTBRACKET = lib.SDLK_RIGHTBRACKET
K_CARET = lib.SDLK_CARET
K_UNDERSCORE = lib.SDLK_UNDERSCORE
K_BACKQUOTE = lib.SDLK_BACKQUOTE
K_a = lib.SDLK_a
K_b = lib.SDLK_b
K_c = lib.SDLK_c
K_d = lib.SDLK_d
K_e = lib.SDLK_e
K_f = lib.SDLK_f
K_g = lib.SDLK_g
K_h = lib.SDLK_h
K_i = lib.SDLK_i
K_j = lib.SDLK_j
K_k = lib.SDLK_k
K_l = lib.SDLK_l
K_m = lib.SDLK_m
K_n = lib.SDLK_n
K_o = lib.SDLK_o
K_p = lib.SDLK_p
K_q = lib.SDLK_q
K_r = lib.SDLK_r
K_s = lib.SDLK_s
K_t = lib.SDLK_t
K_u = lib.SDLK_u
K_v = lib.SDLK_v
K_w = lib.SDLK_w
K_x = lib.SDLK_x
K_y = lib.SDLK_y
K_z = lib.SDLK_z
K_CAPSLOCK = lib.SDLK_CAPSLOCK
K_F1 = lib.SDLK_F1
K_F2 = lib.SDLK_F2
K_F3 = lib.SDLK_F3
K_F4 = lib.SDLK_F4
K_F5 = lib.SDLK_F5
K_F6 = lib.SDLK_F6
K_F7 = lib.SDLK_F7
K_F8 = lib.SDLK_F8
K_F9 = lib.SDLK_F9
K_F10 = lib.SDLK_F10
K_F11 = lib.SDLK_F11
K_F12 = lib.SDLK_F12
K_PRINTSCREEN = lib.SDLK_PRINTSCREEN
K_SCROLLLOCK = lib.SDLK_SCROLLLOCK
K_PAUSE = lib.SDLK_PAUSE
K_INSERT = lib.SDLK_INSERT
K_HOME = lib.SDLK_HOME
K_PAGEUP = lib.SDLK_PAGEUP
K_DELETE = lib.SDLK_DELETE
K_END = lib.SDLK_END
K_PAGEDOWN = lib.SDLK_PAGEDOWN
K_RIGHT = lib.SDLK_RIGHT
K_LEFT = lib.SDLK_LEFT
K_DOWN = lib.SDLK_DOWN
K_UP = lib.SDLK_UP
K_NUMLOCKCLEAR = lib.SDLK_NUMLOCKCLEAR
K_KP_DIVIDE = lib.SDLK_KP_DIVIDE
K_KP_MULTIPLY = lib.SDLK_KP_MULTIPLY
K_KP_MINUS = lib.SDLK_KP_MINUS
K_KP_PLUS = lib.SDLK_KP_PLUS
K_KP_ENTER = lib.SDLK_KP_ENTER
K_KP_1 = lib.SDLK_KP_1
K_KP_2 = lib.SDLK_KP_2
K_KP_3 = lib.SDLK_KP_3
K_KP_4 = lib.SDLK_KP_4
K_KP_5 = lib.SDLK_KP_5
K_KP_6 = lib.SDLK_KP_6
K_KP_7 = lib.SDLK_KP_7
K_KP_8 = lib.SDLK_KP_8
K_KP_9 = lib.SDLK_KP_9
K_KP_0 = lib.SDLK_KP_0
K_KP_PERIOD = lib.SDLK_KP_PERIOD
K_APPLICATION = lib.SDLK_APPLICATION
K_POWER = lib.SDLK_POWER
K_KP_EQUALS = lib.SDLK_KP_EQUALS
K_F13 = lib.SDLK_F13
K_F14 = lib.SDLK_F14
K_F15 = lib.SDLK_F15
K_F16 = lib.SDLK_F16
K_F17 = lib.SDLK_F17
K_F18 = lib.SDLK_F18
K_F19 = lib.SDLK_F19
K_F20 = lib.SDLK_F20
K_F21 = lib.SDLK_F21
K_F22 = lib.SDLK_F22
K_F23 = lib.SDLK_F23
K_F24 = lib.SDLK_F24
K_EXECUTE = lib.SDLK_EXECUTE
K_HELP = lib.SDLK_HELP
K_MENU = lib.SDLK_MENU
K_SELECT = lib.SDLK_SELECT
K_STOP = lib.SDLK_STOP
K_AGAIN = lib.SDLK_AGAIN
K_UNDO = lib.SDLK_UNDO
K_CUT = lib.SDLK_CUT
K_COPY = lib.SDLK_COPY
K_PASTE = lib.SDLK_PASTE
K_FIND = lib.SDLK_FIND
K_MUTE = lib.SDLK_MUTE
K_VOLUMEUP = lib.SDLK_VOLUMEUP
K_VOLUMEDOWN = lib.SDLK_VOLUMEDOWN
K_KP_COMMA = lib.SDLK_KP_COMMA
K_KP_EQUALSAS400 = lib.SDLK_KP_EQUALSAS400
K_ALTERASE = lib.SDLK_ALTERASE
K_SYSREQ = lib.SDLK_SYSREQ
K_CANCEL = lib.SDLK_CANCEL
K_CLEAR = lib.SDLK_CLEAR
K_PRIOR = lib.SDLK_PRIOR
K_RETURN2 = lib.SDLK_RETURN2
K_SEPARATOR = lib.SDLK_SEPARATOR
K_OUT = lib.SDLK_OUT
K_OPER = lib.SDLK_OPER
K_CLEARAGAIN = lib.SDLK_CLEARAGAIN
K_CRSEL = lib.SDLK_CRSEL
K_EXSEL = lib.SDLK_EXSEL
K_KP_00 = lib.SDLK_KP_00
K_KP_000 = lib.SDLK_KP_000
K_THOUSANDSSEPARATOR = lib.SDLK_THOUSANDSSEPARATOR
K_DECIMALSEPARATOR = lib.SDLK_DECIMALSEPARATOR
K_CURRENCYUNIT = lib.SDLK_CURRENCYUNIT
K_CURRENCYSUBUNIT = lib.SDLK_CURRENCYSUBUNIT
K_KP_LEFTPAREN = lib.SDLK_KP_LEFTPAREN
K_KP_RIGHTPAREN = lib.SDLK_KP_RIGHTPAREN
K_KP_LEFTBRACE = lib.SDLK_KP_LEFTBRACE
K_KP_RIGHTBRACE = lib.SDLK_KP_RIGHTBRACE
K_KP_TAB = lib.SDLK_KP_TAB
K_KP_BACKSPACE = lib.SDLK_KP_BACKSPACE
K_KP_A = lib.SDLK_KP_A
K_KP_B = lib.SDLK_KP_B
K_KP_C = lib.SDLK_KP_C
K_KP_D = lib.SDLK_KP_D
K_KP_E = lib.SDLK_KP_E
K_KP_F = lib.SDLK_KP_F
K_KP_XOR = lib.SDLK_KP_XOR
K_KP_POWER = lib.SDLK_KP_POWER
K_KP_PERCENT = lib.SDLK_KP_PERCENT
K_KP_LESS = lib.SDLK_KP_LESS
K_KP_GREATER = lib.SDLK_KP_GREATER
K_KP_AMPERSAND = lib.SDLK_KP_AMPERSAND
K_KP_DBLAMPERSAND = lib.SDLK_KP_DBLAMPERSAND
K_KP_VERTICALBAR = lib.SDLK_KP_VERTICALBAR
K_KP_DBLVERTICALBAR = lib.SDLK_KP_DBLVERTICALBAR
K_KP_COLON = lib.SDLK_KP_COLON
K_KP_HASH = lib.SDLK_KP_HASH
K_KP_SPACE = lib.SDLK_KP_SPACE
K_KP_AT = lib.SDLK_KP_AT
K_KP_EXCLAM = lib.SDLK_KP_EXCLAM
K_KP_MEMSTORE = lib.SDLK_KP_MEMSTORE
K_KP_MEMRECALL = lib.SDLK_KP_MEMRECALL
K_KP_MEMCLEAR = lib.SDLK_KP_MEMCLEAR
K_KP_MEMADD = lib.SDLK_KP_MEMADD
K_KP_MEMSUBTRACT = lib.SDLK_KP_MEMSUBTRACT
K_KP_MEMMULTIPLY = lib.SDLK_KP_MEMMULTIPLY
K_KP_MEMDIVIDE = lib.SDLK_KP_MEMDIVIDE
K_KP_PLUSMINUS = lib.SDLK_KP_PLUSMINUS
K_KP_CLEAR = lib.SDLK_KP_CLEAR
K_KP_CLEARENTRY = lib.SDLK_KP_CLEARENTRY
K_KP_BINARY = lib.SDLK_KP_BINARY
K_KP_OCTAL = lib.SDLK_KP_OCTAL
K_KP_DECIMAL = lib.SDLK_KP_DECIMAL
K_KP_HEXADECIMAL = lib.SDLK_KP_HEXADECIMAL
K_LCTRL = lib.SDLK_LCTRL
K_LSHIFT = lib.SDLK_LSHIFT
K_LALT = lib.SDLK_LALT
K_LGUI = lib.SDLK_LGUI
K_RCTRL = lib.SDLK_RCTRL
K_RSHIFT = lib.SDLK_RSHIFT
K_RALT = lib.SDLK_RALT
K_RGUI = lib.SDLK_RGUI
K_MODE = lib.SDLK_MODE
K_AUDIONEXT = lib.SDLK_AUDIONEXT
K_AUDIOPREV = lib.SDLK_AUDIOPREV
K_AUDIOSTOP = lib.SDLK_AUDIOSTOP
K_AUDIOPLAY = lib.SDLK_AUDIOPLAY
K_AUDIOMUTE = lib.SDLK_AUDIOMUTE
K_MEDIASELECT = lib.SDLK_MEDIASELECT
K_WWW = lib.SDLK_WWW
K_MAIL = lib.SDLK_MAIL
K_CALCULATOR = lib.SDLK_CALCULATOR
K_COMPUTER = lib.SDLK_COMPUTER
K_AC_SEARCH = lib.SDLK_AC_SEARCH
K_AC_HOME = lib.SDLK_AC_HOME
K_AC_BACK = lib.SDLK_AC_BACK
K_AC_FORWARD = lib.SDLK_AC_FORWARD
K_AC_STOP = lib.SDLK_AC_STOP
K_AC_REFRESH = lib.SDLK_AC_REFRESH
K_AC_BOOKMARKS = lib.SDLK_AC_BOOKMARKS
K_BRIGHTNESSDOWN = lib.SDLK_BRIGHTNESSDOWN
K_BRIGHTNESSUP = lib.SDLK_BRIGHTNESSUP
K_DISPLAYSWITCH = lib.SDLK_DISPLAYSWITCH
K_KBDILLUMTOGGLE = lib.SDLK_KBDILLUMTOGGLE
K_KBDILLUMDOWN = lib.SDLK_KBDILLUMDOWN
K_KBDILLUMUP = lib.SDLK_KBDILLUMUP
K_EJECT = lib.SDLK_EJECT
K_SLEEP = lib.SDLK_SLEEP

LOG_CATEGORY_APPLICATION = lib.SDL_LOG_CATEGORY_APPLICATION
LOG_CATEGORY_ERROR = lib.SDL_LOG_CATEGORY_ERROR
LOG_CATEGORY_ASSERT = lib.SDL_LOG_CATEGORY_ASSERT
LOG_CATEGORY_SYSTEM = lib.SDL_LOG_CATEGORY_SYSTEM
LOG_CATEGORY_AUDIO = lib.SDL_LOG_CATEGORY_AUDIO
LOG_CATEGORY_VIDEO = lib.SDL_LOG_CATEGORY_VIDEO
LOG_CATEGORY_RENDER = lib.SDL_LOG_CATEGORY_RENDER
LOG_CATEGORY_INPUT = lib.SDL_LOG_CATEGORY_INPUT
LOG_CATEGORY_TEST = lib.SDL_LOG_CATEGORY_TEST
LOG_CATEGORY_RESERVED1 = lib.SDL_LOG_CATEGORY_RESERVED1
LOG_CATEGORY_RESERVED2 = lib.SDL_LOG_CATEGORY_RESERVED2
LOG_CATEGORY_RESERVED3 = lib.SDL_LOG_CATEGORY_RESERVED3
LOG_CATEGORY_RESERVED4 = lib.SDL_LOG_CATEGORY_RESERVED4
LOG_CATEGORY_RESERVED5 = lib.SDL_LOG_CATEGORY_RESERVED5
LOG_CATEGORY_RESERVED6 = lib.SDL_LOG_CATEGORY_RESERVED6
LOG_CATEGORY_RESERVED7 = lib.SDL_LOG_CATEGORY_RESERVED7
LOG_CATEGORY_RESERVED8 = lib.SDL_LOG_CATEGORY_RESERVED8
LOG_CATEGORY_RESERVED9 = lib.SDL_LOG_CATEGORY_RESERVED9
LOG_CATEGORY_RESERVED10 = lib.SDL_LOG_CATEGORY_RESERVED10
LOG_CATEGORY_CUSTOM = lib.SDL_LOG_CATEGORY_CUSTOM

PIXELTYPE_UNKNOWN = lib.SDL_PIXELTYPE_UNKNOWN
PIXELTYPE_INDEX1 = lib.SDL_PIXELTYPE_INDEX1
PIXELTYPE_INDEX4 = lib.SDL_PIXELTYPE_INDEX4
PIXELTYPE_INDEX8 = lib.SDL_PIXELTYPE_INDEX8
PIXELTYPE_PACKED8 = lib.SDL_PIXELTYPE_PACKED8
PIXELTYPE_PACKED16 = lib.SDL_PIXELTYPE_PACKED16
PIXELTYPE_PACKED32 = lib.SDL_PIXELTYPE_PACKED32
PIXELTYPE_ARRAYU8 = lib.SDL_PIXELTYPE_ARRAYU8
PIXELTYPE_ARRAYU16 = lib.SDL_PIXELTYPE_ARRAYU16
PIXELTYPE_ARRAYU32 = lib.SDL_PIXELTYPE_ARRAYU32
PIXELTYPE_ARRAYF16 = lib.SDL_PIXELTYPE_ARRAYF16
PIXELTYPE_ARRAYF32 = lib.SDL_PIXELTYPE_ARRAYF32

BITMAPORDER_NONE = lib.SDL_BITMAPORDER_NONE
BITMAPORDER_4321 = lib.SDL_BITMAPORDER_4321
BITMAPORDER_1234 = lib.SDL_BITMAPORDER_1234

PACKEDORDER_NONE = lib.SDL_PACKEDORDER_NONE
PACKEDORDER_XRGB = lib.SDL_PACKEDORDER_XRGB
PACKEDORDER_RGBX = lib.SDL_PACKEDORDER_RGBX
PACKEDORDER_ARGB = lib.SDL_PACKEDORDER_ARGB
PACKEDORDER_RGBA = lib.SDL_PACKEDORDER_RGBA
PACKEDORDER_XBGR = lib.SDL_PACKEDORDER_XBGR
PACKEDORDER_BGRX = lib.SDL_PACKEDORDER_BGRX
PACKEDORDER_ABGR = lib.SDL_PACKEDORDER_ABGR
PACKEDORDER_BGRA = lib.SDL_PACKEDORDER_BGRA

ARRAYORDER_NONE = lib.SDL_ARRAYORDER_NONE
ARRAYORDER_RGB = lib.SDL_ARRAYORDER_RGB
ARRAYORDER_RGBA = lib.SDL_ARRAYORDER_RGBA
ARRAYORDER_ARGB = lib.SDL_ARRAYORDER_ARGB
ARRAYORDER_BGR = lib.SDL_ARRAYORDER_BGR
ARRAYORDER_BGRA = lib.SDL_ARRAYORDER_BGRA
ARRAYORDER_ABGR = lib.SDL_ARRAYORDER_ABGR

PACKEDLAYOUT_NONE = lib.SDL_PACKEDLAYOUT_NONE
PACKEDLAYOUT_332 = lib.SDL_PACKEDLAYOUT_332
PACKEDLAYOUT_4444 = lib.SDL_PACKEDLAYOUT_4444
PACKEDLAYOUT_1555 = lib.SDL_PACKEDLAYOUT_1555
PACKEDLAYOUT_5551 = lib.SDL_PACKEDLAYOUT_5551
PACKEDLAYOUT_565 = lib.SDL_PACKEDLAYOUT_565
PACKEDLAYOUT_8888 = lib.SDL_PACKEDLAYOUT_8888
PACKEDLAYOUT_2101010 = lib.SDL_PACKEDLAYOUT_2101010
PACKEDLAYOUT_1010102 = lib.SDL_PACKEDLAYOUT_1010102

AUDIO_STOPPED = lib.SDL_AUDIO_STOPPED
AUDIO_PLAYING = lib.SDL_AUDIO_PLAYING
AUDIO_PAUSED = lib.SDL_AUDIO_PAUSED

BLENDMODE_NONE = lib.SDL_BLENDMODE_NONE
BLENDMODE_BLEND = lib.SDL_BLENDMODE_BLEND
BLENDMODE_ADD = lib.SDL_BLENDMODE_ADD
BLENDMODE_MOD = lib.SDL_BLENDMODE_MOD

FIRSTEVENT = lib.SDL_FIRSTEVENT
QUIT = lib.SDL_QUIT
APP_TERMINATING = lib.SDL_APP_TERMINATING
APP_LOWMEMORY = lib.SDL_APP_LOWMEMORY
APP_WILLENTERBACKGROUND = lib.SDL_APP_WILLENTERBACKGROUND
APP_DIDENTERBACKGROUND = lib.SDL_APP_DIDENTERBACKGROUND
APP_WILLENTERFOREGROUND = lib.SDL_APP_WILLENTERFOREGROUND
APP_DIDENTERFOREGROUND = lib.SDL_APP_DIDENTERFOREGROUND
WINDOWEVENT = lib.SDL_WINDOWEVENT
SYSWMEVENT = lib.SDL_SYSWMEVENT
KEYDOWN = lib.SDL_KEYDOWN
KEYUP = lib.SDL_KEYUP
TEXTEDITING = lib.SDL_TEXTEDITING
TEXTINPUT = lib.SDL_TEXTINPUT
MOUSEMOTION = lib.SDL_MOUSEMOTION
MOUSEBUTTONDOWN = lib.SDL_MOUSEBUTTONDOWN
MOUSEBUTTONUP = lib.SDL_MOUSEBUTTONUP
MOUSEWHEEL = lib.SDL_MOUSEWHEEL
JOYAXISMOTION = lib.SDL_JOYAXISMOTION
JOYBALLMOTION = lib.SDL_JOYBALLMOTION
JOYHATMOTION = lib.SDL_JOYHATMOTION
JOYBUTTONDOWN = lib.SDL_JOYBUTTONDOWN
JOYBUTTONUP = lib.SDL_JOYBUTTONUP
JOYDEVICEADDED = lib.SDL_JOYDEVICEADDED
JOYDEVICEREMOVED = lib.SDL_JOYDEVICEREMOVED
CONTROLLERAXISMOTION = lib.SDL_CONTROLLERAXISMOTION
CONTROLLERBUTTONDOWN = lib.SDL_CONTROLLERBUTTONDOWN
CONTROLLERBUTTONUP = lib.SDL_CONTROLLERBUTTONUP
CONTROLLERDEVICEADDED = lib.SDL_CONTROLLERDEVICEADDED
CONTROLLERDEVICEREMOVED = lib.SDL_CONTROLLERDEVICEREMOVED
CONTROLLERDEVICEREMAPPED = lib.SDL_CONTROLLERDEVICEREMAPPED
FINGERDOWN = lib.SDL_FINGERDOWN
FINGERUP = lib.SDL_FINGERUP
FINGERMOTION = lib.SDL_FINGERMOTION
DOLLARGESTURE = lib.SDL_DOLLARGESTURE
DOLLARRECORD = lib.SDL_DOLLARRECORD
MULTIGESTURE = lib.SDL_MULTIGESTURE
CLIPBOARDUPDATE = lib.SDL_CLIPBOARDUPDATE
DROPFILE = lib.SDL_DROPFILE
RENDER_TARGETS_RESET = lib.SDL_RENDER_TARGETS_RESET
USEREVENT = lib.SDL_USEREVENT
LASTEVENT = lib.SDL_LASTEVENT

GL_RED_SIZE = lib.SDL_GL_RED_SIZE
GL_GREEN_SIZE = lib.SDL_GL_GREEN_SIZE
GL_BLUE_SIZE = lib.SDL_GL_BLUE_SIZE
GL_ALPHA_SIZE = lib.SDL_GL_ALPHA_SIZE
GL_BUFFER_SIZE = lib.SDL_GL_BUFFER_SIZE
GL_DOUBLEBUFFER = lib.SDL_GL_DOUBLEBUFFER
GL_DEPTH_SIZE = lib.SDL_GL_DEPTH_SIZE
GL_STENCIL_SIZE = lib.SDL_GL_STENCIL_SIZE
GL_ACCUM_RED_SIZE = lib.SDL_GL_ACCUM_RED_SIZE
GL_ACCUM_GREEN_SIZE = lib.SDL_GL_ACCUM_GREEN_SIZE
GL_ACCUM_BLUE_SIZE = lib.SDL_GL_ACCUM_BLUE_SIZE
GL_ACCUM_ALPHA_SIZE = lib.SDL_GL_ACCUM_ALPHA_SIZE
GL_STEREO = lib.SDL_GL_STEREO
GL_MULTISAMPLEBUFFERS = lib.SDL_GL_MULTISAMPLEBUFFERS
GL_MULTISAMPLESAMPLES = lib.SDL_GL_MULTISAMPLESAMPLES
GL_ACCELERATED_VISUAL = lib.SDL_GL_ACCELERATED_VISUAL
GL_RETAINED_BACKING = lib.SDL_GL_RETAINED_BACKING
GL_CONTEXT_MAJOR_VERSION = lib.SDL_GL_CONTEXT_MAJOR_VERSION
GL_CONTEXT_MINOR_VERSION = lib.SDL_GL_CONTEXT_MINOR_VERSION
GL_CONTEXT_EGL = lib.SDL_GL_CONTEXT_EGL
GL_CONTEXT_FLAGS = lib.SDL_GL_CONTEXT_FLAGS
GL_CONTEXT_PROFILE_MASK = lib.SDL_GL_CONTEXT_PROFILE_MASK
GL_SHARE_WITH_CURRENT_CONTEXT = lib.SDL_GL_SHARE_WITH_CURRENT_CONTEXT
GL_FRAMEBUFFER_SRGB_CAPABLE = lib.SDL_GL_FRAMEBUFFER_SRGB_CAPABLE

GL_CONTEXT_DEBUG_FLAG = lib.SDL_GL_CONTEXT_DEBUG_FLAG
GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = lib.SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG
GL_CONTEXT_ROBUST_ACCESS_FLAG = lib.SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG
GL_CONTEXT_RESET_ISOLATION_FLAG = lib.SDL_GL_CONTEXT_RESET_ISOLATION_FLAG

GL_CONTEXT_PROFILE_CORE = lib.SDL_GL_CONTEXT_PROFILE_CORE
GL_CONTEXT_PROFILE_COMPATIBILITY = lib.SDL_GL_CONTEXT_PROFILE_COMPATIBILITY
GL_CONTEXT_PROFILE_ES = lib.SDL_GL_CONTEXT_PROFILE_ES

CONTROLLER_AXIS_INVALID = lib.SDL_CONTROLLER_AXIS_INVALID
CONTROLLER_AXIS_LEFTX = lib.SDL_CONTROLLER_AXIS_LEFTX
CONTROLLER_AXIS_LEFTY = lib.SDL_CONTROLLER_AXIS_LEFTY
CONTROLLER_AXIS_RIGHTX = lib.SDL_CONTROLLER_AXIS_RIGHTX
CONTROLLER_AXIS_RIGHTY = lib.SDL_CONTROLLER_AXIS_RIGHTY
CONTROLLER_AXIS_TRIGGERLEFT = lib.SDL_CONTROLLER_AXIS_TRIGGERLEFT
CONTROLLER_AXIS_TRIGGERRIGHT = lib.SDL_CONTROLLER_AXIS_TRIGGERRIGHT
CONTROLLER_AXIS_MAX = lib.SDL_CONTROLLER_AXIS_MAX

CONTROLLER_BINDTYPE_NONE = lib.SDL_CONTROLLER_BINDTYPE_NONE
CONTROLLER_BINDTYPE_BUTTON = lib.SDL_CONTROLLER_BINDTYPE_BUTTON
CONTROLLER_BINDTYPE_AXIS = lib.SDL_CONTROLLER_BINDTYPE_AXIS
CONTROLLER_BINDTYPE_HAT = lib.SDL_CONTROLLER_BINDTYPE_HAT

CONTROLLER_BUTTON_INVALID = lib.SDL_CONTROLLER_BUTTON_INVALID
CONTROLLER_BUTTON_A = lib.SDL_CONTROLLER_BUTTON_A
CONTROLLER_BUTTON_B = lib.SDL_CONTROLLER_BUTTON_B
CONTROLLER_BUTTON_X = lib.SDL_CONTROLLER_BUTTON_X
CONTROLLER_BUTTON_Y = lib.SDL_CONTROLLER_BUTTON_Y
CONTROLLER_BUTTON_BACK = lib.SDL_CONTROLLER_BUTTON_BACK
CONTROLLER_BUTTON_GUIDE = lib.SDL_CONTROLLER_BUTTON_GUIDE
CONTROLLER_BUTTON_START = lib.SDL_CONTROLLER_BUTTON_START
CONTROLLER_BUTTON_LEFTSTICK = lib.SDL_CONTROLLER_BUTTON_LEFTSTICK
CONTROLLER_BUTTON_RIGHTSTICK = lib.SDL_CONTROLLER_BUTTON_RIGHTSTICK
CONTROLLER_BUTTON_LEFTSHOULDER = lib.SDL_CONTROLLER_BUTTON_LEFTSHOULDER
CONTROLLER_BUTTON_RIGHTSHOULDER = lib.SDL_CONTROLLER_BUTTON_RIGHTSHOULDER
CONTROLLER_BUTTON_DPAD_UP = lib.SDL_CONTROLLER_BUTTON_DPAD_UP
CONTROLLER_BUTTON_DPAD_DOWN = lib.SDL_CONTROLLER_BUTTON_DPAD_DOWN
CONTROLLER_BUTTON_DPAD_LEFT = lib.SDL_CONTROLLER_BUTTON_DPAD_LEFT
CONTROLLER_BUTTON_DPAD_RIGHT = lib.SDL_CONTROLLER_BUTTON_DPAD_RIGHT
CONTROLLER_BUTTON_MAX = lib.SDL_CONTROLLER_BUTTON_MAX

HINT_DEFAULT = lib.SDL_HINT_DEFAULT
HINT_NORMAL = lib.SDL_HINT_NORMAL
HINT_OVERRIDE = lib.SDL_HINT_OVERRIDE

KMOD_NONE = lib.KMOD_NONE
KMOD_LSHIFT = lib.KMOD_LSHIFT
KMOD_RSHIFT = lib.KMOD_RSHIFT
KMOD_LCTRL = lib.KMOD_LCTRL
KMOD_RCTRL = lib.KMOD_RCTRL
KMOD_LALT = lib.KMOD_LALT
KMOD_RALT = lib.KMOD_RALT
KMOD_LGUI = lib.KMOD_LGUI
KMOD_RGUI = lib.KMOD_RGUI
KMOD_NUM = lib.KMOD_NUM
KMOD_CAPS = lib.KMOD_CAPS
KMOD_MODE = lib.KMOD_MODE
KMOD_RESERVED = lib.KMOD_RESERVED

LOG_PRIORITY_VERBOSE = lib.SDL_LOG_PRIORITY_VERBOSE
LOG_PRIORITY_DEBUG = lib.SDL_LOG_PRIORITY_DEBUG
LOG_PRIORITY_INFO = lib.SDL_LOG_PRIORITY_INFO
LOG_PRIORITY_WARN = lib.SDL_LOG_PRIORITY_WARN
LOG_PRIORITY_ERROR = lib.SDL_LOG_PRIORITY_ERROR
LOG_PRIORITY_CRITICAL = lib.SDL_LOG_PRIORITY_CRITICAL
NUM_LOG_PRIORITIES = lib.SDL_NUM_LOG_PRIORITIES

MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = lib.SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT
MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = lib.SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT

MESSAGEBOX_COLOR_BACKGROUND = lib.SDL_MESSAGEBOX_COLOR_BACKGROUND
MESSAGEBOX_COLOR_TEXT = lib.SDL_MESSAGEBOX_COLOR_TEXT
MESSAGEBOX_COLOR_BUTTON_BORDER = lib.SDL_MESSAGEBOX_COLOR_BUTTON_BORDER
MESSAGEBOX_COLOR_BUTTON_BACKGROUND = lib.SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND
MESSAGEBOX_COLOR_BUTTON_SELECTED = lib.SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED
MESSAGEBOX_COLOR_MAX = lib.SDL_MESSAGEBOX_COLOR_MAX

MESSAGEBOX_ERROR = lib.SDL_MESSAGEBOX_ERROR
MESSAGEBOX_WARNING = lib.SDL_MESSAGEBOX_WARNING
MESSAGEBOX_INFORMATION = lib.SDL_MESSAGEBOX_INFORMATION

POWERSTATE_UNKNOWN = lib.SDL_POWERSTATE_UNKNOWN
POWERSTATE_ON_BATTERY = lib.SDL_POWERSTATE_ON_BATTERY
POWERSTATE_NO_BATTERY = lib.SDL_POWERSTATE_NO_BATTERY
POWERSTATE_CHARGING = lib.SDL_POWERSTATE_CHARGING
POWERSTATE_CHARGED = lib.SDL_POWERSTATE_CHARGED

RENDERER_SOFTWARE = lib.SDL_RENDERER_SOFTWARE
RENDERER_ACCELERATED = lib.SDL_RENDERER_ACCELERATED
RENDERER_PRESENTVSYNC = lib.SDL_RENDERER_PRESENTVSYNC
RENDERER_TARGETTEXTURE = lib.SDL_RENDERER_TARGETTEXTURE

FLIP_NONE = lib.SDL_FLIP_NONE
FLIP_HORIZONTAL = lib.SDL_FLIP_HORIZONTAL
FLIP_VERTICAL = lib.SDL_FLIP_VERTICAL

SCANCODE_UNKNOWN = lib.SDL_SCANCODE_UNKNOWN
SCANCODE_A = lib.SDL_SCANCODE_A
SCANCODE_B = lib.SDL_SCANCODE_B
SCANCODE_C = lib.SDL_SCANCODE_C
SCANCODE_D = lib.SDL_SCANCODE_D
SCANCODE_E = lib.SDL_SCANCODE_E
SCANCODE_F = lib.SDL_SCANCODE_F
SCANCODE_G = lib.SDL_SCANCODE_G
SCANCODE_H = lib.SDL_SCANCODE_H
SCANCODE_I = lib.SDL_SCANCODE_I
SCANCODE_J = lib.SDL_SCANCODE_J
SCANCODE_K = lib.SDL_SCANCODE_K
SCANCODE_L = lib.SDL_SCANCODE_L
SCANCODE_M = lib.SDL_SCANCODE_M
SCANCODE_N = lib.SDL_SCANCODE_N
SCANCODE_O = lib.SDL_SCANCODE_O
SCANCODE_P = lib.SDL_SCANCODE_P
SCANCODE_Q = lib.SDL_SCANCODE_Q
SCANCODE_R = lib.SDL_SCANCODE_R
SCANCODE_S = lib.SDL_SCANCODE_S
SCANCODE_T = lib.SDL_SCANCODE_T
SCANCODE_U = lib.SDL_SCANCODE_U
SCANCODE_V = lib.SDL_SCANCODE_V
SCANCODE_W = lib.SDL_SCANCODE_W
SCANCODE_X = lib.SDL_SCANCODE_X
SCANCODE_Y = lib.SDL_SCANCODE_Y
SCANCODE_Z = lib.SDL_SCANCODE_Z
SCANCODE_1 = lib.SDL_SCANCODE_1
SCANCODE_2 = lib.SDL_SCANCODE_2
SCANCODE_3 = lib.SDL_SCANCODE_3
SCANCODE_4 = lib.SDL_SCANCODE_4
SCANCODE_5 = lib.SDL_SCANCODE_5
SCANCODE_6 = lib.SDL_SCANCODE_6
SCANCODE_7 = lib.SDL_SCANCODE_7
SCANCODE_8 = lib.SDL_SCANCODE_8
SCANCODE_9 = lib.SDL_SCANCODE_9
SCANCODE_0 = lib.SDL_SCANCODE_0
SCANCODE_RETURN = lib.SDL_SCANCODE_RETURN
SCANCODE_ESCAPE = lib.SDL_SCANCODE_ESCAPE
SCANCODE_BACKSPACE = lib.SDL_SCANCODE_BACKSPACE
SCANCODE_TAB = lib.SDL_SCANCODE_TAB
SCANCODE_SPACE = lib.SDL_SCANCODE_SPACE
SCANCODE_MINUS = lib.SDL_SCANCODE_MINUS
SCANCODE_EQUALS = lib.SDL_SCANCODE_EQUALS
SCANCODE_LEFTBRACKET = lib.SDL_SCANCODE_LEFTBRACKET
SCANCODE_RIGHTBRACKET = lib.SDL_SCANCODE_RIGHTBRACKET
SCANCODE_BACKSLASH = lib.SDL_SCANCODE_BACKSLASH
SCANCODE_NONUSHASH = lib.SDL_SCANCODE_NONUSHASH
SCANCODE_SEMICOLON = lib.SDL_SCANCODE_SEMICOLON
SCANCODE_APOSTROPHE = lib.SDL_SCANCODE_APOSTROPHE
SCANCODE_GRAVE = lib.SDL_SCANCODE_GRAVE
SCANCODE_COMMA = lib.SDL_SCANCODE_COMMA
SCANCODE_PERIOD = lib.SDL_SCANCODE_PERIOD
SCANCODE_SLASH = lib.SDL_SCANCODE_SLASH
SCANCODE_CAPSLOCK = lib.SDL_SCANCODE_CAPSLOCK
SCANCODE_F1 = lib.SDL_SCANCODE_F1
SCANCODE_F2 = lib.SDL_SCANCODE_F2
SCANCODE_F3 = lib.SDL_SCANCODE_F3
SCANCODE_F4 = lib.SDL_SCANCODE_F4
SCANCODE_F5 = lib.SDL_SCANCODE_F5
SCANCODE_F6 = lib.SDL_SCANCODE_F6
SCANCODE_F7 = lib.SDL_SCANCODE_F7
SCANCODE_F8 = lib.SDL_SCANCODE_F8
SCANCODE_F9 = lib.SDL_SCANCODE_F9
SCANCODE_F10 = lib.SDL_SCANCODE_F10
SCANCODE_F11 = lib.SDL_SCANCODE_F11
SCANCODE_F12 = lib.SDL_SCANCODE_F12
SCANCODE_PRINTSCREEN = lib.SDL_SCANCODE_PRINTSCREEN
SCANCODE_SCROLLLOCK = lib.SDL_SCANCODE_SCROLLLOCK
SCANCODE_PAUSE = lib.SDL_SCANCODE_PAUSE
SCANCODE_INSERT = lib.SDL_SCANCODE_INSERT
SCANCODE_HOME = lib.SDL_SCANCODE_HOME
SCANCODE_PAGEUP = lib.SDL_SCANCODE_PAGEUP
SCANCODE_DELETE = lib.SDL_SCANCODE_DELETE
SCANCODE_END = lib.SDL_SCANCODE_END
SCANCODE_PAGEDOWN = lib.SDL_SCANCODE_PAGEDOWN
SCANCODE_RIGHT = lib.SDL_SCANCODE_RIGHT
SCANCODE_LEFT = lib.SDL_SCANCODE_LEFT
SCANCODE_DOWN = lib.SDL_SCANCODE_DOWN
SCANCODE_UP = lib.SDL_SCANCODE_UP
SCANCODE_NUMLOCKCLEAR = lib.SDL_SCANCODE_NUMLOCKCLEAR
SCANCODE_KP_DIVIDE = lib.SDL_SCANCODE_KP_DIVIDE
SCANCODE_KP_MULTIPLY = lib.SDL_SCANCODE_KP_MULTIPLY
SCANCODE_KP_MINUS = lib.SDL_SCANCODE_KP_MINUS
SCANCODE_KP_PLUS = lib.SDL_SCANCODE_KP_PLUS
SCANCODE_KP_ENTER = lib.SDL_SCANCODE_KP_ENTER
SCANCODE_KP_1 = lib.SDL_SCANCODE_KP_1
SCANCODE_KP_2 = lib.SDL_SCANCODE_KP_2
SCANCODE_KP_3 = lib.SDL_SCANCODE_KP_3
SCANCODE_KP_4 = lib.SDL_SCANCODE_KP_4
SCANCODE_KP_5 = lib.SDL_SCANCODE_KP_5
SCANCODE_KP_6 = lib.SDL_SCANCODE_KP_6
SCANCODE_KP_7 = lib.SDL_SCANCODE_KP_7
SCANCODE_KP_8 = lib.SDL_SCANCODE_KP_8
SCANCODE_KP_9 = lib.SDL_SCANCODE_KP_9
SCANCODE_KP_0 = lib.SDL_SCANCODE_KP_0
SCANCODE_KP_PERIOD = lib.SDL_SCANCODE_KP_PERIOD
SCANCODE_NONUSBACKSLASH = lib.SDL_SCANCODE_NONUSBACKSLASH
SCANCODE_APPLICATION = lib.SDL_SCANCODE_APPLICATION
SCANCODE_POWER = lib.SDL_SCANCODE_POWER
SCANCODE_KP_EQUALS = lib.SDL_SCANCODE_KP_EQUALS
SCANCODE_F13 = lib.SDL_SCANCODE_F13
SCANCODE_F14 = lib.SDL_SCANCODE_F14
SCANCODE_F15 = lib.SDL_SCANCODE_F15
SCANCODE_F16 = lib.SDL_SCANCODE_F16
SCANCODE_F17 = lib.SDL_SCANCODE_F17
SCANCODE_F18 = lib.SDL_SCANCODE_F18
SCANCODE_F19 = lib.SDL_SCANCODE_F19
SCANCODE_F20 = lib.SDL_SCANCODE_F20
SCANCODE_F21 = lib.SDL_SCANCODE_F21
SCANCODE_F22 = lib.SDL_SCANCODE_F22
SCANCODE_F23 = lib.SDL_SCANCODE_F23
SCANCODE_F24 = lib.SDL_SCANCODE_F24
SCANCODE_EXECUTE = lib.SDL_SCANCODE_EXECUTE
SCANCODE_HELP = lib.SDL_SCANCODE_HELP
SCANCODE_MENU = lib.SDL_SCANCODE_MENU
SCANCODE_SELECT = lib.SDL_SCANCODE_SELECT
SCANCODE_STOP = lib.SDL_SCANCODE_STOP
SCANCODE_AGAIN = lib.SDL_SCANCODE_AGAIN
SCANCODE_UNDO = lib.SDL_SCANCODE_UNDO
SCANCODE_CUT = lib.SDL_SCANCODE_CUT
SCANCODE_COPY = lib.SDL_SCANCODE_COPY
SCANCODE_PASTE = lib.SDL_SCANCODE_PASTE
SCANCODE_FIND = lib.SDL_SCANCODE_FIND
SCANCODE_MUTE = lib.SDL_SCANCODE_MUTE
SCANCODE_VOLUMEUP = lib.SDL_SCANCODE_VOLUMEUP
SCANCODE_VOLUMEDOWN = lib.SDL_SCANCODE_VOLUMEDOWN
SCANCODE_KP_COMMA = lib.SDL_SCANCODE_KP_COMMA
SCANCODE_KP_EQUALSAS400 = lib.SDL_SCANCODE_KP_EQUALSAS400
SCANCODE_INTERNATIONAL1 = lib.SDL_SCANCODE_INTERNATIONAL1
SCANCODE_INTERNATIONAL2 = lib.SDL_SCANCODE_INTERNATIONAL2
SCANCODE_INTERNATIONAL3 = lib.SDL_SCANCODE_INTERNATIONAL3
SCANCODE_INTERNATIONAL4 = lib.SDL_SCANCODE_INTERNATIONAL4
SCANCODE_INTERNATIONAL5 = lib.SDL_SCANCODE_INTERNATIONAL5
SCANCODE_INTERNATIONAL6 = lib.SDL_SCANCODE_INTERNATIONAL6
SCANCODE_INTERNATIONAL7 = lib.SDL_SCANCODE_INTERNATIONAL7
SCANCODE_INTERNATIONAL8 = lib.SDL_SCANCODE_INTERNATIONAL8
SCANCODE_INTERNATIONAL9 = lib.SDL_SCANCODE_INTERNATIONAL9
SCANCODE_LANG1 = lib.SDL_SCANCODE_LANG1
SCANCODE_LANG2 = lib.SDL_SCANCODE_LANG2
SCANCODE_LANG3 = lib.SDL_SCANCODE_LANG3
SCANCODE_LANG4 = lib.SDL_SCANCODE_LANG4
SCANCODE_LANG5 = lib.SDL_SCANCODE_LANG5
SCANCODE_LANG6 = lib.SDL_SCANCODE_LANG6
SCANCODE_LANG7 = lib.SDL_SCANCODE_LANG7
SCANCODE_LANG8 = lib.SDL_SCANCODE_LANG8
SCANCODE_LANG9 = lib.SDL_SCANCODE_LANG9
SCANCODE_ALTERASE = lib.SDL_SCANCODE_ALTERASE
SCANCODE_SYSREQ = lib.SDL_SCANCODE_SYSREQ
SCANCODE_CANCEL = lib.SDL_SCANCODE_CANCEL
SCANCODE_CLEAR = lib.SDL_SCANCODE_CLEAR
SCANCODE_PRIOR = lib.SDL_SCANCODE_PRIOR
SCANCODE_RETURN2 = lib.SDL_SCANCODE_RETURN2
SCANCODE_SEPARATOR = lib.SDL_SCANCODE_SEPARATOR
SCANCODE_OUT = lib.SDL_SCANCODE_OUT
SCANCODE_OPER = lib.SDL_SCANCODE_OPER
SCANCODE_CLEARAGAIN = lib.SDL_SCANCODE_CLEARAGAIN
SCANCODE_CRSEL = lib.SDL_SCANCODE_CRSEL
SCANCODE_EXSEL = lib.SDL_SCANCODE_EXSEL
SCANCODE_KP_00 = lib.SDL_SCANCODE_KP_00
SCANCODE_KP_000 = lib.SDL_SCANCODE_KP_000
SCANCODE_THOUSANDSSEPARATOR = lib.SDL_SCANCODE_THOUSANDSSEPARATOR
SCANCODE_DECIMALSEPARATOR = lib.SDL_SCANCODE_DECIMALSEPARATOR
SCANCODE_CURRENCYUNIT = lib.SDL_SCANCODE_CURRENCYUNIT
SCANCODE_CURRENCYSUBUNIT = lib.SDL_SCANCODE_CURRENCYSUBUNIT
SCANCODE_KP_LEFTPAREN = lib.SDL_SCANCODE_KP_LEFTPAREN
SCANCODE_KP_RIGHTPAREN = lib.SDL_SCANCODE_KP_RIGHTPAREN
SCANCODE_KP_LEFTBRACE = lib.SDL_SCANCODE_KP_LEFTBRACE
SCANCODE_KP_RIGHTBRACE = lib.SDL_SCANCODE_KP_RIGHTBRACE
SCANCODE_KP_TAB = lib.SDL_SCANCODE_KP_TAB
SCANCODE_KP_BACKSPACE = lib.SDL_SCANCODE_KP_BACKSPACE
SCANCODE_KP_A = lib.SDL_SCANCODE_KP_A
SCANCODE_KP_B = lib.SDL_SCANCODE_KP_B
SCANCODE_KP_C = lib.SDL_SCANCODE_KP_C
SCANCODE_KP_D = lib.SDL_SCANCODE_KP_D
SCANCODE_KP_E = lib.SDL_SCANCODE_KP_E
SCANCODE_KP_F = lib.SDL_SCANCODE_KP_F
SCANCODE_KP_XOR = lib.SDL_SCANCODE_KP_XOR
SCANCODE_KP_POWER = lib.SDL_SCANCODE_KP_POWER
SCANCODE_KP_PERCENT = lib.SDL_SCANCODE_KP_PERCENT
SCANCODE_KP_LESS = lib.SDL_SCANCODE_KP_LESS
SCANCODE_KP_GREATER = lib.SDL_SCANCODE_KP_GREATER
SCANCODE_KP_AMPERSAND = lib.SDL_SCANCODE_KP_AMPERSAND
SCANCODE_KP_DBLAMPERSAND = lib.SDL_SCANCODE_KP_DBLAMPERSAND
SCANCODE_KP_VERTICALBAR = lib.SDL_SCANCODE_KP_VERTICALBAR
SCANCODE_KP_DBLVERTICALBAR = lib.SDL_SCANCODE_KP_DBLVERTICALBAR
SCANCODE_KP_COLON = lib.SDL_SCANCODE_KP_COLON
SCANCODE_KP_HASH = lib.SDL_SCANCODE_KP_HASH
SCANCODE_KP_SPACE = lib.SDL_SCANCODE_KP_SPACE
SCANCODE_KP_AT = lib.SDL_SCANCODE_KP_AT
SCANCODE_KP_EXCLAM = lib.SDL_SCANCODE_KP_EXCLAM
SCANCODE_KP_MEMSTORE = lib.SDL_SCANCODE_KP_MEMSTORE
SCANCODE_KP_MEMRECALL = lib.SDL_SCANCODE_KP_MEMRECALL
SCANCODE_KP_MEMCLEAR = lib.SDL_SCANCODE_KP_MEMCLEAR
SCANCODE_KP_MEMADD = lib.SDL_SCANCODE_KP_MEMADD
SCANCODE_KP_MEMSUBTRACT = lib.SDL_SCANCODE_KP_MEMSUBTRACT
SCANCODE_KP_MEMMULTIPLY = lib.SDL_SCANCODE_KP_MEMMULTIPLY
SCANCODE_KP_MEMDIVIDE = lib.SDL_SCANCODE_KP_MEMDIVIDE
SCANCODE_KP_PLUSMINUS = lib.SDL_SCANCODE_KP_PLUSMINUS
SCANCODE_KP_CLEAR = lib.SDL_SCANCODE_KP_CLEAR
SCANCODE_KP_CLEARENTRY = lib.SDL_SCANCODE_KP_CLEARENTRY
SCANCODE_KP_BINARY = lib.SDL_SCANCODE_KP_BINARY
SCANCODE_KP_OCTAL = lib.SDL_SCANCODE_KP_OCTAL
SCANCODE_KP_DECIMAL = lib.SDL_SCANCODE_KP_DECIMAL
SCANCODE_KP_HEXADECIMAL = lib.SDL_SCANCODE_KP_HEXADECIMAL
SCANCODE_LCTRL = lib.SDL_SCANCODE_LCTRL
SCANCODE_LSHIFT = lib.SDL_SCANCODE_LSHIFT
SCANCODE_LALT = lib.SDL_SCANCODE_LALT
SCANCODE_LGUI = lib.SDL_SCANCODE_LGUI
SCANCODE_RCTRL = lib.SDL_SCANCODE_RCTRL
SCANCODE_RSHIFT = lib.SDL_SCANCODE_RSHIFT
SCANCODE_RALT = lib.SDL_SCANCODE_RALT
SCANCODE_RGUI = lib.SDL_SCANCODE_RGUI
SCANCODE_MODE = lib.SDL_SCANCODE_MODE
SCANCODE_AUDIONEXT = lib.SDL_SCANCODE_AUDIONEXT
SCANCODE_AUDIOPREV = lib.SDL_SCANCODE_AUDIOPREV
SCANCODE_AUDIOSTOP = lib.SDL_SCANCODE_AUDIOSTOP
SCANCODE_AUDIOPLAY = lib.SDL_SCANCODE_AUDIOPLAY
SCANCODE_AUDIOMUTE = lib.SDL_SCANCODE_AUDIOMUTE
SCANCODE_MEDIASELECT = lib.SDL_SCANCODE_MEDIASELECT
SCANCODE_WWW = lib.SDL_SCANCODE_WWW
SCANCODE_MAIL = lib.SDL_SCANCODE_MAIL
SCANCODE_CALCULATOR = lib.SDL_SCANCODE_CALCULATOR
SCANCODE_COMPUTER = lib.SDL_SCANCODE_COMPUTER
SCANCODE_AC_SEARCH = lib.SDL_SCANCODE_AC_SEARCH
SCANCODE_AC_HOME = lib.SDL_SCANCODE_AC_HOME
SCANCODE_AC_BACK = lib.SDL_SCANCODE_AC_BACK
SCANCODE_AC_FORWARD = lib.SDL_SCANCODE_AC_FORWARD
SCANCODE_AC_STOP = lib.SDL_SCANCODE_AC_STOP
SCANCODE_AC_REFRESH = lib.SDL_SCANCODE_AC_REFRESH
SCANCODE_AC_BOOKMARKS = lib.SDL_SCANCODE_AC_BOOKMARKS
SCANCODE_BRIGHTNESSDOWN = lib.SDL_SCANCODE_BRIGHTNESSDOWN
SCANCODE_BRIGHTNESSUP = lib.SDL_SCANCODE_BRIGHTNESSUP
SCANCODE_DISPLAYSWITCH = lib.SDL_SCANCODE_DISPLAYSWITCH
SCANCODE_KBDILLUMTOGGLE = lib.SDL_SCANCODE_KBDILLUMTOGGLE
SCANCODE_KBDILLUMDOWN = lib.SDL_SCANCODE_KBDILLUMDOWN
SCANCODE_KBDILLUMUP = lib.SDL_SCANCODE_KBDILLUMUP
SCANCODE_EJECT = lib.SDL_SCANCODE_EJECT
SCANCODE_SLEEP = lib.SDL_SCANCODE_SLEEP
SCANCODE_APP1 = lib.SDL_SCANCODE_APP1
SCANCODE_APP2 = lib.SDL_SCANCODE_APP2
NUM_SCANCODES = lib.SDL_NUM_SCANCODES

SYSTEM_CURSOR_ARROW = lib.SDL_SYSTEM_CURSOR_ARROW
SYSTEM_CURSOR_IBEAM = lib.SDL_SYSTEM_CURSOR_IBEAM
SYSTEM_CURSOR_WAIT = lib.SDL_SYSTEM_CURSOR_WAIT
SYSTEM_CURSOR_CROSSHAIR = lib.SDL_SYSTEM_CURSOR_CROSSHAIR
SYSTEM_CURSOR_WAITARROW = lib.SDL_SYSTEM_CURSOR_WAITARROW
SYSTEM_CURSOR_SIZENWSE = lib.SDL_SYSTEM_CURSOR_SIZENWSE
SYSTEM_CURSOR_SIZENESW = lib.SDL_SYSTEM_CURSOR_SIZENESW
SYSTEM_CURSOR_SIZEWE = lib.SDL_SYSTEM_CURSOR_SIZEWE
SYSTEM_CURSOR_SIZENS = lib.SDL_SYSTEM_CURSOR_SIZENS
SYSTEM_CURSOR_SIZEALL = lib.SDL_SYSTEM_CURSOR_SIZEALL
SYSTEM_CURSOR_NO = lib.SDL_SYSTEM_CURSOR_NO
SYSTEM_CURSOR_HAND = lib.SDL_SYSTEM_CURSOR_HAND
NUM_SYSTEM_CURSORS = lib.SDL_NUM_SYSTEM_CURSORS

TEXTUREACCESS_STATIC = lib.SDL_TEXTUREACCESS_STATIC
TEXTUREACCESS_STREAMING = lib.SDL_TEXTUREACCESS_STREAMING
TEXTUREACCESS_TARGET = lib.SDL_TEXTUREACCESS_TARGET

TEXTUREMODULATE_NONE = lib.SDL_TEXTUREMODULATE_NONE
TEXTUREMODULATE_COLOR = lib.SDL_TEXTUREMODULATE_COLOR
TEXTUREMODULATE_ALPHA = lib.SDL_TEXTUREMODULATE_ALPHA

THREAD_PRIORITY_LOW = lib.SDL_THREAD_PRIORITY_LOW
THREAD_PRIORITY_NORMAL = lib.SDL_THREAD_PRIORITY_NORMAL
THREAD_PRIORITY_HIGH = lib.SDL_THREAD_PRIORITY_HIGH

WINDOWEVENT_NONE = lib.SDL_WINDOWEVENT_NONE
WINDOWEVENT_SHOWN = lib.SDL_WINDOWEVENT_SHOWN
WINDOWEVENT_HIDDEN = lib.SDL_WINDOWEVENT_HIDDEN
WINDOWEVENT_EXPOSED = lib.SDL_WINDOWEVENT_EXPOSED
WINDOWEVENT_MOVED = lib.SDL_WINDOWEVENT_MOVED
WINDOWEVENT_RESIZED = lib.SDL_WINDOWEVENT_RESIZED
WINDOWEVENT_SIZE_CHANGED = lib.SDL_WINDOWEVENT_SIZE_CHANGED
WINDOWEVENT_MINIMIZED = lib.SDL_WINDOWEVENT_MINIMIZED
WINDOWEVENT_MAXIMIZED = lib.SDL_WINDOWEVENT_MAXIMIZED
WINDOWEVENT_RESTORED = lib.SDL_WINDOWEVENT_RESTORED
WINDOWEVENT_ENTER = lib.SDL_WINDOWEVENT_ENTER
WINDOWEVENT_LEAVE = lib.SDL_WINDOWEVENT_LEAVE
WINDOWEVENT_FOCUS_GAINED = lib.SDL_WINDOWEVENT_FOCUS_GAINED
WINDOWEVENT_FOCUS_LOST = lib.SDL_WINDOWEVENT_FOCUS_LOST
WINDOWEVENT_CLOSE = lib.SDL_WINDOWEVENT_CLOSE

WINDOW_FULLSCREEN = lib.SDL_WINDOW_FULLSCREEN
WINDOW_OPENGL = lib.SDL_WINDOW_OPENGL
WINDOW_SHOWN = lib.SDL_WINDOW_SHOWN
WINDOW_HIDDEN = lib.SDL_WINDOW_HIDDEN
WINDOW_BORDERLESS = lib.SDL_WINDOW_BORDERLESS
WINDOW_RESIZABLE = lib.SDL_WINDOW_RESIZABLE
WINDOW_MINIMIZED = lib.SDL_WINDOW_MINIMIZED
WINDOW_MAXIMIZED = lib.SDL_WINDOW_MAXIMIZED
WINDOW_INPUT_GRABBED = lib.SDL_WINDOW_INPUT_GRABBED
WINDOW_INPUT_FOCUS = lib.SDL_WINDOW_INPUT_FOCUS
WINDOW_MOUSE_FOCUS = lib.SDL_WINDOW_MOUSE_FOCUS
WINDOW_FULLSCREEN_DESKTOP = lib.SDL_WINDOW_FULLSCREEN_DESKTOP
WINDOW_FOREIGN = lib.SDL_WINDOW_FOREIGN
WINDOW_ALLOW_HIGHDPI = lib.SDL_WINDOW_ALLOW_HIGHDPI

ASSERTION_RETRY = lib.SDL_ASSERTION_RETRY
ASSERTION_BREAK = lib.SDL_ASSERTION_BREAK
ASSERTION_ABORT = lib.SDL_ASSERTION_ABORT
ASSERTION_IGNORE = lib.SDL_ASSERTION_IGNORE
ASSERTION_ALWAYS_IGNORE = lib.SDL_ASSERTION_ALWAYS_IGNORE

FALSE = lib.SDL_FALSE
TRUE = lib.SDL_TRUE

ENOMEM = lib.SDL_ENOMEM
EFREAD = lib.SDL_EFREAD
EFWRITE = lib.SDL_EFWRITE
EFSEEK = lib.SDL_EFSEEK
UNSUPPORTED = lib.SDL_UNSUPPORTED
LASTERROR = lib.SDL_LASTERROR

ADDEVENT = lib.SDL_ADDEVENT
PEEKEVENT = lib.SDL_PEEKEVENT
GETEVENT = lib.SDL_GETEVENT

AUDIO_F32 = lib.AUDIO_F32

AUDIO_F32LSB = lib.AUDIO_F32LSB

AUDIO_F32MSB = lib.AUDIO_F32MSB

AUDIO_F32SYS = lib.AUDIO_F32SYS

AUDIO_S16 = lib.AUDIO_S16

AUDIO_S16LSB = lib.AUDIO_S16LSB

AUDIO_S16MSB = lib.AUDIO_S16MSB

AUDIO_S16SYS = lib.AUDIO_S16SYS

AUDIO_S32 = lib.AUDIO_S32

AUDIO_S32LSB = lib.AUDIO_S32LSB

AUDIO_S32MSB = lib.AUDIO_S32MSB

AUDIO_S32SYS = lib.AUDIO_S32SYS

AUDIO_S8 = lib.AUDIO_S8

AUDIO_U16 = lib.AUDIO_U16

AUDIO_U16LSB = lib.AUDIO_U16LSB

AUDIO_U16MSB = lib.AUDIO_U16MSB

AUDIO_U16SYS = lib.AUDIO_U16SYS

AUDIO_U8 = lib.AUDIO_U8

AUDIO_ALLOW_ANY_CHANGE = lib.SDL_AUDIO_ALLOW_ANY_CHANGE

AUDIO_ALLOW_CHANNELS_CHANGE = lib.SDL_AUDIO_ALLOW_CHANNELS_CHANGE

AUDIO_ALLOW_FORMAT_CHANGE = lib.SDL_AUDIO_ALLOW_FORMAT_CHANGE

AUDIO_ALLOW_FREQUENCY_CHANGE = lib.SDL_AUDIO_ALLOW_FREQUENCY_CHANGE

AUDIO_MASK_BITSIZE = lib.SDL_AUDIO_MASK_BITSIZE

AUDIO_MASK_DATATYPE = lib.SDL_AUDIO_MASK_DATATYPE

AUDIO_MASK_ENDIAN = lib.SDL_AUDIO_MASK_ENDIAN

AUDIO_MASK_SIGNED = lib.SDL_AUDIO_MASK_SIGNED

BUTTON_LEFT = lib.SDL_BUTTON_LEFT

BUTTON_LMASK = lib.SDL_BUTTON_LMASK

BUTTON_MIDDLE = lib.SDL_BUTTON_MIDDLE

BUTTON_MMASK = lib.SDL_BUTTON_MMASK

BUTTON_RIGHT = lib.SDL_BUTTON_RIGHT

BUTTON_RMASK = lib.SDL_BUTTON_RMASK

BUTTON_X1 = lib.SDL_BUTTON_X1

BUTTON_X1MASK = lib.SDL_BUTTON_X1MASK

BUTTON_X2 = lib.SDL_BUTTON_X2

BUTTON_X2MASK = lib.SDL_BUTTON_X2MASK

COMPILEDVERSION = lib.SDL_COMPILEDVERSION

DISABLE = lib.SDL_DISABLE

DONTFREE = lib.SDL_DONTFREE

ENABLE = lib.SDL_ENABLE

HAPTIC_AUTOCENTER = lib.SDL_HAPTIC_AUTOCENTER

HAPTIC_CARTESIAN = lib.SDL_HAPTIC_CARTESIAN

HAPTIC_CONSTANT = lib.SDL_HAPTIC_CONSTANT

HAPTIC_CUSTOM = lib.SDL_HAPTIC_CUSTOM

HAPTIC_DAMPER = lib.SDL_HAPTIC_DAMPER

HAPTIC_FRICTION = lib.SDL_HAPTIC_FRICTION

HAPTIC_GAIN = lib.SDL_HAPTIC_GAIN

HAPTIC_INERTIA = lib.SDL_HAPTIC_INERTIA

HAPTIC_INFINITY = lib.SDL_HAPTIC_INFINITY

HAPTIC_LEFTRIGHT = lib.SDL_HAPTIC_LEFTRIGHT

HAPTIC_PAUSE = lib.SDL_HAPTIC_PAUSE

HAPTIC_POLAR = lib.SDL_HAPTIC_POLAR

HAPTIC_RAMP = lib.SDL_HAPTIC_RAMP

HAPTIC_SAWTOOTHDOWN = lib.SDL_HAPTIC_SAWTOOTHDOWN

HAPTIC_SAWTOOTHUP = lib.SDL_HAPTIC_SAWTOOTHUP

HAPTIC_SINE = lib.SDL_HAPTIC_SINE

HAPTIC_SPHERICAL = lib.SDL_HAPTIC_SPHERICAL

HAPTIC_SPRING = lib.SDL_HAPTIC_SPRING

HAPTIC_STATUS = lib.SDL_HAPTIC_STATUS

HAPTIC_TRIANGLE = lib.SDL_HAPTIC_TRIANGLE

HAT_CENTERED = lib.SDL_HAT_CENTERED

HAT_DOWN = lib.SDL_HAT_DOWN

HAT_LEFT = lib.SDL_HAT_LEFT

HAT_LEFTDOWN = lib.SDL_HAT_LEFTDOWN

HAT_LEFTUP = lib.SDL_HAT_LEFTUP

HAT_RIGHT = lib.SDL_HAT_RIGHT

HAT_RIGHTDOWN = lib.SDL_HAT_RIGHTDOWN

HAT_RIGHTUP = lib.SDL_HAT_RIGHTUP

HAT_UP = lib.SDL_HAT_UP

IGNORE = lib.SDL_IGNORE

INIT_AUDIO = lib.SDL_INIT_AUDIO

INIT_EVENTS = lib.SDL_INIT_EVENTS

INIT_EVERYTHING = lib.SDL_INIT_EVERYTHING

INIT_GAMECONTROLLER = lib.SDL_INIT_GAMECONTROLLER

INIT_HAPTIC = lib.SDL_INIT_HAPTIC

INIT_JOYSTICK = lib.SDL_INIT_JOYSTICK

INIT_NOPARACHUTE = lib.SDL_INIT_NOPARACHUTE

INIT_TIMER = lib.SDL_INIT_TIMER

INIT_VIDEO = lib.SDL_INIT_VIDEO

LINE = lib.SDL_LINE

MAJOR_VERSION = lib.SDL_MAJOR_VERSION

MAX_LOG_MESSAGE = lib.SDL_MAX_LOG_MESSAGE

MINOR_VERSION = lib.SDL_MINOR_VERSION

MIX_MAXVOLUME = lib.SDL_MIX_MAXVOLUME

NULL_WHILE_LOOP_CONDITION = lib.SDL_NULL_WHILE_LOOP_CONDITION

PATCHLEVEL = lib.SDL_PATCHLEVEL

PREALLOC = lib.SDL_PREALLOC

PRESSED = lib.SDL_PRESSED

QUERY = lib.SDL_QUERY

RELEASED = lib.SDL_RELEASED

RLEACCEL = lib.SDL_RLEACCEL

RWOPS_JNIFILE = lib.SDL_RWOPS_JNIFILE

RWOPS_MEMORY = lib.SDL_RWOPS_MEMORY

RWOPS_MEMORY_RO = lib.SDL_RWOPS_MEMORY_RO

RWOPS_STDFILE = lib.SDL_RWOPS_STDFILE

RWOPS_UNKNOWN = lib.SDL_RWOPS_UNKNOWN

RWOPS_WINFILE = lib.SDL_RWOPS_WINFILE

SWSURFACE = lib.SDL_SWSURFACE

TEXTEDITINGEVENT_TEXT_SIZE = lib.SDL_TEXTEDITINGEVENT_TEXT_SIZE

TEXTINPUTEVENT_TEXT_SIZE = lib.SDL_TEXTINPUTEVENT_TEXT_SIZE

TOUCH_MOUSEID = lib.SDL_TOUCH_MOUSEID

WINDOWPOS_CENTERED = lib.SDL_WINDOWPOS_CENTERED

WINDOWPOS_CENTERED_MASK = lib.SDL_WINDOWPOS_CENTERED_MASK

WINDOWPOS_UNDEFINED = lib.SDL_WINDOWPOS_UNDEFINED

WINDOWPOS_UNDEFINED_MASK = lib.SDL_WINDOWPOS_UNDEFINED_MASK

class AudioCVT(Struct):
    """Wrap `SDL_AudioCVT`"""
    __ctype__ = 'SDL_AudioCVT'
    _fields = ('needed', 'src_format', 'dst_format', 'rate_incr', 'buf',
        'len', 'len_cvt', 'len_mult', 'len_ratio', 'filters', 'filter_index')

    @property
    def needed(self):
        return self.cdata.needed

    @needed.setter
    def needed(self, value):
        self.cdata.needed = value

    @property
    def src_format(self):
        return self.cdata.src_format

    @src_format.setter
    def src_format(self, value):
        self.cdata.src_format = value

    @property
    def dst_format(self):
        return self.cdata.dst_format

    @dst_format.setter
    def dst_format(self, value):
        self.cdata.dst_format = value

    @property
    def rate_incr(self):
        return self.cdata.rate_incr

    @rate_incr.setter
    def rate_incr(self, value):
        self.cdata.rate_incr = value

    @property
    def buf(self):
        return self.cdata.buf

    @buf.setter
    def buf(self, value):
        self.cdata.buf = value

    @property
    def len(self):
        return self.cdata.len

    @len.setter
    def len(self, value):
        self.cdata.len = value

    @property
    def len_cvt(self):
        return self.cdata.len_cvt

    @len_cvt.setter
    def len_cvt(self, value):
        self.cdata.len_cvt = value

    @property
    def len_mult(self):
        return self.cdata.len_mult

    @len_mult.setter
    def len_mult(self, value):
        self.cdata.len_mult = value

    @property
    def len_ratio(self):
        return self.cdata.len_ratio

    @len_ratio.setter
    def len_ratio(self, value):
        self.cdata.len_ratio = value

    @property
    def filters(self):
        return self.cdata.filters

    @filters.setter
    def filters(self, value):
        self.cdata.filters = value

    @property
    def filter_index(self):
        return self.cdata.filter_index

    @filter_index.setter
    def filter_index(self, value):
        self.cdata.filter_index = value
    buildAudioCVT = buildAudioCVT
    convertAudio = convertAudio

class AudioSpec(Struct):
    """Wrap `SDL_AudioSpec`"""
    __ctype__ = 'SDL_AudioSpec'
    _fields = ('freq', 'format', 'channels', 'silence', 'samples',
        'padding', 'size', 'callback', 'userdata')

    @property
    def freq(self):
        return self.cdata.freq

    @freq.setter
    def freq(self, value):
        self.cdata.freq = value

    @property
    def format(self):
        return self.cdata.format

    @format.setter
    def format(self, value):
        self.cdata.format = value

    @property
    def channels(self):
        return self.cdata.channels

    @channels.setter
    def channels(self, value):
        self.cdata.channels = value

    @property
    def silence(self):
        return self.cdata.silence

    @silence.setter
    def silence(self, value):
        self.cdata.silence = value

    @property
    def samples(self):
        return self.cdata.samples

    @samples.setter
    def samples(self, value):
        self.cdata.samples = value

    @property
    def padding(self):
        return self.cdata.padding

    @padding.setter
    def padding(self, value):
        self.cdata.padding = value

    @property
    def size(self):
        return self.cdata.size

    @size.setter
    def size(self, value):
        self.cdata.size = value

    @property
    def callback(self):
        return self.cdata.callback

    @callback.setter
    def callback(self, value):
        self.cdata.callback = value

    @property
    def userdata(self):
        return self.cdata.userdata

    @userdata.setter
    def userdata(self, value):
        self.cdata.userdata = value
    openAudio = openAudio

class Color(Struct):
    """Wrap `SDL_Color`"""
    __ctype__ = 'SDL_Color'
    _fields = 'r', 'g', 'b', 'a'

    @property
    def r(self):
        return self.cdata.r

    @r.setter
    def r(self, value):
        self.cdata.r = value

    @property
    def g(self):
        return self.cdata.g

    @g.setter
    def g(self, value):
        self.cdata.g = value

    @property
    def b(self):
        return self.cdata.b

    @b.setter
    def b(self, value):
        self.cdata.b = value

    @property
    def a(self):
        return self.cdata.a

    @a.setter
    def a(self, value):
        self.cdata.a = value

class CommonEvent(Struct):
    """Wrap `SDL_CommonEvent`"""
    __ctype__ = 'SDL_CommonEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class ControllerAxisEvent(Struct):
    """Wrap `SDL_ControllerAxisEvent`"""
    __ctype__ = 'SDL_ControllerAxisEvent'
    _fields = ('type', 'timestamp', 'which', 'axis', 'padding1', 'padding2',
        'padding3', 'value', 'padding4')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def axis(self):
        return self.cdata.axis

    @axis.setter
    def axis(self, value):
        self.cdata.axis = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding4(self):
        return self.cdata.padding4

    @padding4.setter
    def padding4(self, value):
        self.cdata.padding4 = value

class ControllerButtonEvent(Struct):
    """Wrap `SDL_ControllerButtonEvent`"""
    __ctype__ = 'SDL_ControllerButtonEvent'
    _fields = ('type', 'timestamp', 'which', 'button', 'state', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class ControllerDeviceEvent(Struct):
    """Wrap `SDL_ControllerDeviceEvent`"""
    __ctype__ = 'SDL_ControllerDeviceEvent'
    _fields = 'type', 'timestamp', 'which'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

class Cursor(Struct):
    """Wrap `SDL_Cursor`"""
    __ctype__ = 'SDL_Cursor'
    _fields = ()
    freeCursor = freeCursor
    setCursor = setCursor

class DisplayMode(Struct):
    """Wrap `SDL_DisplayMode`"""
    __ctype__ = 'SDL_DisplayMode'
    _fields = 'format', 'w', 'h', 'refresh_rate', 'driverdata'

    @property
    def format(self):
        return self.cdata.format

    @format.setter
    def format(self, value):
        self.cdata.format = value

    @property
    def w(self):
        return self.cdata.w

    @w.setter
    def w(self, value):
        self.cdata.w = value

    @property
    def h(self):
        return self.cdata.h

    @h.setter
    def h(self, value):
        self.cdata.h = value

    @property
    def refresh_rate(self):
        return self.cdata.refresh_rate

    @refresh_rate.setter
    def refresh_rate(self, value):
        self.cdata.refresh_rate = value

    @property
    def driverdata(self):
        return self.cdata.driverdata

    @driverdata.setter
    def driverdata(self, value):
        self.cdata.driverdata = value

class DollarGestureEvent(Struct):
    """Wrap `SDL_DollarGestureEvent`"""
    __ctype__ = 'SDL_DollarGestureEvent'
    _fields = ('type', 'timestamp', 'touchId', 'gestureId', 'numFingers',
        'error', 'x', 'y')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def touchId(self):
        return self.cdata.touchId

    @touchId.setter
    def touchId(self, value):
        self.cdata.touchId = value

    @property
    def gestureId(self):
        return self.cdata.gestureId

    @gestureId.setter
    def gestureId(self, value):
        self.cdata.gestureId = value

    @property
    def numFingers(self):
        return self.cdata.numFingers

    @numFingers.setter
    def numFingers(self, value):
        self.cdata.numFingers = value

    @property
    def error(self):
        return self.cdata.error

    @error.setter
    def error(self, value):
        self.cdata.error = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

class DropEvent(Struct):
    """Wrap `SDL_DropEvent`"""
    __ctype__ = 'SDL_DropEvent'
    _fields = 'type', 'timestamp', 'file'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def file(self):
        return self.cdata.file

    @file.setter
    def file(self, value):
        self.cdata.file = value

class Event(Struct):
    """Wrap `SDL_Event`"""
    __ctype__ = 'SDL_Event'
    _fields = ('type', 'common', 'window', 'key', 'edit', 'text', 'motion',
        'button', 'wheel', 'jaxis', 'jball', 'jhat', 'jbutton', 'jdevice',
        'caxis', 'cbutton', 'cdevice', 'quit', 'user', 'syswm', 'tfinger',
        'mgesture', 'dgesture', 'drop', 'padding')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def common(self):
        return CommonEvent(self.cdata.common) if self.cdata.common else None

    @common.setter
    def common(self, value):
        try:
            self.cdata.common = value.cdata
        except:
            self.cdata.common = ffi.new('SDL_CommonEvent *', value)

    @property
    def window(self):
        return WindowEvent(self.cdata.window) if self.cdata.window else None

    @window.setter
    def window(self, value):
        try:
            self.cdata.window = value.cdata
        except:
            self.cdata.window = ffi.new('SDL_WindowEvent *', value)

    @property
    def key(self):
        return KeyboardEvent(self.cdata.key) if self.cdata.key else None

    @key.setter
    def key(self, value):
        try:
            self.cdata.key = value.cdata
        except:
            self.cdata.key = ffi.new('SDL_KeyboardEvent *', value)

    @property
    def edit(self):
        return TextEditingEvent(self.cdata.edit) if self.cdata.edit else None

    @edit.setter
    def edit(self, value):
        try:
            self.cdata.edit = value.cdata
        except:
            self.cdata.edit = ffi.new('SDL_TextEditingEvent *', value)

    @property
    def text(self):
        return TextInputEvent(self.cdata.text) if self.cdata.text else None

    @text.setter
    def text(self, value):
        try:
            self.cdata.text = value.cdata
        except:
            self.cdata.text = ffi.new('SDL_TextInputEvent *', value)

    @property
    def motion(self):
        return MouseMotionEvent(self.cdata.motion
            ) if self.cdata.motion else None

    @motion.setter
    def motion(self, value):
        try:
            self.cdata.motion = value.cdata
        except:
            self.cdata.motion = ffi.new('SDL_MouseMotionEvent *', value)

    @property
    def button(self):
        return MouseButtonEvent(self.cdata.button
            ) if self.cdata.button else None

    @button.setter
    def button(self, value):
        try:
            self.cdata.button = value.cdata
        except:
            self.cdata.button = ffi.new('SDL_MouseButtonEvent *', value)

    @property
    def wheel(self):
        return MouseWheelEvent(self.cdata.wheel) if self.cdata.wheel else None

    @wheel.setter
    def wheel(self, value):
        try:
            self.cdata.wheel = value.cdata
        except:
            self.cdata.wheel = ffi.new('SDL_MouseWheelEvent *', value)

    @property
    def jaxis(self):
        return JoyAxisEvent(self.cdata.jaxis) if self.cdata.jaxis else None

    @jaxis.setter
    def jaxis(self, value):
        try:
            self.cdata.jaxis = value.cdata
        except:
            self.cdata.jaxis = ffi.new('SDL_JoyAxisEvent *', value)

    @property
    def jball(self):
        return JoyBallEvent(self.cdata.jball) if self.cdata.jball else None

    @jball.setter
    def jball(self, value):
        try:
            self.cdata.jball = value.cdata
        except:
            self.cdata.jball = ffi.new('SDL_JoyBallEvent *', value)

    @property
    def jhat(self):
        return JoyHatEvent(self.cdata.jhat) if self.cdata.jhat else None

    @jhat.setter
    def jhat(self, value):
        try:
            self.cdata.jhat = value.cdata
        except:
            self.cdata.jhat = ffi.new('SDL_JoyHatEvent *', value)

    @property
    def jbutton(self):
        return JoyButtonEvent(self.cdata.jbutton
            ) if self.cdata.jbutton else None

    @jbutton.setter
    def jbutton(self, value):
        try:
            self.cdata.jbutton = value.cdata
        except:
            self.cdata.jbutton = ffi.new('SDL_JoyButtonEvent *', value)

    @property
    def jdevice(self):
        return JoyDeviceEvent(self.cdata.jdevice
            ) if self.cdata.jdevice else None

    @jdevice.setter
    def jdevice(self, value):
        try:
            self.cdata.jdevice = value.cdata
        except:
            self.cdata.jdevice = ffi.new('SDL_JoyDeviceEvent *', value)

    @property
    def caxis(self):
        return ControllerAxisEvent(self.cdata.caxis
            ) if self.cdata.caxis else None

    @caxis.setter
    def caxis(self, value):
        try:
            self.cdata.caxis = value.cdata
        except:
            self.cdata.caxis = ffi.new('SDL_ControllerAxisEvent *', value)

    @property
    def cbutton(self):
        return ControllerButtonEvent(self.cdata.cbutton
            ) if self.cdata.cbutton else None

    @cbutton.setter
    def cbutton(self, value):
        try:
            self.cdata.cbutton = value.cdata
        except:
            self.cdata.cbutton = ffi.new('SDL_ControllerButtonEvent *', value)

    @property
    def cdevice(self):
        return ControllerDeviceEvent(self.cdata.cdevice
            ) if self.cdata.cdevice else None

    @cdevice.setter
    def cdevice(self, value):
        try:
            self.cdata.cdevice = value.cdata
        except:
            self.cdata.cdevice = ffi.new('SDL_ControllerDeviceEvent *', value)

    @property
    def quit(self):
        return QuitEvent(self.cdata.quit) if self.cdata.quit else None

    @quit.setter
    def quit(self, value):
        try:
            self.cdata.quit = value.cdata
        except:
            self.cdata.quit = ffi.new('SDL_QuitEvent *', value)

    @property
    def user(self):
        return UserEvent(self.cdata.user) if self.cdata.user else None

    @user.setter
    def user(self, value):
        try:
            self.cdata.user = value.cdata
        except:
            self.cdata.user = ffi.new('SDL_UserEvent *', value)

    @property
    def syswm(self):
        return SysWMEvent(self.cdata.syswm) if self.cdata.syswm else None

    @syswm.setter
    def syswm(self, value):
        try:
            self.cdata.syswm = value.cdata
        except:
            self.cdata.syswm = ffi.new('SDL_SysWMEvent *', value)

    @property
    def tfinger(self):
        return TouchFingerEvent(self.cdata.tfinger
            ) if self.cdata.tfinger else None

    @tfinger.setter
    def tfinger(self, value):
        try:
            self.cdata.tfinger = value.cdata
        except:
            self.cdata.tfinger = ffi.new('SDL_TouchFingerEvent *', value)

    @property
    def mgesture(self):
        return MultiGestureEvent(self.cdata.mgesture
            ) if self.cdata.mgesture else None

    @mgesture.setter
    def mgesture(self, value):
        try:
            self.cdata.mgesture = value.cdata
        except:
            self.cdata.mgesture = ffi.new('SDL_MultiGestureEvent *', value)

    @property
    def dgesture(self):
        return DollarGestureEvent(self.cdata.dgesture
            ) if self.cdata.dgesture else None

    @dgesture.setter
    def dgesture(self, value):
        try:
            self.cdata.dgesture = value.cdata
        except:
            self.cdata.dgesture = ffi.new('SDL_DollarGestureEvent *', value)

    @property
    def drop(self):
        return DropEvent(self.cdata.drop) if self.cdata.drop else None

    @drop.setter
    def drop(self, value):
        try:
            self.cdata.drop = value.cdata
        except:
            self.cdata.drop = ffi.new('SDL_DropEvent *', value)

    @property
    def padding(self):
        return self.cdata.padding

    @padding.setter
    def padding(self, value):
        self.cdata.padding = value
    unwrapEvent = unwrapEvent
    peepEvents = peepEvents
    pollEvent = pollEvent
    pushEvent = pushEvent
    waitEvent = waitEvent
    waitEventTimeout = waitEventTimeout

class Finger(Struct):
    """Wrap `SDL_Finger`"""
    __ctype__ = 'SDL_Finger'
    _fields = 'id', 'x', 'y', 'pressure'

    @property
    def id(self):
        return self.cdata.id

    @id.setter
    def id(self, value):
        self.cdata.id = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def pressure(self):
        return self.cdata.pressure

    @pressure.setter
    def pressure(self, value):
        self.cdata.pressure = value

class GameController(Struct):
    """Wrap `SDL_GameController`"""
    __ctype__ = 'SDL_GameController'
    _fields = ()
    gameControllerClose = gameControllerClose
    gameControllerGetAttached = gameControllerGetAttached
    gameControllerGetAxis = gameControllerGetAxis
    gameControllerGetBindForAxis = gameControllerGetBindForAxis
    gameControllerGetBindForButton = gameControllerGetBindForButton
    gameControllerGetButton = gameControllerGetButton
    gameControllerGetJoystick = gameControllerGetJoystick
    gameControllerMapping = gameControllerMapping
    gameControllerName = gameControllerName

class GameControllerButtonBind(Struct):
    """Wrap `SDL_GameControllerButtonBind`"""
    __ctype__ = 'SDL_GameControllerButtonBind'
    _fields = 'bindType', 'value'

    @property
    def bindType(self):
        return self.cdata.bindType

    @bindType.setter
    def bindType(self, value):
        self.cdata.bindType = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

class Haptic(Struct):
    """Wrap `SDL_Haptic`"""
    __ctype__ = 'SDL_Haptic'
    _fields = ()
    hapticClose = hapticClose
    hapticDestroyEffect = hapticDestroyEffect
    hapticEffectSupported = hapticEffectSupported
    hapticGetEffectStatus = hapticGetEffectStatus
    hapticIndex = hapticIndex
    hapticNewEffect = hapticNewEffect
    hapticNumAxes = hapticNumAxes
    hapticNumEffects = hapticNumEffects
    hapticNumEffectsPlaying = hapticNumEffectsPlaying
    hapticPause = hapticPause
    hapticQuery = hapticQuery
    hapticRumbleInit = hapticRumbleInit
    hapticRumblePlay = hapticRumblePlay
    hapticRumbleStop = hapticRumbleStop
    hapticRumbleSupported = hapticRumbleSupported
    hapticRunEffect = hapticRunEffect
    hapticSetAutocenter = hapticSetAutocenter
    hapticSetGain = hapticSetGain
    hapticStopAll = hapticStopAll
    hapticStopEffect = hapticStopEffect
    hapticUnpause = hapticUnpause
    hapticUpdateEffect = hapticUpdateEffect

class HapticCondition(Struct):
    """Wrap `SDL_HapticCondition`"""
    __ctype__ = 'SDL_HapticCondition'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'right_sat', 'left_sat', 'right_coeff', 'left_coeff', 'deadband',
        'center')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def right_sat(self):
        return self.cdata.right_sat

    @right_sat.setter
    def right_sat(self, value):
        self.cdata.right_sat = value

    @property
    def left_sat(self):
        return self.cdata.left_sat

    @left_sat.setter
    def left_sat(self, value):
        self.cdata.left_sat = value

    @property
    def right_coeff(self):
        return self.cdata.right_coeff

    @right_coeff.setter
    def right_coeff(self, value):
        self.cdata.right_coeff = value

    @property
    def left_coeff(self):
        return self.cdata.left_coeff

    @left_coeff.setter
    def left_coeff(self, value):
        self.cdata.left_coeff = value

    @property
    def deadband(self):
        return self.cdata.deadband

    @deadband.setter
    def deadband(self, value):
        self.cdata.deadband = value

    @property
    def center(self):
        return self.cdata.center

    @center.setter
    def center(self, value):
        self.cdata.center = value

class HapticConstant(Struct):
    """Wrap `SDL_HapticConstant`"""
    __ctype__ = 'SDL_HapticConstant'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'level', 'attack_length', 'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def level(self):
        return self.cdata.level

    @level.setter
    def level(self, value):
        self.cdata.level = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticCustom(Struct):
    """Wrap `SDL_HapticCustom`"""
    __ctype__ = 'SDL_HapticCustom'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'channels', 'period', 'samples', 'data', 'attack_length',
        'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def channels(self):
        return self.cdata.channels

    @channels.setter
    def channels(self, value):
        self.cdata.channels = value

    @property
    def period(self):
        return self.cdata.period

    @period.setter
    def period(self, value):
        self.cdata.period = value

    @property
    def samples(self):
        return self.cdata.samples

    @samples.setter
    def samples(self, value):
        self.cdata.samples = value

    @property
    def data(self):
        return self.cdata.data

    @data.setter
    def data(self, value):
        self.cdata.data = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticDirection(Struct):
    """Wrap `SDL_HapticDirection`"""
    __ctype__ = 'SDL_HapticDirection'
    _fields = 'type', 'dir'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def dir(self):
        return self.cdata.dir

    @dir.setter
    def dir(self, value):
        self.cdata.dir = value

class HapticEffect(Struct):
    """Wrap `SDL_HapticEffect`"""
    __ctype__ = 'SDL_HapticEffect'
    _fields = ('type', 'constant', 'periodic', 'condition', 'ramp',
        'leftright', 'custom')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def constant(self):
        return HapticConstant(self.cdata.constant
            ) if self.cdata.constant else None

    @constant.setter
    def constant(self, value):
        try:
            self.cdata.constant = value.cdata
        except:
            self.cdata.constant = ffi.new('SDL_HapticConstant *', value)

    @property
    def periodic(self):
        return HapticPeriodic(self.cdata.periodic
            ) if self.cdata.periodic else None

    @periodic.setter
    def periodic(self, value):
        try:
            self.cdata.periodic = value.cdata
        except:
            self.cdata.periodic = ffi.new('SDL_HapticPeriodic *', value)

    @property
    def condition(self):
        return HapticCondition(self.cdata.condition
            ) if self.cdata.condition else None

    @condition.setter
    def condition(self, value):
        try:
            self.cdata.condition = value.cdata
        except:
            self.cdata.condition = ffi.new('SDL_HapticCondition *', value)

    @property
    def ramp(self):
        return HapticRamp(self.cdata.ramp) if self.cdata.ramp else None

    @ramp.setter
    def ramp(self, value):
        try:
            self.cdata.ramp = value.cdata
        except:
            self.cdata.ramp = ffi.new('SDL_HapticRamp *', value)

    @property
    def leftright(self):
        return HapticLeftRight(self.cdata.leftright
            ) if self.cdata.leftright else None

    @leftright.setter
    def leftright(self, value):
        try:
            self.cdata.leftright = value.cdata
        except:
            self.cdata.leftright = ffi.new('SDL_HapticLeftRight *', value)

    @property
    def custom(self):
        return HapticCustom(self.cdata.custom) if self.cdata.custom else None

    @custom.setter
    def custom(self, value):
        try:
            self.cdata.custom = value.cdata
        except:
            self.cdata.custom = ffi.new('SDL_HapticCustom *', value)

class HapticLeftRight(Struct):
    """Wrap `SDL_HapticLeftRight`"""
    __ctype__ = 'SDL_HapticLeftRight'
    _fields = 'type', 'length', 'large_magnitude', 'small_magnitude'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def large_magnitude(self):
        return self.cdata.large_magnitude

    @large_magnitude.setter
    def large_magnitude(self, value):
        self.cdata.large_magnitude = value

    @property
    def small_magnitude(self):
        return self.cdata.small_magnitude

    @small_magnitude.setter
    def small_magnitude(self, value):
        self.cdata.small_magnitude = value

class HapticPeriodic(Struct):
    """Wrap `SDL_HapticPeriodic`"""
    __ctype__ = 'SDL_HapticPeriodic'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'period', 'magnitude', 'offset', 'phase', 'attack_length',
        'attack_level', 'fade_length', 'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def period(self):
        return self.cdata.period

    @period.setter
    def period(self, value):
        self.cdata.period = value

    @property
    def magnitude(self):
        return self.cdata.magnitude

    @magnitude.setter
    def magnitude(self, value):
        self.cdata.magnitude = value

    @property
    def offset(self):
        return self.cdata.offset

    @offset.setter
    def offset(self, value):
        self.cdata.offset = value

    @property
    def phase(self):
        return self.cdata.phase

    @phase.setter
    def phase(self, value):
        self.cdata.phase = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class HapticRamp(Struct):
    """Wrap `SDL_HapticRamp`"""
    __ctype__ = 'SDL_HapticRamp'
    _fields = ('type', 'direction', 'length', 'delay', 'button', 'interval',
        'start', 'end', 'attack_length', 'attack_level', 'fade_length',
        'fade_level')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def direction(self):
        return HapticDirection(self.cdata.direction
            ) if self.cdata.direction else None

    @direction.setter
    def direction(self, value):
        try:
            self.cdata.direction = value.cdata
        except:
            self.cdata.direction = ffi.new('SDL_HapticDirection *', value)

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

    @property
    def delay(self):
        return self.cdata.delay

    @delay.setter
    def delay(self, value):
        self.cdata.delay = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def interval(self):
        return self.cdata.interval

    @interval.setter
    def interval(self, value):
        self.cdata.interval = value

    @property
    def start(self):
        return self.cdata.start

    @start.setter
    def start(self, value):
        self.cdata.start = value

    @property
    def end(self):
        return self.cdata.end

    @end.setter
    def end(self, value):
        self.cdata.end = value

    @property
    def attack_length(self):
        return self.cdata.attack_length

    @attack_length.setter
    def attack_length(self, value):
        self.cdata.attack_length = value

    @property
    def attack_level(self):
        return self.cdata.attack_level

    @attack_level.setter
    def attack_level(self, value):
        self.cdata.attack_level = value

    @property
    def fade_length(self):
        return self.cdata.fade_length

    @fade_length.setter
    def fade_length(self, value):
        self.cdata.fade_length = value

    @property
    def fade_level(self):
        return self.cdata.fade_level

    @fade_level.setter
    def fade_level(self, value):
        self.cdata.fade_level = value

class JoyAxisEvent(Struct):
    """Wrap `SDL_JoyAxisEvent`"""
    __ctype__ = 'SDL_JoyAxisEvent'
    _fields = ('type', 'timestamp', 'which', 'axis', 'padding1', 'padding2',
        'padding3', 'value', 'padding4')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def axis(self):
        return self.cdata.axis

    @axis.setter
    def axis(self, value):
        self.cdata.axis = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding4(self):
        return self.cdata.padding4

    @padding4.setter
    def padding4(self, value):
        self.cdata.padding4 = value

class JoyBallEvent(Struct):
    """Wrap `SDL_JoyBallEvent`"""
    __ctype__ = 'SDL_JoyBallEvent'
    _fields = ('type', 'timestamp', 'which', 'ball', 'padding1', 'padding2',
        'padding3', 'xrel', 'yrel')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def ball(self):
        return self.cdata.ball

    @ball.setter
    def ball(self, value):
        self.cdata.ball = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def xrel(self):
        return self.cdata.xrel

    @xrel.setter
    def xrel(self, value):
        self.cdata.xrel = value

    @property
    def yrel(self):
        return self.cdata.yrel

    @yrel.setter
    def yrel(self, value):
        self.cdata.yrel = value

class JoyButtonEvent(Struct):
    """Wrap `SDL_JoyButtonEvent`"""
    __ctype__ = 'SDL_JoyButtonEvent'
    _fields = ('type', 'timestamp', 'which', 'button', 'state', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class JoyDeviceEvent(Struct):
    """Wrap `SDL_JoyDeviceEvent`"""
    __ctype__ = 'SDL_JoyDeviceEvent'
    _fields = 'type', 'timestamp', 'which'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

class JoyHatEvent(Struct):
    """Wrap `SDL_JoyHatEvent`"""
    __ctype__ = 'SDL_JoyHatEvent'
    _fields = ('type', 'timestamp', 'which', 'hat', 'value', 'padding1',
        'padding2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def hat(self):
        return self.cdata.hat

    @hat.setter
    def hat(self, value):
        self.cdata.hat = value

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

class Joystick(Struct):
    """Wrap `SDL_Joystick`"""
    __ctype__ = 'SDL_Joystick'
    _fields = ()
    hapticOpenFromJoystick = hapticOpenFromJoystick
    joystickClose = joystickClose
    joystickGetAttached = joystickGetAttached
    joystickGetAxis = joystickGetAxis
    joystickGetBall = joystickGetBall
    joystickGetButton = joystickGetButton
    joystickGetGUID = joystickGetGUID
    joystickGetHat = joystickGetHat
    joystickInstanceID = joystickInstanceID
    joystickIsHaptic = joystickIsHaptic
    joystickName = joystickName
    joystickNumAxes = joystickNumAxes
    joystickNumBalls = joystickNumBalls
    joystickNumButtons = joystickNumButtons
    joystickNumHats = joystickNumHats

class JoystickGUID(Struct):
    """Wrap `SDL_JoystickGUID`"""
    __ctype__ = 'SDL_JoystickGUID'
    _fields = 'data',

    @property
    def data(self):
        return self.cdata.data

    @data.setter
    def data(self, value):
        self.cdata.data = value

class KeyboardEvent(Struct):
    """Wrap `SDL_KeyboardEvent`"""
    __ctype__ = 'SDL_KeyboardEvent'
    _fields = ('type', 'timestamp', 'windowID', 'state', 'repeat',
        'padding2', 'padding3', 'keysym')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def repeat(self):
        return self.cdata.repeat

    @repeat.setter
    def repeat(self, value):
        self.cdata.repeat = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def keysym(self):
        return Keysym(self.cdata.keysym) if self.cdata.keysym else None

    @keysym.setter
    def keysym(self, value):
        try:
            self.cdata.keysym = value.cdata
        except:
            self.cdata.keysym = ffi.new('SDL_Keysym *', value)

class Keysym(Struct):
    """Wrap `SDL_Keysym`"""
    __ctype__ = 'SDL_Keysym'
    _fields = 'scancode', 'sym', 'mod', 'unused'

    @property
    def scancode(self):
        return self.cdata.scancode

    @scancode.setter
    def scancode(self, value):
        self.cdata.scancode = value

    @property
    def sym(self):
        return self.cdata.sym

    @sym.setter
    def sym(self, value):
        self.cdata.sym = value

    @property
    def mod(self):
        return self.cdata.mod

    @mod.setter
    def mod(self, value):
        self.cdata.mod = value

    @property
    def unused(self):
        return self.cdata.unused

    @unused.setter
    def unused(self, value):
        self.cdata.unused = value

class MessageBoxButtonData(Struct):
    """Wrap `SDL_MessageBoxButtonData`"""
    __ctype__ = 'SDL_MessageBoxButtonData'
    _fields = 'flags', 'buttonid', 'text'

    @property
    def flags(self):
        return self.cdata.flags

    @flags.setter
    def flags(self, value):
        self.cdata.flags = value

    @property
    def buttonid(self):
        return self.cdata.buttonid

    @buttonid.setter
    def buttonid(self, value):
        self.cdata.buttonid = value

    @property
    def text(self):
        return self.cdata.text

    @text.setter
    def text(self, value):
        self.cdata.text = value

class MessageBoxColor(Struct):
    """Wrap `SDL_MessageBoxColor`"""
    __ctype__ = 'SDL_MessageBoxColor'
    _fields = 'r', 'g', 'b'

    @property
    def r(self):
        return self.cdata.r

    @r.setter
    def r(self, value):
        self.cdata.r = value

    @property
    def g(self):
        return self.cdata.g

    @g.setter
    def g(self, value):
        self.cdata.g = value

    @property
    def b(self):
        return self.cdata.b

    @b.setter
    def b(self, value):
        self.cdata.b = value

class MessageBoxColorScheme(Struct):
    """Wrap `SDL_MessageBoxColorScheme`"""
    __ctype__ = 'SDL_MessageBoxColorScheme'
    _fields = 'colors',

    @property
    def colors(self):
        return self.cdata.colors

    @colors.setter
    def colors(self, value):
        self.cdata.colors = value

class MessageBoxData(Struct):
    """Wrap `SDL_MessageBoxData`"""
    __ctype__ = 'SDL_MessageBoxData'
    _fields = ('flags', 'window', 'title', 'message', 'numbuttons',
        'buttons', 'colorScheme')

    @property
    def flags(self):
        return self.cdata.flags

    @flags.setter
    def flags(self, value):
        self.cdata.flags = value

    @property
    def window(self):
        return Window(self.cdata.window) if self.cdata.window else None

    @window.setter
    def window(self, value):
        try:
            self.cdata.window = value.cdata
        except:
            self.cdata.window = ffi.new('SDL_Window *', value)

    @property
    def title(self):
        return self.cdata.title

    @title.setter
    def title(self, value):
        self.cdata.title = value

    @property
    def message(self):
        return self.cdata.message

    @message.setter
    def message(self, value):
        self.cdata.message = value

    @property
    def numbuttons(self):
        return self.cdata.numbuttons

    @numbuttons.setter
    def numbuttons(self, value):
        self.cdata.numbuttons = value

    @property
    def buttons(self):
        return MessageBoxButtonData(self.cdata.buttons
            ) if self.cdata.buttons else None

    @buttons.setter
    def buttons(self, value):
        try:
            self.cdata.buttons = value.cdata
        except:
            self.cdata.buttons = ffi.new('SDL_MessageBoxButtonData *', value)

    @property
    def colorScheme(self):
        return MessageBoxColorScheme(self.cdata.colorScheme
            ) if self.cdata.colorScheme else None

    @colorScheme.setter
    def colorScheme(self, value):
        try:
            self.cdata.colorScheme = value.cdata
        except:
            self.cdata.colorScheme = ffi.new('SDL_MessageBoxColorScheme *',
                value)
    showMessageBox = showMessageBox

class MouseButtonEvent(Struct):
    """Wrap `SDL_MouseButtonEvent`"""
    __ctype__ = 'SDL_MouseButtonEvent'
    _fields = ('type', 'timestamp', 'windowID', 'which', 'button', 'state',
        'clicks', 'padding1', 'x', 'y')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def button(self):
        return self.cdata.button

    @button.setter
    def button(self, value):
        self.cdata.button = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def clicks(self):
        return self.cdata.clicks

    @clicks.setter
    def clicks(self, value):
        self.cdata.clicks = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

class MouseMotionEvent(Struct):
    """Wrap `SDL_MouseMotionEvent`"""
    __ctype__ = 'SDL_MouseMotionEvent'
    _fields = ('type', 'timestamp', 'windowID', 'which', 'state', 'x', 'y',
        'xrel', 'yrel')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def state(self):
        return self.cdata.state

    @state.setter
    def state(self, value):
        self.cdata.state = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def xrel(self):
        return self.cdata.xrel

    @xrel.setter
    def xrel(self, value):
        self.cdata.xrel = value

    @property
    def yrel(self):
        return self.cdata.yrel

    @yrel.setter
    def yrel(self, value):
        self.cdata.yrel = value

class MouseWheelEvent(Struct):
    """Wrap `SDL_MouseWheelEvent`"""
    __ctype__ = 'SDL_MouseWheelEvent'
    _fields = 'type', 'timestamp', 'windowID', 'which', 'x', 'y'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def which(self):
        return self.cdata.which

    @which.setter
    def which(self, value):
        self.cdata.which = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

class MultiGestureEvent(Struct):
    """Wrap `SDL_MultiGestureEvent`"""
    __ctype__ = 'SDL_MultiGestureEvent'
    _fields = ('type', 'timestamp', 'touchId', 'dTheta', 'dDist', 'x', 'y',
        'numFingers', 'padding')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def touchId(self):
        return self.cdata.touchId

    @touchId.setter
    def touchId(self, value):
        self.cdata.touchId = value

    @property
    def dTheta(self):
        return self.cdata.dTheta

    @dTheta.setter
    def dTheta(self, value):
        self.cdata.dTheta = value

    @property
    def dDist(self):
        return self.cdata.dDist

    @dDist.setter
    def dDist(self, value):
        self.cdata.dDist = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def numFingers(self):
        return self.cdata.numFingers

    @numFingers.setter
    def numFingers(self, value):
        self.cdata.numFingers = value

    @property
    def padding(self):
        return self.cdata.padding

    @padding.setter
    def padding(self, value):
        self.cdata.padding = value

class OSEvent(Struct):
    """Wrap `SDL_OSEvent`"""
    __ctype__ = 'SDL_OSEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class Palette(Struct):
    """Wrap `SDL_Palette`"""
    __ctype__ = 'SDL_Palette'
    _fields = 'ncolors', 'colors', 'version', 'refcount'

    @property
    def ncolors(self):
        return self.cdata.ncolors

    @ncolors.setter
    def ncolors(self, value):
        self.cdata.ncolors = value

    @property
    def colors(self):
        return Color(self.cdata.colors) if self.cdata.colors else None

    @colors.setter
    def colors(self, value):
        try:
            self.cdata.colors = value.cdata
        except:
            self.cdata.colors = ffi.new('SDL_Color *', value)

    @property
    def version(self):
        return self.cdata.version

    @version.setter
    def version(self, value):
        self.cdata.version = value

    @property
    def refcount(self):
        return self.cdata.refcount

    @refcount.setter
    def refcount(self, value):
        self.cdata.refcount = value
    freePalette = freePalette
    setPaletteColors = setPaletteColors

class PixelFormat(Struct):
    """Wrap `SDL_PixelFormat`"""
    __ctype__ = 'SDL_PixelFormat'
    _fields = ('format', 'palette', 'BitsPerPixel', 'BytesPerPixel',
        'padding', 'Rmask', 'Gmask', 'Bmask', 'Amask', 'Rloss', 'Gloss',
        'Bloss', 'Aloss', 'Rshift', 'Gshift', 'Bshift', 'Ashift',
        'refcount', 'next')

    @property
    def format(self):
        return self.cdata.format

    @format.setter
    def format(self, value):
        self.cdata.format = value

    @property
    def palette(self):
        return Palette(self.cdata.palette) if self.cdata.palette else None

    @palette.setter
    def palette(self, value):
        try:
            self.cdata.palette = value.cdata
        except:
            self.cdata.palette = ffi.new('SDL_Palette *', value)

    @property
    def BitsPerPixel(self):
        return self.cdata.BitsPerPixel

    @BitsPerPixel.setter
    def BitsPerPixel(self, value):
        self.cdata.BitsPerPixel = value

    @property
    def BytesPerPixel(self):
        return self.cdata.BytesPerPixel

    @BytesPerPixel.setter
    def BytesPerPixel(self, value):
        self.cdata.BytesPerPixel = value

    @property
    def padding(self):
        return self.cdata.padding

    @padding.setter
    def padding(self, value):
        self.cdata.padding = value

    @property
    def Rmask(self):
        return self.cdata.Rmask

    @Rmask.setter
    def Rmask(self, value):
        self.cdata.Rmask = value

    @property
    def Gmask(self):
        return self.cdata.Gmask

    @Gmask.setter
    def Gmask(self, value):
        self.cdata.Gmask = value

    @property
    def Bmask(self):
        return self.cdata.Bmask

    @Bmask.setter
    def Bmask(self, value):
        self.cdata.Bmask = value

    @property
    def Amask(self):
        return self.cdata.Amask

    @Amask.setter
    def Amask(self, value):
        self.cdata.Amask = value

    @property
    def Rloss(self):
        return self.cdata.Rloss

    @Rloss.setter
    def Rloss(self, value):
        self.cdata.Rloss = value

    @property
    def Gloss(self):
        return self.cdata.Gloss

    @Gloss.setter
    def Gloss(self, value):
        self.cdata.Gloss = value

    @property
    def Bloss(self):
        return self.cdata.Bloss

    @Bloss.setter
    def Bloss(self, value):
        self.cdata.Bloss = value

    @property
    def Aloss(self):
        return self.cdata.Aloss

    @Aloss.setter
    def Aloss(self, value):
        self.cdata.Aloss = value

    @property
    def Rshift(self):
        return self.cdata.Rshift

    @Rshift.setter
    def Rshift(self, value):
        self.cdata.Rshift = value

    @property
    def Gshift(self):
        return self.cdata.Gshift

    @Gshift.setter
    def Gshift(self, value):
        self.cdata.Gshift = value

    @property
    def Bshift(self):
        return self.cdata.Bshift

    @Bshift.setter
    def Bshift(self, value):
        self.cdata.Bshift = value

    @property
    def Ashift(self):
        return self.cdata.Ashift

    @Ashift.setter
    def Ashift(self, value):
        self.cdata.Ashift = value

    @property
    def refcount(self):
        return self.cdata.refcount

    @refcount.setter
    def refcount(self, value):
        self.cdata.refcount = value

    @property
    def next(self):
        return PixelFormat(self.cdata.next) if self.cdata.next else None

    @next.setter
    def next(self, value):
        try:
            self.cdata.next = value.cdata
        except:
            self.cdata.next = ffi.new('SDL_PixelFormat *', value)
    freeFormat = freeFormat
    mapRGB = mapRGB
    mapRGBA = mapRGBA
    setPixelFormatPalette = setPixelFormatPalette

class Point(Struct):
    """Wrap `SDL_Point`"""
    __ctype__ = 'SDL_Point'
    _fields = 'x', 'y'

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value
    enclosePoints = enclosePoints

class QuitEvent(Struct):
    """Wrap `SDL_QuitEvent`"""
    __ctype__ = 'SDL_QuitEvent'
    _fields = 'type', 'timestamp'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

class RWops(Struct):
    """Wrap `SDL_RWops`"""
    __ctype__ = 'SDL_RWops'
    _fields = 'size', 'seek', 'read', 'write', 'close', 'type', 'hidden'

    @property
    def size(self):
        return int64_t(self.cdata.size) if self.cdata.size else None

    @size.setter
    def size(self, value):
        try:
            self.cdata.size = value.cdata
        except:
            self.cdata.size = ffi.new('int64_t *', value)

    @property
    def seek(self):
        return int64_t(self.cdata.seek) if self.cdata.seek else None

    @seek.setter
    def seek(self, value):
        try:
            self.cdata.seek = value.cdata
        except:
            self.cdata.seek = ffi.new('int64_t *', value)

    @property
    def read(self):
        return size_t(self.cdata.read) if self.cdata.read else None

    @read.setter
    def read(self, value):
        try:
            self.cdata.read = value.cdata
        except:
            self.cdata.read = ffi.new('size_t *', value)

    @property
    def write(self):
        return size_t(self.cdata.write) if self.cdata.write else None

    @write.setter
    def write(self, value):
        try:
            self.cdata.write = value.cdata
        except:
            self.cdata.write = ffi.new('size_t *', value)

    @property
    def close(self):
        return self.cdata.close

    @close.setter
    def close(self, value):
        self.cdata.close = value

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def hidden(self):
        return self.cdata.hidden

    @hidden.setter
    def hidden(self, value):
        self.cdata.hidden = value
    freeRW = freeRW
    gameControllerAddMappingsFromRW = gameControllerAddMappingsFromRW
    loadBMP_RW = loadBMP_RW
    loadWAV_RW = loadWAV_RW
    readBE16 = readBE16
    readBE32 = readBE32
    readBE64 = readBE64
    readLE16 = readLE16
    readLE32 = readLE32
    readLE64 = readLE64
    readU8 = readU8
    saveAllDollarTemplates = saveAllDollarTemplates
    writeBE16 = writeBE16
    writeBE32 = writeBE32
    writeBE64 = writeBE64
    writeLE16 = writeLE16
    writeLE32 = writeLE32
    writeLE64 = writeLE64
    writeU8 = writeU8

class Rect(Struct):
    """Wrap `SDL_Rect`"""
    __ctype__ = 'SDL_Rect'
    _fields = 'x', 'y', 'w', 'h'

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def w(self):
        return self.cdata.w

    @w.setter
    def w(self, value):
        self.cdata.w = value

    @property
    def h(self):
        return self.cdata.h

    @h.setter
    def h(self, value):
        self.cdata.h = value
    hasIntersection = hasIntersection
    intersectRect = intersectRect
    intersectRectAndLine = intersectRectAndLine
    rectEmpty = rectEmpty
    rectEquals = rectEquals
    setTextInputRect = setTextInputRect
    unionRect = unionRect

class Renderer(Struct):
    """Wrap `SDL_Renderer`"""
    __ctype__ = 'SDL_Renderer'
    _fields = ()
    createTexture = createTexture
    createTextureFromSurface = createTextureFromSurface
    destroyRenderer = destroyRenderer
    getRenderDrawBlendMode = getRenderDrawBlendMode
    getRenderDrawColor = getRenderDrawColor
    getRenderTarget = getRenderTarget
    getRendererInfo = getRendererInfo
    getRendererOutputSize = getRendererOutputSize
    renderClear = renderClear
    renderCopy = renderCopy
    renderCopyEx = renderCopyEx
    renderDrawLine = renderDrawLine
    renderDrawLines = renderDrawLines
    renderDrawPoint = renderDrawPoint
    renderDrawPoints = renderDrawPoints
    renderDrawRect = renderDrawRect
    renderDrawRects = renderDrawRects
    renderFillRect = renderFillRect
    renderFillRects = renderFillRects
    renderGetClipRect = renderGetClipRect
    renderGetLogicalSize = renderGetLogicalSize
    renderGetScale = renderGetScale
    renderGetViewport = renderGetViewport
    renderPresent = renderPresent
    renderReadPixels = renderReadPixels
    renderSetClipRect = renderSetClipRect
    renderSetLogicalSize = renderSetLogicalSize
    renderSetScale = renderSetScale
    renderSetViewport = renderSetViewport
    renderTargetSupported = renderTargetSupported
    setRenderDrawBlendMode = setRenderDrawBlendMode
    setRenderDrawColor = setRenderDrawColor
    setRenderTarget = setRenderTarget

class RendererInfo(Struct):
    """Wrap `SDL_RendererInfo`"""
    __ctype__ = 'SDL_RendererInfo'
    _fields = ('name', 'flags', 'num_texture_formats', 'texture_formats',
        'max_texture_width', 'max_texture_height')

    @property
    def name(self):
        return self.cdata.name

    @name.setter
    def name(self, value):
        self.cdata.name = value

    @property
    def flags(self):
        return self.cdata.flags

    @flags.setter
    def flags(self, value):
        self.cdata.flags = value

    @property
    def num_texture_formats(self):
        return self.cdata.num_texture_formats

    @num_texture_formats.setter
    def num_texture_formats(self, value):
        self.cdata.num_texture_formats = value

    @property
    def texture_formats(self):
        return self.cdata.texture_formats

    @texture_formats.setter
    def texture_formats(self, value):
        self.cdata.texture_formats = value

    @property
    def max_texture_width(self):
        return self.cdata.max_texture_width

    @max_texture_width.setter
    def max_texture_width(self, value):
        self.cdata.max_texture_width = value

    @property
    def max_texture_height(self):
        return self.cdata.max_texture_height

    @max_texture_height.setter
    def max_texture_height(self, value):
        self.cdata.max_texture_height = value

class Surface(Struct):
    """Wrap `SDL_Surface`"""
    __ctype__ = 'SDL_Surface'
    _fields = ('flags', 'format', 'w', 'h', 'pitch', 'pixels', 'userdata',
        'locked', 'lock_data', 'clip_rect', 'map', 'refcount')

    @property
    def flags(self):
        return self.cdata.flags

    @flags.setter
    def flags(self, value):
        self.cdata.flags = value

    @property
    def format(self):
        return PixelFormat(self.cdata.format) if self.cdata.format else None

    @format.setter
    def format(self, value):
        try:
            self.cdata.format = value.cdata
        except:
            self.cdata.format = ffi.new('SDL_PixelFormat *', value)

    @property
    def w(self):
        return self.cdata.w

    @w.setter
    def w(self, value):
        self.cdata.w = value

    @property
    def h(self):
        return self.cdata.h

    @h.setter
    def h(self, value):
        self.cdata.h = value

    @property
    def pitch(self):
        return self.cdata.pitch

    @pitch.setter
    def pitch(self, value):
        self.cdata.pitch = value

    @property
    def pixels(self):
        return self.cdata.pixels

    @pixels.setter
    def pixels(self, value):
        self.cdata.pixels = value

    @property
    def userdata(self):
        return self.cdata.userdata

    @userdata.setter
    def userdata(self, value):
        self.cdata.userdata = value

    @property
    def locked(self):
        return self.cdata.locked

    @locked.setter
    def locked(self, value):
        self.cdata.locked = value

    @property
    def lock_data(self):
        return self.cdata.lock_data

    @lock_data.setter
    def lock_data(self, value):
        self.cdata.lock_data = value

    @property
    def clip_rect(self):
        return Rect(self.cdata.clip_rect) if self.cdata.clip_rect else None

    @clip_rect.setter
    def clip_rect(self, value):
        try:
            self.cdata.clip_rect = value.cdata
        except:
            self.cdata.clip_rect = ffi.new('SDL_Rect *', value)

    @property
    def map(self):
        return self.cdata.map

    @map.setter
    def map(self, value):
        self.cdata.map = value

    @property
    def refcount(self):
        return self.cdata.refcount

    @refcount.setter
    def refcount(self, value):
        self.cdata.refcount = value
    convertSurface = convertSurface
    convertSurfaceFormat = convertSurfaceFormat
    createColorCursor = createColorCursor
    createSoftwareRenderer = createSoftwareRenderer
    fillRect = fillRect
    fillRects = fillRects
    freeSurface = freeSurface
    getClipRect = getClipRect
    getColorKey = getColorKey
    getSurfaceAlphaMod = getSurfaceAlphaMod
    getSurfaceBlendMode = getSurfaceBlendMode
    getSurfaceColorMod = getSurfaceColorMod
    lockSurface = lockSurface
    lowerBlit = lowerBlit
    lowerBlitScaled = lowerBlitScaled
    saveBMP_RW = saveBMP_RW
    setClipRect = setClipRect
    setColorKey = setColorKey
    setSurfaceAlphaMod = setSurfaceAlphaMod
    setSurfaceBlendMode = setSurfaceBlendMode
    setSurfaceColorMod = setSurfaceColorMod
    setSurfacePalette = setSurfacePalette
    setSurfaceRLE = setSurfaceRLE
    softStretch = softStretch
    unlockSurface = unlockSurface
    upperBlit = upperBlit
    upperBlitScaled = upperBlitScaled

class SysWMEvent(Struct):
    """Wrap `SDL_SysWMEvent`"""
    __ctype__ = 'SDL_SysWMEvent'
    _fields = 'type', 'timestamp', 'msg'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def msg(self):
        return SysWMmsg(self.cdata.msg) if self.cdata.msg else None

    @msg.setter
    def msg(self, value):
        try:
            self.cdata.msg = value.cdata
        except:
            self.cdata.msg = ffi.new('SDL_SysWMmsg *', value)

class SysWMmsg(Struct):
    """Wrap `SDL_SysWMmsg`"""
    __ctype__ = 'SDL_SysWMmsg'
    _fields = ()

class TextEditingEvent(Struct):
    """Wrap `SDL_TextEditingEvent`"""
    __ctype__ = 'SDL_TextEditingEvent'
    _fields = 'type', 'timestamp', 'windowID', 'text', 'start', 'length'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def text(self):
        return self.cdata.text

    @text.setter
    def text(self, value):
        self.cdata.text = value

    @property
    def start(self):
        return self.cdata.start

    @start.setter
    def start(self, value):
        self.cdata.start = value

    @property
    def length(self):
        return self.cdata.length

    @length.setter
    def length(self, value):
        self.cdata.length = value

class TextInputEvent(Struct):
    """Wrap `SDL_TextInputEvent`"""
    __ctype__ = 'SDL_TextInputEvent'
    _fields = 'type', 'timestamp', 'windowID', 'text'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def text(self):
        return self.cdata.text

    @text.setter
    def text(self, value):
        self.cdata.text = value

class Texture(Struct):
    """Wrap `SDL_Texture`"""
    __ctype__ = 'SDL_Texture'
    _fields = ()
    destroyTexture = destroyTexture
    GL_BindTexture = GL_BindTexture
    GL_UnbindTexture = GL_UnbindTexture
    getTextureAlphaMod = getTextureAlphaMod
    getTextureBlendMode = getTextureBlendMode
    getTextureColorMod = getTextureColorMod
    lockTexture = lockTexture
    queryTexture = queryTexture
    setTextureAlphaMod = setTextureAlphaMod
    setTextureBlendMode = setTextureBlendMode
    setTextureColorMod = setTextureColorMod
    unlockTexture = unlockTexture
    updateTexture = updateTexture
    updateYUVTexture = updateYUVTexture

class Thread(Struct):
    """Wrap `SDL_Thread`"""
    __ctype__ = 'SDL_Thread'
    _fields = ()
    detachThread = detachThread
    getThreadID = getThreadID
    getThreadName = getThreadName
    waitThread = waitThread

class TouchFingerEvent(Struct):
    """Wrap `SDL_TouchFingerEvent`"""
    __ctype__ = 'SDL_TouchFingerEvent'
    _fields = ('type', 'timestamp', 'touchId', 'fingerId', 'x', 'y', 'dx',
        'dy', 'pressure')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def touchId(self):
        return self.cdata.touchId

    @touchId.setter
    def touchId(self, value):
        self.cdata.touchId = value

    @property
    def fingerId(self):
        return self.cdata.fingerId

    @fingerId.setter
    def fingerId(self, value):
        self.cdata.fingerId = value

    @property
    def x(self):
        return self.cdata.x

    @x.setter
    def x(self, value):
        self.cdata.x = value

    @property
    def y(self):
        return self.cdata.y

    @y.setter
    def y(self, value):
        self.cdata.y = value

    @property
    def dx(self):
        return self.cdata.dx

    @dx.setter
    def dx(self, value):
        self.cdata.dx = value

    @property
    def dy(self):
        return self.cdata.dy

    @dy.setter
    def dy(self, value):
        self.cdata.dy = value

    @property
    def pressure(self):
        return self.cdata.pressure

    @pressure.setter
    def pressure(self, value):
        self.cdata.pressure = value

class UserEvent(Struct):
    """Wrap `SDL_UserEvent`"""
    __ctype__ = 'SDL_UserEvent'
    _fields = 'type', 'timestamp', 'windowID', 'code', 'data1', 'data2'

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def code(self):
        return self.cdata.code

    @code.setter
    def code(self, value):
        self.cdata.code = value

    @property
    def data1(self):
        return self.cdata.data1

    @data1.setter
    def data1(self, value):
        self.cdata.data1 = value

    @property
    def data2(self):
        return self.cdata.data2

    @data2.setter
    def data2(self, value):
        self.cdata.data2 = value

class Window(Struct):
    """Wrap `SDL_Window`"""
    __ctype__ = 'SDL_Window'
    _fields = ()
    createRenderer = createRenderer
    destroyWindow = destroyWindow
    GL_CreateContext = GL_CreateContext
    GL_GetDrawableSize = GL_GetDrawableSize
    GL_MakeCurrent = GL_MakeCurrent
    GL_SwapWindow = GL_SwapWindow
    getRenderer = getRenderer
    getWindowBrightness = getWindowBrightness
    getWindowData = getWindowData
    getWindowDisplayIndex = getWindowDisplayIndex
    getWindowDisplayMode = getWindowDisplayMode
    getWindowFlags = getWindowFlags
    getWindowGammaRamp = getWindowGammaRamp
    getWindowGrab = getWindowGrab
    getWindowID = getWindowID
    getWindowMaximumSize = getWindowMaximumSize
    getWindowMinimumSize = getWindowMinimumSize
    getWindowPixelFormat = getWindowPixelFormat
    getWindowPosition = getWindowPosition
    getWindowSize = getWindowSize
    getWindowSurface = getWindowSurface
    getWindowTitle = getWindowTitle
    hideWindow = hideWindow
    isScreenKeyboardShown = isScreenKeyboardShown
    maximizeWindow = maximizeWindow
    minimizeWindow = minimizeWindow
    raiseWindow = raiseWindow
    restoreWindow = restoreWindow
    setWindowBordered = setWindowBordered
    setWindowBrightness = setWindowBrightness
    setWindowData = setWindowData
    setWindowDisplayMode = setWindowDisplayMode
    setWindowFullscreen = setWindowFullscreen
    setWindowGammaRamp = setWindowGammaRamp
    setWindowGrab = setWindowGrab
    setWindowIcon = setWindowIcon
    setWindowMaximumSize = setWindowMaximumSize
    setWindowMinimumSize = setWindowMinimumSize
    setWindowPosition = setWindowPosition
    setWindowSize = setWindowSize
    setWindowTitle = setWindowTitle
    showWindow = showWindow
    updateWindowSurface = updateWindowSurface
    updateWindowSurfaceRects = updateWindowSurfaceRects
    warpMouseInWindow = warpMouseInWindow

class WindowEvent(Struct):
    """Wrap `SDL_WindowEvent`"""
    __ctype__ = 'SDL_WindowEvent'
    _fields = ('type', 'timestamp', 'windowID', 'event', 'padding1',
        'padding2', 'padding3', 'data1', 'data2')

    @property
    def type(self):
        return self.cdata.type

    @type.setter
    def type(self, value):
        self.cdata.type = value

    @property
    def timestamp(self):
        return self.cdata.timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.cdata.timestamp = value

    @property
    def windowID(self):
        return self.cdata.windowID

    @windowID.setter
    def windowID(self, value):
        self.cdata.windowID = value

    @property
    def event(self):
        return self.cdata.event

    @event.setter
    def event(self, value):
        self.cdata.event = value

    @property
    def padding1(self):
        return self.cdata.padding1

    @padding1.setter
    def padding1(self, value):
        self.cdata.padding1 = value

    @property
    def padding2(self):
        return self.cdata.padding2

    @padding2.setter
    def padding2(self, value):
        self.cdata.padding2 = value

    @property
    def padding3(self):
        return self.cdata.padding3

    @padding3.setter
    def padding3(self, value):
        self.cdata.padding3 = value

    @property
    def data1(self):
        return self.cdata.data1

    @data1.setter
    def data1(self, value):
        self.cdata.data1 = value

    @property
    def data2(self):
        return self.cdata.data2

    @data2.setter
    def data2(self, value):
        self.cdata.data2 = value

class assert_data(Struct):
    """Wrap `SDL_assert_data`"""
    __ctype__ = 'SDL_assert_data'
    _fields = ('always_ignore', 'trigger_count', 'condition', 'filename',
        'linenum', 'function', 'next')

    @property
    def always_ignore(self):
        return self.cdata.always_ignore

    @always_ignore.setter
    def always_ignore(self, value):
        self.cdata.always_ignore = value

    @property
    def trigger_count(self):
        return self.cdata.trigger_count

    @trigger_count.setter
    def trigger_count(self, value):
        self.cdata.trigger_count = value

    @property
    def condition(self):
        return self.cdata.condition

    @condition.setter
    def condition(self, value):
        self.cdata.condition = value

    @property
    def filename(self):
        return self.cdata.filename

    @filename.setter
    def filename(self, value):
        self.cdata.filename = value

    @property
    def linenum(self):
        return self.cdata.linenum

    @linenum.setter
    def linenum(self, value):
        self.cdata.linenum = value

    @property
    def function(self):
        return self.cdata.function

    @function.setter
    def function(self, value):
        self.cdata.function = value

    @property
    def next(self):
        return assert_data(self.cdata.next) if self.cdata.next else None

    @next.setter
    def next(self, value):
        try:
            self.cdata.next = value.cdata
        except:
            self.cdata.next = ffi.new('SDL_assert_data *', value)
    reportAssertion = reportAssertion

class atomic_t(Struct):
    """Wrap `SDL_atomic_t`"""
    __ctype__ = 'SDL_atomic_t'
    _fields = 'value',

    @property
    def value(self):
        return self.cdata.value

    @value.setter
    def value(self, value):
        self.cdata.value = value
    atomicAdd = atomicAdd
    atomicCAS = atomicCAS
    atomicGet = atomicGet
    atomicSet = atomicSet

class cond(Struct):
    """Wrap `SDL_cond`"""
    __ctype__ = 'SDL_cond'
    _fields = ()
    condBroadcast = condBroadcast
    condSignal = condSignal
    condWait = condWait
    condWaitTimeout = condWaitTimeout
    destroyCond = destroyCond

class mutex(Struct):
    """Wrap `SDL_mutex`"""
    __ctype__ = 'SDL_mutex'
    _fields = ()
    destroyMutex = destroyMutex
    lockMutex = lockMutex
    tryLockMutex = tryLockMutex
    unlockMutex = unlockMutex

class sem(Struct):
    """Wrap `SDL_sem`"""
    __ctype__ = 'SDL_sem'
    _fields = ()
    destroySemaphore = destroySemaphore
    semPost = semPost
    semTryWait = semTryWait
    semValue = semValue
    semWait = semWait
    semWaitTimeout = semWaitTimeout

class version(Struct):
    """Wrap `SDL_version`"""
    __ctype__ = 'SDL_version'
    _fields = 'major', 'minor', 'patch'

    @property
    def major(self):
        return self.cdata.major

    @major.setter
    def major(self, value):
        self.cdata.major = value

    @property
    def minor(self):
        return self.cdata.minor

    @minor.setter
    def minor(self, value):
        self.cdata.minor = value

    @property
    def patch(self):
        return self.cdata.patch

    @patch.setter
    def patch(self, value):
        self.cdata.patch = value
    getVersion = getVersion

blitSurface = upperBlit

# Must import after definitions due to circular dependencies
try:
    import sdl.image, sdl.ttf, sdl.mixer
except ImportError:
    pass
