from Game import Game
from lettuce import step
from lettuce.registry import world
from nose.tools import raises
from GameCannotStartError import GameCannotStartError

@step(u'A new game')
def a_new_game(step):
    world.game = Game()

@step(u'there are zero players in the game')
def the_game_has_zero_players(step):
    assert world.game.playersCount() == 0

@step(u'I add a computer player')
def i_add_a_computer_player(step):
    world.game.addComputerPlayer()

@step(u'there is one player in the game')
def there_s_one_player(step):
    assert world.game.playersCount() == 1
    
@step(u'I add a human player')
def i_add_a_human_player(step):
    world.game.addHumanPlayer()
    
@step(u'I can start the game')
def i_can_start_the_game(step):
    assert world.game.canStartGame()

@step(u'I cannot start the game')
def i_cannot_start_the_game(step):
    assert (not world.game.canStartGame())
    
    throwsException = False
    try:
        world.game.start()
    except GameCannotStartError:
        throwsException = True
    assert throwsException