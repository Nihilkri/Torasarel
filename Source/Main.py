import sys
import cmath
import pygame
import pygame.locals
import json
from Globals import *
import Universe
import Solarbody


def pyinit():
    global clock, screen
    clock = pygame.time.Clock()
    # initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption("Toras'arel by Nihil K'ri")
    return


def main():
    pyinit()
    # p = WINCENTER
    running, frame = True, 0
    universe = Universe.Universe("Test", 32, 1, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed!")
                running = False
        screen.fill(black)
        # print(frame, clock, str(pygame.time.get_ticks()))
        # Draw things
        for star in universe.stars:
            pygame.draw.rect(screen, (128, 128, 128),
                             (star.position[0] - 7, star.position[1] - 7,
                              15, 15), 3)
            pygame.draw.rect(screen, (192, 192, 192),
                             (star.position[0] - 4, star.position[1] - 4,
                              10, 10), 2)
            pygame.draw.rect(screen, (255, 255, 255),
                             (star.position[0] - 2, star.position[1] - 2,
                              5, 5), 1)

        pygame.display.update()
        frame += 1
        clock.tick(10)
    comp = json.loads('"Components.json"')
    print(comp)
    print(json.dumps(comp))


# if python says run, then we should run
if __name__ == '__main__':
        main()
