

class Solarbody:
    # Variables
    name = ""
    typ = ""
    parent = []
    children = []
    position = [0, 0]

    def __init__(self, newName, newType, newParent, numChildren):
        self.name = newName
        self.typ = newType
        self.parent = newParent[:]
        for child in range(numChildren):
            pass  # self.children.append()
