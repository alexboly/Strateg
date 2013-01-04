Feature: Peasant builds barracks

Scenario: Peasant doesn't build barracks without an order
	Given A started game
	Then the first peasant is not building

Scenario: Peasant builds barracks
	Given A started game
	When I order the first peasant to build barracks
	Then the first peasant starts building the barracks
	
