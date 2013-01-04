from Peasant import Peasant
from Barracks import Barracks

class Player:
    
    def __init__(self):
        self.firstPeasant = Peasant()
        self.HasBarracks = False
        self.Barracks = Barracks("BarracksPosition")
    
    def getPeasant(self):
        return self.firstPeasant
    
    def hasBase(self):
        return True

    def getPeasantCount(self):
        return 1
    
    def hasBarracks(self):
        return self.HasBarracks

    def getBarracks(self):
        return self.Barracks