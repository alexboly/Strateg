from Game import Game
from lettuce.decorators import step
from lettuce.registry import world

@step(u'Given A started game')
def given_a_started_game(step):
    world.game = Game.withHumanAndComputerPlayer()
