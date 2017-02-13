import random

def roll_die():
	return random.randint(1,6)

def roll_until():
	roll_outcome = 0
	continue_question = "y"
	running_tally = 0
	while continue_question == "y" and roll_outcome != 1:
		roll_outcome= roll_die()
		print "You rolled: ", roll_outcome
		if roll_outcome == 1:
			return 0
		else: 
			running_tally= roll_outcome + running_tally
		print "Your running tally is: ", running_tally
		continue_question= raw_input("Press Y to roll again: ").lower()
	return running_tally


def main():
#how to exit at any time?

	player1_score = 0
	player2_score = 0
 
	print "The Goal: Reach 100 points or more"
	print "The Rules: Each player rolls as many times as they like to add to their score"
	print "The catch: If the player rolls 1, they lose all points from turn."
	starting_player = random.choice(["Oldest player", "Youngest player"])
	print starting_player, "begins!"
	print "Your current score is: ", player1_score
	player1_score= roll_until() + player1_score
	print "Starting player current score is: ", player1_score

	while(True):

		if player1_score >= 100:
			print "YOU WIN STARTING PLAYER!"
			break

		else:

			print "Not starting player begins!"
			print "Not starting current score is: ", player2_score
			player2_score= roll_until() + player2_score
			if player2_score >=100:
				print "YOU WIN NOT STARTING PLAYER!!!" 
				break
			else: 
				print "Starting players turn"
				print "Starting current score is: ", player1_score
				player1_score= roll_until() + player1_score


main()
	