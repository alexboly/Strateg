class Peasant:
    
    def __init__(self):
        self.IsSelected = False
    
    def select(self):
        self.IsSelected = True

    def isSelected(self):
        return self.IsSelected
