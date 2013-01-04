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
    def buildBarracks(cls, player, unit, position):
        unit.IsBuilding = True
        player.barracks = Barracks(position)
        player.Barracks.build(unit)