# Write a function that is a number guessing game. It should determine a random number from 1-100 CHECK, and let the user guess the number. It should report back whether their guess is correct, too high, or too low CHECK. 
#Important: if the user guesses a number they've already guessed, it should tell them they have previously guessed this number. Until they guess the correct number, it should continue to prompt them. 
#Once they've guessed the correct number, it should congratulate them and tell them how many guesses they took to solve the problem (minus any duplicate guesses). CHECK


import random

def guessing_game(lower_bound, upper_bound):
	print """
	Welcome to the Number Guessing Game.
	Here's how it works: you enter a number between {lower_bound} and {upper_bound}.
	I will tell you if you're guess is too high or too low, until you guess the correct number!

	Good luck!
	Mandy
	""".format(**locals())

	target_number = random.randint(lower_bound, upper_bound)

	guess = 0
	guess_history = []	

	while target_number != guess:
	    print 'Guess a number?'
	    guess = raw_input()
	    guess = int(guess)

	    if guess in guess_history:
	        print "You already tried this number, please guess again."
	    elif guess > upper_bound:
	    	print "Please enter a number between {lower_bound} and {upper_bound}.".format(**locals())
	    elif guess < lower_bound:
	    	print "Please enter a number between {lower_bound} and {upper_bound}.".format(**locals())

	    elif guess < target_number:
	        print 'Your guess is too low. Try again.'
	        guess_history.append(guess)
	    elif guess > target_number:
	        print 'Your guess is too high. Try again.'
	        guess_history.append(guess)
	    elif guess == target_number: 
	        guess_history.append(guess)
	        print "Congratulations! You guessed the correct number."
	        if len(guess_history) == 1:
	        	try_string = "try."
	        else:
	        	try_string = "tries."
	        print "You needed", len(guess_history), try_string
	        print guess_history
	        break

guessing_game(1, 100)
