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
            pos = [(star % 3 + 1) * 160,
                   (star / 3 + 1) * 160]
            print("Planet")
            p = Solarbody(star + "", "Planet", pos, [])
            self.stars.append(p)
        for empire in range(numEmpires):
            pass  # self.empires.append()
