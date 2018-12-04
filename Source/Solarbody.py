from Globals import *
# import Physics


class Solarbody:
    # Variables
    name = ""
    parent = []
    children = []
    position = []
    # Orbital Parameters
    orbit = ()
    mass = 0

    def __init__(self, newName, newParent, newPosition, numChildren):
        self.name = newName
        self.parent = newParent[:]
        self.position = newPosition[:]
        self.children = [0 for child in range(numChildren)]
        # for child in range(numChildren):
        pass  # self.children.append()
        # if self.parent.length == 0:
        #     physics.newstar(self)
        # else:
        #     physics.newplanet(self)

    def tostr(self):
        return self.name + " +" + str(len(self.children
                                          )) + " @" + str(self.position)
