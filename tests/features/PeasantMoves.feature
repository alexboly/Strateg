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
		Then I can move the first peasant to the position "position"
		
	Scenario: Cannot move the peasant when not selected
		Given A started game
		When I move the first peasant
		Then the first peasant doesn't move