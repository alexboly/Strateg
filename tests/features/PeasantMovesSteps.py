from lettuce import step
from lettuce.registry import world
from Position import Position, InitialPosition

@step(u'first peasant is selected')
def first_peasant_is_selected(step):
    assert world.game.getFirstPlayer().getPeasant().isSelected()
    
@step(u'select the first peasant')
def select_the_first_peasant(step):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    
    world.peasant.select()
     
@step(u'can move the first peasant to the position "([^"]*)"')
def can_move_the_first_peasant_to_the_position(step, position):
    expectedPosition = Position(position)
    world.peasant.move(expectedPosition)
    
    assert world.peasant.Position == expectedPosition
    assert expectedPosition != InitialPosition
    
@step(u'move the first peasant')
def move_the_first_peasant(step):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    world.peasant.move("position")
    
@step(u'first peasant doesn\'t move')
def first_peasant_doesn_t_move(step):
    assert not world.peasant.isSelected()
    assert world.peasant.Position == InitialPosition
