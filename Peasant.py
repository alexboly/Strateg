class Peasant:
    
    def __init__(self):
        self.IsSelected = False
        self.Position = ""
    
    def select(self):
        self.IsSelected = True

    def isSelected(self):
        return self.IsSelected

    def move(self, position):
        self.Position = position