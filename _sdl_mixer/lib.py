# Names to expose to the outside

from .constants import *
from .autohelpers import *

def Mix_PlayChannel(channel, chunk, loops):
    return Mix_PlayChannelTimed(channel, chunk, loops, -1)