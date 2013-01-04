from lettuce import step
from lettuce.registry import world
from UnitActions import UnitActions

@step(u'order the first peasant to build barracks')

def buildBarracksAtPosition(position):
    return UnitActions.buildBarracks(world.game, world.firstPlayer, world.firstPeasantOfFirstPlayer, position)

def order_the_first_peasant_to_build_barracks(step):
    buildBarracksAtPosition("barracksPosition")

@step(u'first peasant starts building the barracks')
def first_peasant_starts_building_the_barracks(step):
    assert world.firstPeasantOfFirstPlayer.isBuilding()
    
@step(u'first peasant is not building')
def first_peasant_is_not_building(step):
    assert not world.firstPeasantOfFirstPlayer.isBuilding()

@step(u'wait for 2 ticks')
def wait_for_2_ticks(step):
    world.game.Timer.tick()
    world.game.Timer.tick()
    
@step(u'player has a barracks')
def player_has_a_barracks(step):
    assert world.firstPlayer.hasBarracks()
    
@step(u'doesn\'t have a barracks')
def player_doesn_t_have_a_barracks(step):
    assert not world.firstPlayer.hasBarracks()
    
@step(u'barracks is built at position "([^"]*)"')
def barracks_is_built_at_position_position(step, position):
    buildBarracksAtPosition(position)
    
@step(u'barracks is found at position "([^"]*)"')
def barracks_is_found_at_position_position(step, position):
    assert world.firstPlayer.getBarracks().Position == position
