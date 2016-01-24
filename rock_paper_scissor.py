import random

class Computer(object):
	def choose(self):
		return random.randrange(1,3)

class Player(object):
	def __init__(self, name):
		self.name = name;
	def choose(self):
		print """Enter:
- 1 FOR ROCK;
- 2 FOR PAPER;
- 3 FOR SCISSOR."""
		Choice = int(raw_input('>'))
		while(Choice<1 or Choice>3):
			print "Wrong!!! Enter 1 for rock, 2 for paper, or 3 for scissor."
			Choice = int(raw_input('>'))
		return Choice


def main():
	print "Let's play Rock Paper Scissor"
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
	choices = {1: "ROCK.", 2: "PAPER.", 3: "SCISSOR."}
	return choices[choiceNumber]

	# if ( choiceNumber == 1 ):
	# 	return "ROCK."
	# elif ( choiceNumber == 2 ):
	# 	return "PAPER."
	# elif ( choiceNumber == 3 ):
	# 	return "SCISSOR."


#check and prints the winner

draw = "It's a draw."
winner = "You won :)"
loser = "You lose :("

def checkWinner(P, C):
	if ( P == C ):
		return draw
	elif ( (P-C)%3 == 1 ):
		return winner
	elif ( (C-P)%3 == 1 ):
		return loser

def printWinner(P,C):
	print "You chose", getChoice(P) 
	print "Computer chose", getChoice(C)
	print checkWinner(P, C)
	# return checkWinner(P, C)

#start the game
main()


# -------------------------------------------------------------

# def printWinner(P,C):
# 	if ( P == C ): #Rock, Paper, or Scissor for both
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "It is a draw."
# 	elif ( P == 1 and C == 2 ): #Player is Rock and Computer is Paper 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You lose :("
# 	elif ( P == 1 and C == 3 ): #Player is Rock and Computer is Scissor 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You won :)"
# 	elif ( P == 2 and C == 1 ): #Player is Paper and Computer is Rock 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You won :)"
# 	elif ( P == 2 and C == 3 ): #Player is Paper and Computer is Scissor 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You lose :("
# 	elif ( P == 3 and C == 1 ): #Player is Scissor and Computer is Rock 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You lose :("
# 	elif ( P == 3 and C == 2 ): #Player is Scissor and Computer is Paper 
# 		print "You chose", getChoice(P) 
# 		print "Computer chose", getChoice(C)
# 		print "You won :)"
