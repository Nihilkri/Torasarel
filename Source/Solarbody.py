

class Solarbody:
    # Variables
    name = ""
    parent = []
    children = []
    position = []

    def __init__(self, newName, newParent, newPosition, numChildren):
        self.name = newName
        self.parent = newParent[:]
        self.position = newPosition[:]
        # for child in range(numChildren):
        pass  # self.children.append()
