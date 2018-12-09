# import Globals
from Globals import *
import math
from random import Random
from Solarbody import Solarbody
Rand = Random()
randi = Rand.randint
randg = Rand.gauss


# Constants
G = 6.67408e-11  # m3*kg-1*s-2, Gravitational Constant


def rand(a: float, b: float):
    return a + (b - a) * Rand.random()


def newuniverse(usize, numStars, numAveragePlanets):
    # Creates the universe from scratch, starting with the apple pie
    applepie = 1
    stars = []
    # Select the style of universe
    # 0 = Randomized
    # 1 = Spaced
    # 2 = Sectioned
    # 3 = Gaussian Globular Cluster
    # 4 = Keplerian Globular Cluster
    # 5 = Spiral Galaxy
    UniverseStyle = 1
    if UniverseStyle == 0:
        for i in range(numStars):
            # pos = [rand(int(usize[0] * 0.05), int(usize[0] * 0.95)),
            #        rand(int(usize[1] * 0.05), int(usize[1] * 0.95))]
            pos = [int(usize[0] * rand(0.05, 0.95)),
                   int(usize[1] * rand(0.05, 0.95)), 0, 0]
            # print(str(star) + " " + str(pos))
            stars.append(newstar(i, pos))
    elif UniverseStyle == 1:
        for i in range(numStars):
            clear = False
            for tries in range(numStars):
                clear = True
                # pos = [rand(int(usize[0] * 0.05), int(usize[0] * 0.95)),
                #        rand(int(usize[1] * 0.05), int(usize[1] * 0.95))]
                pos = [int(usize[0] * rand(0.05, 0.95)),
                       int(usize[1] * rand(0.05, 0.95)), 0, 0]
                for ii in range(i):
                    iipos = stars[ii].position
                    d = ((pos[0] - iipos[0]) ** 2 +
                         (pos[1] - iipos[1]) ** 2) ** 0.5
                    if d < 30:
                        # print("Collision between new star", i, "at", pos[:2],
                        #       "and ", ii, "at", iipos[:2], d)
                        clear = False
                        break
                if clear:
                    # print("Star", i, "successful at", pos[:2])
                    break
            if not clear:
                print("Ran out of tries at star", i)
                numStars = i - 1
                break
            # print(str(star) + " " + str(pos))
            stars.append(newstar(i, pos))
    elif UniverseStyle == 2:
        pass
    elif UniverseStyle == 3:
        pass
    elif UniverseStyle == 4:
        pass
    elif UniverseStyle == 5:
        pass
    elif UniverseStyle == 6:
        pass
    else:
        pass
    return stars


def newstar(num: int, pos: list):
    # Creates a new star
    c = randi(0, 8)
    return Solarbody("Star " + str(num), [], pos, c)


def newplanet(body: Solarbody):
    # Creates a new planet
    mass = 5.97237e21 * rand(55, 317800)  # Between Mercury and Jupiter
    orbit = physics.neworbit()


def neworbit(body: Solarbody):
    # Calculates a new randomized orbit for new solar bodies
    m, M = body.mass, body.parent.mass

    # Semimajor axis (a)-the sum of the periapsis
    # and apoapsis distances divided by two
    a = 100

    # Eccentricity (e)-shape of the ellipse, describing
    # how much it is elongated compared to a circle
    e = -G * (m + M) / 2 / a

    # Inclination (i)-vertical tilt of the ellipse
    # with respect to the reference plane, measured at the ascending node

    # Longitude of the ascending node (o)-horizontally orients the ascending
    # node of the ellipse with respect to the reference frame's vernal point

    # Argument of periapsis (w) is the orientation of the ellipse in the orbital
    # plane, as an angle measured from the ascending node to the periapsis

    # True anomaly (f) defines the position of the orbiting body
    # along the ellipse at a t = 0


def pos(body: Solarbody, t: int, win: list):
    # Computes the real position of a solar body
    # based on the orbital parameters at time t
    e, a, i, o, w, th = body.orbit
    X, Y, Z = pos(body.parent, t, win)
