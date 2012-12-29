from Player import Player

class Game:
    def __init__(self):
        self.humanPlayers = 0
        self.computerPlayers = 0
    
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
        self.computerPlayers += 1

    def addHumanPlayer(self):
        self.humanPlayers += 1
        
    def playersCount(self):
        return (self.humanPlayers + self.computerPlayers)
    
    def start(self):
        pass

    def getFirstPlayer(self):
        return Player()
    
    def getSecondPlayer(self):
        return Player()