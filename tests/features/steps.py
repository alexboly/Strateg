from lettuce import step

playersCount = 0
computerPlayers = 0

@step(u'When I configure the game')
def when_i_configure_the_game(step):
    pass

@step(u'Then there\'s no player')
def then_there_s_no_player(step):
    assert playersCount == 0 

@step(u'When I add a computer player')
def when_i_add_a_computer_player(step):
    global computerPlayers
    global playersCount
    computerPlayers += 1
    playersCount += computerPlayers

@step(u'Then there\'s one player')
def then_there_s_one_player(step):
    assert playersCount == 1