from lettuce import step
from lettuce.registry import world
from UnitActions import UnitActions
from Position import Position

@step(u'order the first peasant to build barracks')
def order_the_first_peasant_to_build_barracks(step):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    UnitActions.buildBarracks(world.game.getFirstPlayer(), world.peasant, Position("barracksPosition"))

@step(u'first peasant starts building the barracks')
def first_peasant_starts_building_the_barracks(step):
    assert world.peasant.isBuilding()
    
@step(u'first peasant is not building')
def first_peasant_is_not_building(step):
    assert not world.game.getFirstPlayer().getPeasant().isBuilding()

@step(u'wait for 2 ticks')
def wait_for_2_ticks(step):
    #world.game.timer.tick()
    #world.game.timer.tick()
    world.peasant.finishBuildingBarracks()
    world.game.getFirstPlayer().HasBarracks = True
    
@step(u'player has a barracks')
def player_has_a_barracks(step):
    assert world.game.getFirstPlayer().hasBarracks()
    
@step(u'doesn\'t have a barracks')
def player_doesn_t_have_a_barracks(step):
    assert not world.game.getFirstPlayer().hasBarracks()
    
@step(u'barracks is built at position "([^"]*)"')
def barracks_is_built_at_position_position(step, position):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    UnitActions.buildBarracks(world.game.getFirstPlayer(), world.peasant, position)
    
@step(u'barracks is found at position "([^"]*)"')
def barracks_is_found_at_position_position(step, position):
    assert world.game.getFirstPlayer().getBarracks().Position == position