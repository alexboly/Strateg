from Game import *
from lettuce import step

game = None

@step(u'Given Another started game')
def given_another_started_game(step):
    global game
    game = Game()
    game.addHumanPlayer()
    game.addComputerPlayer()
    game.start()

@step(u'Then I can select the first peasant')
def then_i_can_select_the_first_peasant(step):
    global game
    firstPlayer = game.getFirstPlayer()
    peasant = firstPlayer.getPeasant()
    
    peasant.select()
    
    assert peasant.isSelected()