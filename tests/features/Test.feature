Feature: Start game
	As a gamer
	I want to start a game
	In order to play
	
	Scenario: No player
		When I configure the game
		Then there's no player
		
	Scenario: Add computer player
		When I add a computer player
		Then there's one player