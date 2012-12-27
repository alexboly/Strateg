from lettuce import step
from curses.ascii import CAN

playersCount = 0
computerPlayers = 0
humanPlayers = 0
canStartGame = False


@step(u'Given A new game to configure')
def given_a_new_game_to_configure(step):
    global playersCount
    global humanPlayers
    global computerPlayers
    computerPlayers = 0
    humanPlayers = 0
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
    
@step(u'And I add a computer player')
def and_i_add_a_computer_player(step):
    when_i_add_a_computer_player(step)
    
@step(u'Then I can start the game')
def then_i_can_start_the_game(step):
    global canStartGame
    canStartGame = (humanPlayers == 1) and (computerPlayers == 1) and (playersCount >= 2)
    assert canStartGame
