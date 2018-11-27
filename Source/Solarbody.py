from Globals import *
import physics


class Solarbody:
    # Variables
    name = ""
    parent = []
    children = []
    position = []
    # Orbital Parameters
    orbit = (,)
    mass = 0

    def __init__(self, newName, newParent, newPosition, numChildren):
        self.name = newName
        self.parent = newParent[:]
        self.position = newPosition[:]
        # for child in range(numChildren):
        pass  # self.children.append()
        if self.parent.length == 0:
            physics.newstar(self)
        else
            physics.newplanet(self)


