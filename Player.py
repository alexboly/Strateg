from Peasant import Peasant

class Player:
    
    def __init__(self):
        self.firstPeasant = Peasant()
    
    def getPeasant(self):
        return self.firstPeasant
    
    def hasBase(self):
        return True

    def getPeasantCount(self):
        return 1
