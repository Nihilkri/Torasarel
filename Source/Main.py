import sys
import cmath
import pygame
import pygame.locals
import json
import os
from Globals import *

mxy = (0, 0)
sel = -1


def pyinit():
    global clock, screen, font
    clock = pygame.time.Clock()
    # initialize and prepare screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (1366, 0)  # (2000, 250)
    pygame.init()
    font = pygame.font.SysFont("arial", 20)
    screen = pygame.display.set_mode(WINSIZE, 32)  # 32 is NoFrame
    pygame.display.set_caption("Toras'arel by Nihil K'ri")
    return


def startup():
    global universe, components
    pyinit()
    # TODO: Write JSON parser and component loader
    components = json.loads('"Components.json"')
    print(components)
    print(json.dumps(components))
    universe = Universe("Test", WINSIZE, 256, 1, 1)
    return


def gameloop():
    global sel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closed!")
            return False
        elif event.type == pygame.MOUSEMOTION:
            global mxy
            mxy = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if sel == -1:
                    print("Escape!")
                    return False
                else:
                    sel = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for star in universe.stars:
                if ((abs(mxy[0] - star.position[0]) < 15) &
                        (abs(mxy[1] - star.position[1]) < 15)):
                    sel = star
    return True


def drawframe():
    screen.fill(black)
    # print(frame, clock, str(pygame.time.get_ticks()))
    # Draw things
    pygame.draw.rect(screen, red, (WINSIZE[0] * 0.05, WINSIZE[1] * 0.05,
                                   WINSIZE[0] * 0.9, WINSIZE[1] * 0.9), 1)
    for star in universe.stars:
        if len(star.children) >= 0:
            pygame.draw.rect(screen, (255, 255, 255),
                             (star.position[0] - 2, star.position[1] - 2,
                              5, 5), 1)
        if len(star.children) >= 1:
            pygame.draw.rect(screen, (192, 192, 192),
                             (star.position[0] - 4, star.position[1] - 4,
                              10, 10), 2)
        if len(star.children) >= 5:
            pygame.draw.rect(screen, (128, 128, 128),
                             (star.position[0] - 7, star.position[1] - 7,
                              15, 15), 3)
        if ((abs(mxy[0] - star.position[0]) < 15) &
                (abs(mxy[1] - star.position[1]) < 15)):
            pygame.draw.circle(screen, cyan, star.position, 15, 1)
            frend = font.render(star.name, 1, white)
            fpos = frend.get_size()
            screen.blit(frend, (star.position[0] - fpos[0] / 2,
                                star.position[1] - fpos[1] * 2))
    pygame.draw.line(screen, cyan,
                     (mxy[0], 0), (mxy[0], WINSIZE[1]), 1)
    pygame.draw.line(screen, cyan,
                     (0, mxy[1]), (WINSIZE[0], mxy[1]), 1)
    if sel != -1:
        pygame.draw.circle(screen, red, sel.position, 15, 1)
        frend = font.render(sel.name, 1, white)
        fpos = frend.get_size()
        screen.blit(frend, (sel.position[0] - fpos[0] / 2,
                            sel.position[1] - fpos[1] * 2))
        pygame.draw.line(screen, red,
                         (sel.position[0], 0), (sel.position[0], WINSIZE[1]), 1)
        pygame.draw.line(screen, red,
                         (0, sel.position[1]), (WINSIZE[0], sel.position[1]), 1)
    pygame.display.update()
    return


def main():
    # p = WINCENTER
    startup()
    running, frame = True, 0
    while running:
        running = gameloop()
        drawframe()
        frame += 1
        clock.tick(10)


# if python says run, then we should run
if __name__ == '__main__':
        main()
