from random import Random
from Universe import Universe
from Solarbody import Solarbody


# constants
WINSIZE = [640, 640]
WINCENTER = [320, 320]
white = 255, 255, 255
black = 0, 0, 0

# globals
clock, screen = 0, 0
universe, components = 0, 0

__all__ = ["Random", "Universe", "Solarbody",
           "WINSIZE", "WINCENTER", "white", "black",
           "clock", "screen",
           "universe", "components"]
