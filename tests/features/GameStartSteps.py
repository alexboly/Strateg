from lettuce import step
from Game import *

game = None

@step(u'Given A started game')
def given_a_started_game(step):
    global game
    game = Game()
    game.addHumanPlayer()
    game.addComputerPlayer()
    game.start()

@step(u'Then the first player has a base')
def then_the_first_player_has_a_base(step):
    global game
    firstPlayer = game.getFirstPlayer()
    
    assert firstPlayer.hasBase()

@step(u'Then the second player has a base')
def then_the_second_player_has_a_base(step):
    global game
    secondPlayer = game.getSecondPlayer()
    
    assert secondPlayer.hasBase()

@step(u'Then the first player has a peasant')
def then_the_first_player_has_a_peasant(step):
    global game
    firstPlayer = game.getFirstPlayer()
    
    assert firstPlayer.getPeasantCount() == 1
    
@step(u'Then the second player has a peasant')
def then_the_second_player_has_a_peasant(step):
    global game
    secondPlayer = game.getSecondPlayer()
    
    assert secondPlayer.getPeasantCount() == 1
