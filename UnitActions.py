from Barracks import Barracks
class UnitActions:

    @staticmethod
    def canMove(unit):
        return unit.isSelected()

    @staticmethod
    def move(unit, position):
        if UnitActions.canMove(unit):
            unit.Position = position
    
    @classmethod
    def buildBarracks(cls, game, player, unit, position):
        unit.IsBuilding = True
        player.Barracks = Barracks(unit, position)
        game.Timer.CallOnTick = player.Barracks.advanceBuild