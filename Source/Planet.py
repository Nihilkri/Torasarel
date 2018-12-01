from Globals import *


class Planet(Solarbody.Solarbody):
    # Materials are 2d arrays for subsurface and surface versions
    name = ""
    water = [100, 10]
    metals = [100, 10]
    silicates = [100, 10]

    def __init__(self, newName, newParent, numChildren):
        super().Solarbody(self, newName, newParent, numChildren)
        pass
