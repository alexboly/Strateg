Feature: Game timer
	As a game designer
	I want the game to have a timer
	So that I game progresses in time
	

	Scenario: Game starts with a timer
		Given a started game
		Then the game has a timer
		
	Scenario: Timer notifies on tick
		Given a new timer with an observer
		When the timer ticks
		Then the observer is notified