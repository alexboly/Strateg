from Player import Player
from GameCannotStartError import GameCannotStartError

class Game:
    def __init__(self):
        self.players = []
    
    @staticmethod
    def withHumanAndComputerPlayer():
        game = Game()
        game.addHumanPlayer()
        game.addComputerPlayer()
        game.start()
        return game
        
    def canStartGame(self):
        return self.playersCount() >= 2
    
    def addComputerPlayer(self):
        self.players.append(Player())

    def addHumanPlayer(self):
        self.players.append(Player())
        
    def playersCount(self):
        return len(self.players)
    
    def start(self):
        if not self.canStartGame():
            raise GameCannotStartError()

    def getFirstPlayer(self):
        return self.players[0]
    
    def getSecondPlayer(self):
        return self.players[1]