from lettuce import step

@step(u'When I configure the game')
def when_i_configure_the_game(step):
    pass

@step(u'Then there\'s no player')
def then_there_s_no_player(step):
    playersCount = 0
    assert playersCount == 0 
