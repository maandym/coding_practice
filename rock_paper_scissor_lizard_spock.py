import random

class Computer(object):
	def choose(self):
		return random.randrange(1,5)

class Player(object):
	def __init__(self, name):
		self.name = name;
	def choose(self):
		print """Enter:
- 1 FOR ROCK;
- 2 FOR PAPER;
- 3 FOR SCISSOR;
- 4 FOR LIZARD;
- 5 FOR SPOCK."""
		Choice = int(raw_input('>'))
		while(Choice<1 or Choice>5):
			print "Wrong!!! Enter 1 for rock, 2 for paper, 3 for scissor, 4 for lizard, or 5 for spock."
			Choice = int(raw_input('>'))
		return Choice


def main():
	print "Let's play Rock Paper Scissor Lizard Spock"
	print "You choose and I tell you if you win!"
	print "Let's start: what is your name?"
	name = raw_input(">>>") 

	again  = 'y'
	while(again == 'y'):
		tPlayer = Player(name)
		tComputer = Computer()
		printWinner(tPlayer.choose() , tComputer.choose())
		again = raw_input("Do you want to play again? y or n: ")
	
	print "Bye Bye {name}!".format(name=tPlayer.name)	


#actual choice from the number
def getChoice(choiceNumber):
	choices = {1: "ROCK.", 2: "PAPER.", 3: "SCISSOR.", 4: "LIZARD.", 5: "SPOCK."}
	return choices[choiceNumber]

#check and prints the winner

draw = "It's a draw."
winner = "You won :)"
loser = "You lose :("

def checkWinner(P, C):
	if ( P == C ):
		return draw
	elif ( (P-C)%3 == 1 ) or ( (P-C)%5 == 1 ):
		return winner
	elif ( (C-P)%3 == 1 ) or ( (P-C)%5 == 1 ):
		return loser

def printWinner(P,C):
	print "You chose", getChoice(P) 
	print "Computer chose", getChoice(C)
	print checkWinner(P, C)
	# return checkWinner(P, C)

#start the game
main()

