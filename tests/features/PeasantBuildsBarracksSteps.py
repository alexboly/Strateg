from lettuce import step
from lettuce.registry import world
from UnitActions import UnitActions
from Position import Position

@step(u'order the first peasant to build barracks')
def order_the_first_peasant_to_build_barracks(step):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    UnitActions.buildBarracks(world.peasant, Position("barracksPosition"))

@step(u'first peasant starts building the barracks')
def first_peasant_starts_building_the_barracks(step):
    assert world.peasant.isBuilding()
    
@step(u'first peasant is not building')
def first_peasant_is_not_building(step):
    assert not world.game.getFirstPlayer().getPeasant().isBuilding()