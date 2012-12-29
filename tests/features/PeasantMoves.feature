Feature: Peasant Moves
	As a player
	I want to move my peasant
	So that I can interact with the map
	
	Scenario: Can select the peasant
		Given A started game
		When I select the first peasant
		Then the first peasant is selected
		
	Scenario: Can move the peasant
		Given A started game
		When I select the first peasant
		Then I can move the first peasant to the location I provide