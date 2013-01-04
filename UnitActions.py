class UnitActions:

    @staticmethod
    def canMove(unit):
        return unit.isSelected()

    @staticmethod
    def move(unit, position):
        if UnitActions.canMove(unit):
            unit.Position = position
    
    @classmethod
    def buildBarracks(cls, unit, position):
        unit.IsBuilding = True
    
    
