import sys
import cmath
import random
import pygame
import pygame.locals
import Universe
import Solarbody

# constants
clock, screen = 0, 0
WINSIZE = [640, 640]
WINCENTER = [320, 320]
white = 255, 255, 255
black = 0, 0, 0


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
    universe = Universe("Test", 8, 1, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed!")
                running = False
        screen.fill(black)
        # print(frame, clock, str(pygame.time.get_ticks()))
        # Draw things
        for star in universe.stars:
            pygame.draw.rect(screen, white, (star.pos[0],
                                             star.pos[1], 5, 5), 1)

        pygame.display.update()
        frame += 1
        clock.tick(10)


# if python says run, then we should run
if __name__ == '__main__':
        main()
