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
    global clock, screen, font, WINSIZE
    clock = pygame.time.Clock()
    # initialize and prepare screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % WINPOS
    pygame.init()
    font = pygame.font.SysFont("lucida console", 24, True)
    print("WINSIZE, WINPOS, WINCENTER = ", WINSIZE, WINPOS, WINCENTER)
    print("Display = ", pygame.display)
    infoObject = pygame.display.Info()
    WINSIZE = (infoObject.current_w, infoObject.current_h)
    print("WINSIZE = ", WINSIZE)
    print("infoObject = ", infoObject)
    print("Modes = ", pygame.display.list_modes())
    print("WMinfo = ", pygame.display.get_wm_info())
    # WINSIZE = (640, 640)
    screen = pygame.display.set_mode(WINSIZE, 32)  # 32 is NoFrame
    pygame.display.set_caption("Toras'arel by Nihil K'ri")
    return


def startup():
    global universe, components, sel
    pyinit()
    # TODO: Write JSON parser and component loader
    with open("Components.json", "r") as jsonfile:
        components = json.load(jsonfile)
    if False:
        # print(components)
        # print(json.dumps(components))
        print("Components:")
        for key in iter(components):
            print(key + " :")
            for key2 in iter(components[key]):
                print("    " + key2 + " :")
                for key3 in iter(components[key][key2]):
                    print("        " + key3 + " :", components[key][key2][key3])
    universe = Universe("Test", WINSIZE, 256, 1, 1)
    sel = universe.stars[0]
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
            # else:
            #     for key in pygame.key.get_pressed():
            #         print(key)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for star in universe.stars:
                if ((abs(mxy[0] - star.position[0]) < 15) &
                        (abs(mxy[1] - star.position[1]) < 15)):
                    sel = star
    return True


def drawframe():
    screen.fill(0x000000)
    # print(frame, clock, str(pygame.time.get_ticks()))
    # Draw things
    pygame.draw.rect(screen, 0x800000, (WINSIZE[0] * 0.05, WINSIZE[1] * 0.05,
                                        WINSIZE[0] * 0.9, WINSIZE[1] * 0.9), 1)
    for star in universe.stars:
        if len(star.children) >= 0:
            pygame.draw.rect(screen, 0xFFFFFF,
                             (star.position[0] - 2, star.position[1] - 2,
                              5, 5), 1)
        if len(star.children) >= 1:
            pygame.draw.rect(screen, 0xC0C0C0,
                             (star.position[0] - 4, star.position[1] - 4,
                              10, 10), 2)
        if len(star.children) >= 5:
            pygame.draw.rect(screen, 0x808080,
                             (star.position[0] - 7, star.position[1] - 7,
                              15, 15), 3)
    pygame.draw.line(screen, 0x00FFFF,
                     (mxy[0], 0), (mxy[0], WINSIZE[1]), 1)
    pygame.draw.line(screen, 0x00FFFF,
                     (0, mxy[1]), (WINSIZE[0], mxy[1]), 1)
    if sel != -1:
        pygame.draw.circle(screen, 0xFF0000, sel.position[:2], 15, 1)
        frend = font.render(sel.tostr(), 1, (255, 0, 0), (64, 64, 64))
        fpos = frend.get_size()
        screen.blit(frend, (sel.position[0] - fpos[0] / 2,
                            sel.position[1] - fpos[1] * 2))
        pygame.draw.line(screen, 0xFF0000,
                         (sel.position[0], 0), (sel.position[0], WINSIZE[1]), 1)
        pygame.draw.line(screen, 0xFF0000,
                         (0, sel.position[1]), (WINSIZE[0], sel.position[1]), 1)
    for star in universe.stars:
        if ((abs(mxy[0] - star.position[0]) < 15) &
                (abs(mxy[1] - star.position[1]) < 15)):
            pygame.draw.circle(screen, 0x00FFFF, star.position[:2], 15, 1)
            frend = font.render(star.tostr(), 1,
                                (0, 0, 0), (192, 192, 192))
            fpos = frend.get_size()
            ful = (star.position[0] - fpos[0] / 2,
                   star.position[1] - fpos[1] * 2)
            screen.fill((192, 0, 0),
                        (ful[0] - 2, ful[1] - 5, fpos[0] + 4, fpos[1] + 7))
            screen.blit(frend, ful)
    # TODO: Draw the fps
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
    pygame.display.quit()


# if python says run, then we should run
if __name__ == '__main__':
        main()
