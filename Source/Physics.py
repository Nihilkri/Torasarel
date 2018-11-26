from Globals import *
import math
import Solarbody


# Constants
G = 0


def neworbit():
    # Calculates a new randomized orbit for new solar bodies
    # Eccentricity (e)—shape of the ellipse, describing how much it is elongated compared to a circle
    e = rand(0, 100) / 100
    # Semimajor axis (a)—the sum of the periapsis and apoapsis distances divided by two
    # Inclination (i)—vertical tilt of the ellipse with respect to the reference plane, measured at the ascending node
    # Longitude of the ascending node (o)—horizontally orients the ascending node of the ellipse with respect to the reference frame's vernal point
    # Argument of periapsis (w) defines the orientation of the ellipse in the orbital plane, as an angle measured from the ascending node to the periapsis
    # True anomaly (f) defines the position of the orbiting body along the ellipse at a t = 0

def pos(body: Solarbody, t: int, win: rect):
    # Computes the real position of a solar body based on the orbital parameters at time t
    e, a, i, o, w, th = body.orbit
    X, Y, Z = pos(body.parent, t, win)



# https://en.wikipedia.org/wiki/Orbital_elements
# https://en.wikipedia.org/wiki/Equinox#Celestial_coordinate_systems
# https://en.wikipedia.org/wiki/Orbital_eccentricity
# https://en.wikipedia.org/wiki/Reduced_mass
# https://en.wikipedia.org/wiki/Specific_orbital_energy
# https://en.wikipedia.org/wiki/Gravitational_constant
# https://www.pygame.org/docs/ref/time.html
# https://docs.python.org/3/library/sys.html#module-sys
# https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python