def parseFirstMove(firstMove):
	if regexDrinkHemlock(firstMove):
		print("You chose to believe the GUARD, DRINK HEMLOCK, and died. Your score was 100.")
	else:
		print("You appear to have done something other than choosing to DRINK HEMLOCK. This appears to have worked! Your score is i. Type HELP for options.")

def main():
	print("Some members of the GUARD are here and waiting for you to DRINK HEMLOCK.")
	firstMove = newChoice()
	parseFirstMove(firstMove)
