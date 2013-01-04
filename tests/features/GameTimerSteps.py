from lettuce import step
from lettuce.registry import world
from Game import GameTimer

@step(u'game has a timer')
def game_has_a_timer(step):
    assert world.game.Timer != None

@step(u'timer ticks')
def timer_ticks(step):
    world.timer.tick()

def callOnTick():
    world.callOnTickCalled = True

@step(u'new timer with an observer')
def new_timer_with_an_observer(step):
    world.timer = GameTimer()
    world.timer.CallOnTick = callOnTick
    world.callOnTickCalled = False
    
@step(u'Then the observer is notified')
def then_the_observer_is_notified(step):
    assert world.callOnTickCalled
