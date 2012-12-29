Feature: Game started
	As a player
	I want to have a base and a peasant after the game starts
	So that I can start building
	
	Scenario: The first player has a base in the beginning
		Given A started game
		Then the first player has a base
		
	Scenario: The second player has a base in the beginning
		Given A started game
		Then the second player has a base
		
	Scenario: The first player has a peasant in the beginning
		Given A started game
		Then the first player has a peasant
		
	Scenario: The second player has a peasant in the beginning
		Given A started game
		Then the second player has a peasant
	