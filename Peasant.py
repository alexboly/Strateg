from Barracks import Barracks
from Position import InitialPosition

class Peasant:

    def __init__(self, player):
        self.player = player
        self.IsSelected = False
        self.Position = InitialPosition
        self.IsBuilding = False
    
    def select(self):
        self.IsSelected = True

    def isSelected(self):
        return self.IsSelected
    
    def canMove(self):
        return self.isSelected()

    def move(self, position):
        if self.canMove():
            self.Position = position

    def isBuilding(self):
        return self.IsBuilding
    
    def buildBarracks(self, gameTimer, position):
        self.startBuildingBarracks(position)
        gameTimer.CallOnTick = self.advanceBuild
    
    def startBuildingBarracks(self, position):
        self.ticksRemaining = Barracks.ticksRequired
        self.IsBuilding = True
        self.player.Barracks = Barracks(position)
    
    def finishBuildingBarracks(self):
        self.IsBuilding = False

    def advanceBuild(self):
        if self.ticksRemaining > 0:
            self.ticksRemaining = self.ticksRemaining - 1

        if self.ticksRemaining == 0:
            self.finishBuildingBarracks()
