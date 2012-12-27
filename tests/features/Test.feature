Feature: Start game
	As a gamer
	I want to start a game
	In order to play
	
	Scenario: No player
		Given A new game to configure
		Then there's no player
		
	Scenario: Add computer player
		Given A new game to configure
		When I add a computer player
		Then there's one player
		
	Scenario: Add human player
		Given A new game to configure
		When I add a human player
		Then there's one player