from Globals import *
import math
import Solarbody
rand = Random().gauss


# Constants
G = 6.67408e-11  # m3*kg-1*s-2, Gravitational Constant


def newstar(body: Solarbody):
    # Creates a new star
    pass


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
