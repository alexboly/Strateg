Feature: Peasant builds barracks
	As a player
	I want to build a barrack
	So that I can build soldiers

Scenario: Peasant doesn't build barracks without an order
	Given A started game
	Then the first peasant is not building

Scenario: Peasant builds barracks
	Given A started game
	When I order the first peasant to build barracks
	Then the first peasant starts building the barracks
	
Scenario: Peasant finishes building
	Given A started game
	When I order the first peasant to build barracks
	And I wait for 2 ticks
	Then the first peasant is not building
	
Scenario: Barracks is built
	Given a started game
	When I order the first peasant to build barracks
	And I wait for 2 ticks
	Then the player has a barracks
	
Scenario: Player doesn't start with barracks
	Given a started game
	Then the player doesn't have a barracks
	
Scenario: Barracks is at the right position
	Given a started game
	When the barracks is built at position "BarracksPosition"
	Then the barracks is found at position "BarracksPosition"