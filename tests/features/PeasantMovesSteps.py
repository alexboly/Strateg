from Position import Position, InitialPosition
from lettuce import step
from lettuce.registry import world

@step(u'first peasant is selected')
def first_peasant_is_selected(step):
    assert world.firstPeasantOfFirstPlayer.isSelected()
    
@step(u'select the first peasant')
def select_the_first_peasant(step):
    world.firstPeasantOfFirstPlayer.select()
     
@step(u'can move the first peasant to the position "([^"]*)"')
def can_move_the_first_peasant_to_the_position(step, position):
    expectedPosition = Position(position)
    world.firstPeasantOfFirstPlayer.move(expectedPosition)
    
    assert world.firstPeasantOfFirstPlayer.Position == expectedPosition
    assert expectedPosition != InitialPosition
    
@step(u'move the first peasant')
def move_the_first_peasant(step):
    world.firstPeasantOfFirstPlayer.move("position")
    
@step(u'first peasant doesn\'t move')
def first_peasant_doesn_t_move(step):
    assert not world.firstPeasantOfFirstPlayer.isSelected()
    assert world.firstPeasantOfFirstPlayer.Position == InitialPosition
