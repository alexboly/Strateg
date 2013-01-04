class Barracks:
    
    def __init__(self, unit, position):
        self.Position = position
        self.unit = unit
        self.ticksRemaining = 2
        
    def advanceBuild(self):
        if self.ticksRemaining > 0:
            self.ticksRemaining = self.ticksRemaining - 1

        if self.ticksRemaining == 0:
            self.unit.finishBuildingBarracks()
