from Solarbody import Solarbody


class Planet(Solarbody.Solarbody):
    pop = []
    water = []
    metals = []
    silicates = []

    def __init__(self, newName, newType, newParent, numChildren):
        super().Solarbody(self, newName, newType, newParent, numChildren)
        pass
