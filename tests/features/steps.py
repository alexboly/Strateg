from lettuce import step

playersCount = 0
computerPlayers = 0
humanPlayers = 0


@step(u'Given A new game to configure')
def given_a_new_game_to_configure(step):
    global playersCount
    playersCount = 0

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
    
@step(u'When I add a human player')
def when_i_add_a_human_player(step):
    global humanPlayers
    global playersCount
    humanPlayers += 1
    playersCount += humanPlayers