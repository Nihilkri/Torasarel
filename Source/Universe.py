from Globals import *
import Physics
# from Solarbody import Solarbody
# from random import Random
# rand = Random().randint


class Universe:
    # Variables
    gamename = ""
    stars = []
    AveragePlanets = []
    empires = []

    def __init__(self, newGameName, usize, numStars,
                 numAveragePlanets, numEmpires):
        self.gamename = newGameName
        print(usize)
        print(dir())
        self.stars = Physics.newuniverse(usize, numStars, numAveragePlanets)

        # print([star.tostr() for star in self.stars])
        for empire in range(numEmpires):
            pass  # self.empires.append()
