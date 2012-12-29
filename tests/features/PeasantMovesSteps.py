from lettuce import step
from lettuce.registry import world

@step(u'Then I can select the first peasant')
def then_i_can_select_the_first_peasant(step):
    firstPlayer = world.game.getFirstPlayer()
    peasant = firstPlayer.getPeasant()
    
    peasant.select()
    
    assert peasant.isSelected()
    
@step(u'When I select the first peasant')
def when_i_select_the_first_peasant(step):
    firstPlayer = world.game.getFirstPlayer()
    world.peasant = firstPlayer.getPeasant()
    
    world.peasant.select()
    
    
@step(u'Then I can move it to the location I provide')
def then_i_can_move_it_to_the_location_i_provide(step):
    world.peasant.move("position")
    
    assert world.peasant.Position == "position"