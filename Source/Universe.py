from Globals import *
import Solarbody


class Universe:
    # Variables
    gamename = ""
    stars = []
    AveragePlanets = []
    empires = []

    def __init__(self, newGameName, numStars,
                 numAveragePlanets, numEmpires):
        self.gamename = newGameName
        for star in range(numStars):
            pos = [rand(640 * 0.1, 640 * 0.9), rand(640 * 0.1, 640 * 0.9)]
            print(str(star) + " " + str(pos))
            p = Solarbody.Solarbody("Planet " + str(star), [], pos, 0)
            self.stars.append(p)
        for empire in range(numEmpires):
            pass  # self.empires.append()
