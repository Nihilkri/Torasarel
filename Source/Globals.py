from random import Random
from Universe import Universe
from Solarbody import Solarbody


# constants
# WINSIZE = [int(768 * 16.0 / 9.0), 768]  # [640, 640]
WINSIZE = [1920, 1080]
WINCENTER = [WINSIZE[0] // 2, WINSIZE[1] // 2]
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
cyan = 0, 255, 255

# globals
clock, screen, font = 0, 0, 0
universe, components = 0, 0

__all__ = ["Random", "Universe", "Solarbody",
           "WINSIZE", "WINCENTER",
           "white", "black", "red", "cyan",
           "clock", "screen", "font",
           "universe", "components"]
