from Game import Game
from lettuce.decorators import step
from lettuce.registry import world

@step(u'A started game')
def given_a_started_game(step):
    world.game = Game.withHumanAndComputerPlayer()
    world.firstPlayer = world.game.getFirstPlayer()
    world.firstPeasantOfFirstPlayer = world.firstPlayer.getPeasant()