from lettuce import step
from Game import Game

game = None

@step(u'Given A new game to configure')
def given_a_new_game_to_configure(step):
    global game
    game = Game()

@step(u'Then there\'s no player')
def then_there_s_no_player(step):
    assert game.playersCount() == 0

@step(u'When I add a computer player')
def when_i_add_a_computer_player(step):
    game.addComputerPlayer()

@step(u'Then there\'s one player')
def then_there_s_one_player(step):
    assert game.playersCount() == 1
    
@step(u'When I add a human player')
def when_i_add_a_human_player(step):
    game.addHumanPlayer()
    
@step(u'And I add a computer player')
def and_i_add_a_computer_player(step):
    when_i_add_a_computer_player(step)
    
@step(u'And I add a human player')
def and_i_add_a_human_player(step):
    when_i_add_a_human_player(step)
    
@step(u'Then I can start the game')
def then_i_can_start_the_game(step):
    assert game.canStartGame()
