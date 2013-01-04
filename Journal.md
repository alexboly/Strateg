# Journal

## 4 January 2013

The first scenario I wanted to implement was the simplest strategy game I could imagine:

* two players, one is human and the other one does nothing
* they both start with a base and a "peasant" - forage and build unit
* the human player builds a war building, then creates a "soldier"
* the soldier destroys the other player's base
* human player wins

I started with the typical warcraft / starcraft stuff, simply because I am familiar with it.

When I got to the feature "Peasant forages resource", I started wondering:

* What type of resource do I want? 
* Is it really necessary to have resources at this point?
* Is this how I want to forage resources? I prefer less micro-management and more strategy, so maybe foraging should be automatic? Or more like Pharaoh?

There's also an overarching concern: What decisions do I want to make now, and what decisions do I want to postpone?

I have a few options:

#. Avoid foraging
    
    I could avoid foraging. Start with a peasant and a soldier, send the soldier to destroy the base. 
    Then focus on a simple visual representation of the game, just enough to see what else I need to show.
    
    This means I temporarily ignore the foraging code I wrote, remove it or stash it.
    
#. Choose one way to forage

    I could decide now what type of foraging I want. That seems to add less value than first option. Having a visual representation adds more value.
    
#. Avoid foraging but build

	I could avoid foraging but change the script so that I can build the war building. Either the war building costs nothing, or the player starts with
	enough resources to build it immediately. I prefer the second option since it requires less change later.
	
	I will also have to temporarily ignore, remove or stash the foraging code.
	
I think I can safely ignore second option. Third option seems better, but it requires more work on the visual code. Still, I don't think it's that much.

I will probably go with option 3, unless I change my mind.