from lettuce import step
from lettuce.registry import world

@step(u'Then I can select the first peasant')
def then_i_can_select_the_first_peasant(step):
    firstPlayer = world.game.getFirstPlayer()
    peasant = firstPlayer.getPeasant()
    
    peasant.select()
    
    assert peasant.isSelected()