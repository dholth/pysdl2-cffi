# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl_ttf import ffi, lib
from _sdl_ttf.structs import unbox, Struct
from _sdl.structs import u8, SDLError
# ttf needs the aliases for now...
from sdl import Surface as SDL_Surface, version as SDL_version

def byteSwappedUNICODE(swapped):
    """
    ``void TTF_ByteSwappedUNICODE(int)``
    """
    swapped_c = swapped
    lib.TTF_ByteSwappedUNICODE(swapped_c)

def closeFont(font):
    """
    ``void TTF_CloseFont(TTF_Font *)``
    """
    font_c = unbox(font, 'TTF_Font *')
    lib.TTF_CloseFont(font_c)

def fontAscent(font):
    """
    ``int TTF_FontAscent(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontAscent(font_c)
    return rc

def fontDescent(font):
    """
    ``int TTF_FontDescent(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontDescent(font_c)
    return rc

def fontFaceFamilyName(font):
    """
    ``char * TTF_FontFaceFamilyName(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontFaceFamilyName(font_c)
    return ffi.string(rc).decode('utf-8')

def fontFaceIsFixedWidth(font):
    """
    ``int TTF_FontFaceIsFixedWidth(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontFaceIsFixedWidth(font_c)
    return rc

def fontFaceStyleName(font):
    """
    ``char * TTF_FontFaceStyleName(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontFaceStyleName(font_c)
    return ffi.string(rc).decode('utf-8')

def fontFaces(font):
    """
    ``long TTF_FontFaces(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontFaces(font_c)
    return rc

def fontHeight(font):
    """
    ``int TTF_FontHeight(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontHeight(font_c)
    return rc

def fontLineSkip(font):
    """
    ``int TTF_FontLineSkip(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_FontLineSkip(font_c)
    return rc

def getFontHinting(font):
    """
    ``int TTF_GetFontHinting(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_GetFontHinting(font_c)
    return rc

def getFontKerning(font):
    """
    ``int TTF_GetFontKerning(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_GetFontKerning(font_c)
    return rc

def getFontKerningSize(font, prev_index, index):
    """
    ``int TTF_GetFontKerningSize(TTF_Font *, int, int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    prev_index_c = prev_index
    index_c = index
    rc = lib.TTF_GetFontKerningSize(font_c, prev_index_c, index_c)
    return rc

def getFontOutline(font):
    """
    ``int TTF_GetFontOutline(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_GetFontOutline(font_c)
    return rc

def getFontStyle(font):
    """
    ``int TTF_GetFontStyle(TTF_Font const *)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    rc = lib.TTF_GetFontStyle(font_c)
    return rc

def glyphIsProvided(font, ch):
    """
    ``int TTF_GlyphIsProvided(TTF_Font const *, unsigned short)``
    """
    font_c = unbox(font, 'TTF_Font const *')
    ch_c = ch
    rc = lib.TTF_GlyphIsProvided(font_c, ch_c)
    return rc

def glyphMetrics(font, ch, minx=None, maxx=None, miny=None, maxy=None, advance=None):
    """
    ``int TTF_GlyphMetrics(TTF_Font *, unsigned short, int *, int *, int *, int *, int *)``
    """
    font_c = unbox(font, 'TTF_Font *')
    ch_c = ch
    minx_c = unbox(minx, 'int *')
    maxx_c = unbox(maxx, 'int *')
    miny_c = unbox(miny, 'int *')
    maxy_c = unbox(maxy, 'int *')
    advance_c = unbox(advance, 'int *')
    rc = lib.TTF_GlyphMetrics(font_c, ch_c, minx_c, maxx_c, miny_c, maxy_c, advance_c)
    return (rc, minx_c[0], maxx_c[0], miny_c[0], maxy_c[0], advance_c[0])

def init():
    """
    ``int TTF_Init(void)``
    """
    rc = lib.TTF_Init()
    if rc == -1: raise SDLError()
    return rc

def linked_Version():
    """
    ``SDL_version const * TTF_Linked_Version(void)``
    """
    rc = lib.TTF_Linked_Version()
    return SDL_version(rc)

def openFont(file, ptsize):
    """
    ``TTF_Font * TTF_OpenFont(char const *, int)``
    """
    file_c = u8(file)
    ptsize_c = ptsize
    rc = lib.TTF_OpenFont(file_c, ptsize_c)
    if rc == ffi.NULL: raise SDLError()
    return Font(rc)

def openFontIndex(file, ptsize, index):
    """
    ``TTF_Font * TTF_OpenFontIndex(char const *, int, long)``
    """
    file_c = u8(file)
    ptsize_c = ptsize
    index_c = index
    rc = lib.TTF_OpenFontIndex(file_c, ptsize_c, index_c)
    if rc == ffi.NULL: raise SDLError()
    return Font(rc)

def openFontIndexRW(src, freesrc, ptsize, index):
    """
    ``TTF_Font * TTF_OpenFontIndexRW(SDL_RWops *, int, int, long)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    ptsize_c = ptsize
    index_c = index
    rc = lib.TTF_OpenFontIndexRW(src_c, freesrc_c, ptsize_c, index_c)
    if rc == ffi.NULL: raise SDLError()
    return Font(rc)

def openFontRW(src, freesrc, ptsize):
    """
    ``TTF_Font * TTF_OpenFontRW(SDL_RWops *, int, int)``
    """
    src_c = unbox(src, 'SDL_RWops *')
    freesrc_c = freesrc
    ptsize_c = ptsize
    rc = lib.TTF_OpenFontRW(src_c, freesrc_c, ptsize_c)
    if rc == ffi.NULL: raise SDLError()
    return Font(rc)

def quit():
    """
    ``void TTF_Quit(void)``
    """
    lib.TTF_Quit()

def renderGlyph_Blended(font, ch, fg):
    """
    ``SDL_Surface * TTF_RenderGlyph_Blended(TTF_Font *, unsigned short, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    ch_c = ch
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderGlyph_Blended(font_c, ch_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderGlyph_Shaded(font, ch, fg, bg):
    """
    ``SDL_Surface * TTF_RenderGlyph_Shaded(TTF_Font *, unsigned short, SDL_Color, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    ch_c = ch
    fg_c = unbox(fg, 'SDL_Color')
    bg_c = unbox(bg, 'SDL_Color')
    rc = lib.TTF_RenderGlyph_Shaded(font_c, ch_c, fg_c, bg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderGlyph_Solid(font, ch, fg):
    """
    ``SDL_Surface * TTF_RenderGlyph_Solid(TTF_Font *, unsigned short, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    ch_c = ch
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderGlyph_Solid(font_c, ch_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderText_Blended(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderText_Blended(TTF_Font *, char const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderText_Blended(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderText_Blended_Wrapped(font, text, fg, wrapLength):
    """
    ``SDL_Surface * TTF_RenderText_Blended_Wrapped(TTF_Font *, char const *, SDL_Color, unsigned int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    wrapLength_c = wrapLength
    rc = lib.TTF_RenderText_Blended_Wrapped(font_c, text_c, fg_c, wrapLength_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderText_Shaded(font, text, fg, bg):
    """
    ``SDL_Surface * TTF_RenderText_Shaded(TTF_Font *, char const *, SDL_Color, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    bg_c = unbox(bg, 'SDL_Color')
    rc = lib.TTF_RenderText_Shaded(font_c, text_c, fg_c, bg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderText_Solid(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderText_Solid(TTF_Font *, char const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderText_Solid(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUNICODE_Blended(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderUNICODE_Blended(TTF_Font *, unsigned short const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = unbox(text, 'unsigned short const *')
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderUNICODE_Blended(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUNICODE_Blended_Wrapped(font, text, fg, wrapLength):
    """
    ``SDL_Surface * TTF_RenderUNICODE_Blended_Wrapped(TTF_Font *, unsigned short const *, SDL_Color, unsigned int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = unbox(text, 'unsigned short const *')
    fg_c = unbox(fg, 'SDL_Color')
    wrapLength_c = wrapLength
    rc = lib.TTF_RenderUNICODE_Blended_Wrapped(font_c, text_c, fg_c, wrapLength_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUNICODE_Shaded(font, text, fg, bg):
    """
    ``SDL_Surface * TTF_RenderUNICODE_Shaded(TTF_Font *, unsigned short const *, SDL_Color, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = unbox(text, 'unsigned short const *')
    fg_c = unbox(fg, 'SDL_Color')
    bg_c = unbox(bg, 'SDL_Color')
    rc = lib.TTF_RenderUNICODE_Shaded(font_c, text_c, fg_c, bg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUNICODE_Solid(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderUNICODE_Solid(TTF_Font *, unsigned short const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = unbox(text, 'unsigned short const *')
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderUNICODE_Solid(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUTF8_Blended(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderUTF8_Blended(TTF_Font *, char const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderUTF8_Blended(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUTF8_Blended_Wrapped(font, text, fg, wrapLength):
    """
    ``SDL_Surface * TTF_RenderUTF8_Blended_Wrapped(TTF_Font *, char const *, SDL_Color, unsigned int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    wrapLength_c = wrapLength
    rc = lib.TTF_RenderUTF8_Blended_Wrapped(font_c, text_c, fg_c, wrapLength_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUTF8_Shaded(font, text, fg, bg):
    """
    ``SDL_Surface * TTF_RenderUTF8_Shaded(TTF_Font *, char const *, SDL_Color, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    bg_c = unbox(bg, 'SDL_Color')
    rc = lib.TTF_RenderUTF8_Shaded(font_c, text_c, fg_c, bg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def renderUTF8_Solid(font, text, fg):
    """
    ``SDL_Surface * TTF_RenderUTF8_Solid(TTF_Font *, char const *, SDL_Color)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    fg_c = unbox(fg, 'SDL_Color')
    rc = lib.TTF_RenderUTF8_Solid(font_c, text_c, fg_c)
    if rc == ffi.NULL: raise SDLError()
    return SDL_Surface(rc)

def setFontHinting(font, hinting):
    """
    ``void TTF_SetFontHinting(TTF_Font *, int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    hinting_c = hinting
    lib.TTF_SetFontHinting(font_c, hinting_c)

def setFontKerning(font, allowed):
    """
    ``void TTF_SetFontKerning(TTF_Font *, int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    allowed_c = allowed
    lib.TTF_SetFontKerning(font_c, allowed_c)

def setFontOutline(font, outline):
    """
    ``void TTF_SetFontOutline(TTF_Font *, int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    outline_c = outline
    lib.TTF_SetFontOutline(font_c, outline_c)

def setFontStyle(font, style):
    """
    ``void TTF_SetFontStyle(TTF_Font *, int)``
    """
    font_c = unbox(font, 'TTF_Font *')
    style_c = style
    lib.TTF_SetFontStyle(font_c, style_c)

def sizeText(font, text, w=None, h=None):
    """
    ``int TTF_SizeText(TTF_Font *, char const *, int *, int *)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    rc = lib.TTF_SizeText(font_c, text_c, w_c, h_c)
    return (rc, w_c[0], h_c[0])

def sizeUNICODE(font, text=None, w=None, h=None):
    """
    ``int TTF_SizeUNICODE(TTF_Font *, unsigned short const *, int *, int *)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = unbox(text, 'unsigned short const *')
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    rc = lib.TTF_SizeUNICODE(font_c, text_c, w_c, h_c)
    return (rc, text_c[0], w_c[0], h_c[0])

def sizeUTF8(font, text, w=None, h=None):
    """
    ``int TTF_SizeUTF8(TTF_Font *, char const *, int *, int *)``
    """
    font_c = unbox(font, 'TTF_Font *')
    text_c = u8(text)
    w_c = unbox(w, 'int *')
    h_c = unbox(h, 'int *')
    rc = lib.TTF_SizeUTF8(font_c, text_c, w_c, h_c)
    return (rc, w_c[0], h_c[0])

def wasInit():
    """
    ``int TTF_WasInit(void)``
    """
    rc = lib.TTF_WasInit()
    return rc

class Font(Struct):
    """Wrap `TTF_Font`"""
    __ctype__ = 'TTF_Font'
    _fields = ()
    closeFont = closeFont
    fontAscent = fontAscent
    fontDescent = fontDescent
    fontFaceFamilyName = fontFaceFamilyName
    fontFaceIsFixedWidth = fontFaceIsFixedWidth
    fontFaceStyleName = fontFaceStyleName
    fontFaces = fontFaces
    fontHeight = fontHeight
    fontLineSkip = fontLineSkip
    getFontHinting = getFontHinting
    getFontKerning = getFontKerning
    getFontKerningSize = getFontKerningSize
    getFontOutline = getFontOutline
    getFontStyle = getFontStyle
    glyphIsProvided = glyphIsProvided
    glyphMetrics = glyphMetrics
    renderGlyph_Blended = renderGlyph_Blended
    renderGlyph_Shaded = renderGlyph_Shaded
    renderGlyph_Solid = renderGlyph_Solid
    renderText_Blended = renderText_Blended
    renderText_Blended_Wrapped = renderText_Blended_Wrapped
    renderText_Shaded = renderText_Shaded
    renderText_Solid = renderText_Solid
    renderUNICODE_Blended = renderUNICODE_Blended
    renderUNICODE_Blended_Wrapped = renderUNICODE_Blended_Wrapped
    renderUNICODE_Shaded = renderUNICODE_Shaded
    renderUNICODE_Solid = renderUNICODE_Solid
    renderUTF8_Blended = renderUTF8_Blended
    renderUTF8_Blended_Wrapped = renderUTF8_Blended_Wrapped
    renderUTF8_Shaded = renderUTF8_Shaded
    renderUTF8_Solid = renderUTF8_Solid
    setFontHinting = setFontHinting
    setFontKerning = setFontKerning
    setFontOutline = setFontOutline
    setFontStyle = setFontStyle
    sizeText = sizeText
    sizeUNICODE = sizeUNICODE
    sizeUTF8 = sizeUTF8

