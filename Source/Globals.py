from random import Random
# if __name__ != "__main__":
from Universe import Universe
from Solarbody import Solarbody
import Physics
Rand = Random
rand = Rand.random
randi = Rand.randint
randg = Rand.gauss


# constants
# WINSIZE = [int(768 * 16.0 / 9.0), 768]  # [640, 640]
WINPOS = [(0, 0), (-1920, 0), (1366, 0)][0]
WINSIZE = (1920, 1080)
WINCENTER = (WINSIZE[0] // 2, WINSIZE[1] // 2)


# Colors
class Clr:
    # White / Greys / Black
    white = 255, 255, 255, 255
    c777 = 224, 224, 224, 255
    c666 = 192, 192, 192, 255
    c555 = 160, 160, 160, 255
    c444 = 128, 128, 128, 255
    c333 = 96, 96, 96, 255
    c222 = 64, 64, 64, 255
    c111 = 32, 32, 32, 255
    black = 0, 0, 0, 255
    # Red
    red = 255, 0, 0, 255
    # Orange / Brown
    # Yellow
    # Green
    # Blue
    # Cyan
    cyan = 0, 255, 255, 255


clr = {888: (255, 255, 255, 255)}
for r in range(9):
    for g in range(9):
        for b in range(9):
            clr[str(r * 100 + g * 10 + b)] = (
                max(255, r * 32), max(255, g * 32), max(255, b * 32), 255)

# globals
clock, screen, font = 0, 0, 0
universe, components = 0, 0

__all__ = [
    "Random", "Universe", "Solarbody", "Physics",
    "Rand", "rand", "randi", "randg",
    "WINPOS", "WINSIZE", "WINCENTER",
    "clr", "Clr",  # "white", "black", "red", "cyan",
    "clock", "screen", "font",
    "universe", "components"]
