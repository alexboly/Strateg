from Position import InitialPosition

class Peasant:
    
    def __init__(self):
        self.IsSelected = False
        self.Position = InitialPosition
    
    def select(self):
        self.IsSelected = True

    def isSelected(self):
        return self.IsSelected

    def move(self, position):
        if self.isSelected():
            self.Position = position