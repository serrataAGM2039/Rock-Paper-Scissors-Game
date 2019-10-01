# Gabriel Serrata
# Rock Paper Scissors Game
#_______________________________________________________________________
# break into pieces
# welcome page, with name entry 
# score screen with computer, player(name), and ties
# Options for game r, p, s, q
# Game will loop untill q is entered 
# Each loop it will get a random chooice from the computer 
# a choice from the player, compare the two, and update the score 
# when the game is over (when q is entered )the ginal score is displayed 

# WELCOME PAGE
# Prompt for the player name 
# a welcome name

# ______________________________________________________________________

# Imports
import random
# Variables 
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name:")
# main loop
while True:
	print("Score:")
	print("Computer:" + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit: ")
	compterChoice = random.choice(cChoices)
	
	if choice == "q":
		break

	if choice == "r":
		print(name + " Picked Rock")
		if compterChoice == "r": # Tie
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1

			
		elif compterChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	elif choice == "p":
		print(name + " Picked Paper")
		if compterChoice == "p": # Tie
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1

			
		elif compterChoice == "s":
			print("Computer picked Scissors")
			print("Paper beats Rock")
			computerScore += 1
		else: # r is only choice left
			print("Computer picked Rock")
			print("Scissors beats Rock")
			playerScore += 1
	elif choice == "s":
		print(name + " Picked Scissors")
		if compterChoice == "s": # Tie
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1

			
		elif compterChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore += 1
		else: # p is only choice left
			print("Computer picked Paper")
			print("Scissors beat Paper")
			playerScore += 1
	else: # type something
		print("This is not an option ")

