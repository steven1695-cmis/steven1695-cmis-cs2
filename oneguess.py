import random

main():
	minimum = float(raw_input("What is the minimum number? "))
	maximum = float(raw_input("What is the maximum number? "))
	
	print """I'm thinking of a number from""" + minimum + """to""" + maximum + """."""

	guess = float(raw_input("What do you think it is?: "))
	answer = random.randint(minimum, maximum)
	output ="""
	The target was {}.
	Your guess was {}.
	That's under by {}."""
	#Output
	


main()
