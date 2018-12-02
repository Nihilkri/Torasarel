from Globals import *
from Solarbody import Solarbody
rand = Random().randint


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
        for star in range(numStars):
            pos = [rand(int(usize[0] * 0.05), int(usize[0] * 0.95)),
                   rand(int(usize[1] * 0.05), int(usize[1] * 0.95))]
            # print(str(star) + " " + str(pos))
            c = rand(0, 8)
            p = Solarbody("Star " + str(star) + ", " + str(c), [], pos, c)
            self.stars.append(p)
        print([star.tostr() for star in self.stars])
        for empire in range(numEmpires):
            pass  # self.empires.append()
