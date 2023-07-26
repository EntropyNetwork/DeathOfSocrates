import regex

##TODO: package these globals, foolhardy python developer
locations = ["YOUR HOME"]
items = ["SCORE"]
actions = ["SPEAK", "LOOK", "GO TO", "CHECK", "ACTIONS", "HELP", "SCORE"]
score_i = "a useless imaginary number"

def parseFirstMove(firstMove):
	if regexDrinkHemlock(firstMove):
		print("You chose to believe the GUARD, DRINK HEMLOCK, and died. Your score was 100.")
	else:
		print("You chose to do something other than DRINK HEMLOCK.")
		print("The GUARD appears upset and shakes his head. 'Fine, then, Philosopher. Persist in this doomed Athens without the favor of the gods.'")
		print("It appears to have worked! Your SCORE is i. Type ACTIONS to pull up the ACTIONS menu.")
		print("You are in YOUR HOME. The KID WHO IS AFRAID OF ANIMALS is screaming outside.")

def main():
	print("Some members of the GUARD are here and waiting for you to DRINK HEMLOCK.")
	firstMove = newChoice()
	parseFirstMove(firstMove)
