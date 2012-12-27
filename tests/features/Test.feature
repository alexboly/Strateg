Feature: Start game
	As a gamer
	I want to start a game
	In order to play
	
	Scenario: New game has no player
		Given A new game to configure
		Then there's no player
		
	Scenario: Game with a computer player has one player
		Given A new game to configure
		When I add a computer player
		Then there's one player
		
	Scenario: Game with a human player has one player
		Given A new game to configure
		When I add a human player
		Then there's one player
		
	Scenario: Can start game with one human and one computer player
		Given A new game to configure
		When I add a human player
		And I add a computer player
		Then I can start the game
		
	Scenario: Can start game with two human players
		Given A new game to configure
		When I add a human player
		And I add a human player
		Then I can start the game
		
	Scenario: Can start game with two computer players (demo)
		Given A new game to configure
		When I add a computer player
		And I add a computer player
		Then I can start the game
	
	Scenario: Cannot start game without a player
		Given A new game to configure
		Then I cannot start the game
		
	Scenario: Cannot start game with one human player
		Given A new game to configure
		When I add a human player
		Then I cannot start the game

	Scenario: Cannot start game with one computer player
		Given A new game to configure
		When I add a computer player
		Then I cannot start the game
