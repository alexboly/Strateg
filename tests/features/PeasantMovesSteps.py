from lettuce import step
from lettuce.registry import world

@step(u'the first peasant is selected')
def then_the_first_peasant_is_selected(step):
    assert world.game.getFirstPlayer().getPeasant().isSelected()
    
@step(u'I select the first peasant')
def when_i_select_the_first_peasant(step):
    world.peasant = world.game.getFirstPlayer().getPeasant()
    
    world.peasant.select()
    
@step(u'I can move the first peasant to the location I provide')
def then_i_can_move_it_to_the_location_i_provide(step):
    world.peasant.move("position")
    
    assert world.peasant.Position == "position"