from Peasant import Peasant

class Player:
    
    def __init__(self):
        self.firstPeasant = Peasant(self)
        self.HasBarracks = False
        self.Barracks = None
    
    def getPeasant(self):
        return self.firstPeasant
    
    def hasBase(self):
        return True

    def getPeasantCount(self):
        return 1
    
    def hasBarracks(self):
        return self.Barracks != None

    def getBarracks(self):
        return self.Barracks