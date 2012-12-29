class UnitActions:

    @staticmethod
    def canMove(unit):
        return unit.isSelected()

    @staticmethod
    def move(unit, position):
        if UnitActions.canMove(unit):
            unit.Position = position