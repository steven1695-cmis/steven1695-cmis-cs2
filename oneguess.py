import random

# Defintion of Functions
def output(target, guess, difference):
	print """
The target was {}.
Your guess was {}.""".format(target, guess)
	if target > guess:
		print "Thats under by {}.".format(difference)
	elif target < guess:
		print "Thats over by {}.".format(difference)
	elif target == guess:
		print "Correct! You must be a psychic!"
	

def main():
	#Input
	minimum = raw_input("What is the minimum number? ")
	maximum = raw_input("What is the maximum number? ")
	
	#Output
	print """I'm thinking of a number from """ + minimum + """ to """ + maximum + """."""

	#Input 
	guess = int(raw_input("What do you think it is?: "))
	
	#Processing
	answer = random.randint(int(minimum), int(maximum))
	out = output(answer, guess, abs(guess - answer))

	#Output
	return out
	


main()
