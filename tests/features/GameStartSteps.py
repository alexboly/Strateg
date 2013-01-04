from lettuce import step
from lettuce.registry import world

@step(u'Then the first player has a base')
def then_the_first_player_has_a_base(step):
    assert world.firstPlayer.hasBase()

@step(u'Then the second player has a base')
def then_the_second_player_has_a_base(step):
    assert world.secondPlayer.hasBase()

@step(u'Then the first player has a peasant')
def then_the_first_player_has_a_peasant(step):
    assert world.firstPlayer.getPeasantCount() == 1
    
@step(u'Then the second player has a peasant')
def then_the_second_player_has_a_peasant(step):
    assert world.secondPlayer.getPeasantCount() == 1
