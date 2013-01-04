from Position import InitialPosition

class Peasant:

    def __init__(self):
        self.IsSelected = False
        self.Position = InitialPosition
        self.IsBuilding = False
    
    def select(self):
        self.IsSelected = True

    def isSelected(self):
        return self.IsSelected
    
    def isBuilding(self):
        return self.IsBuilding