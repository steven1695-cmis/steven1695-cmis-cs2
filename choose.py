#My script will be a story of a child and her choices which will affect the outcome of her story

def brothertrouble():
	choice = raw_input("""Oh no! Your brother fell into the river when he tripped on the rocks. 
He is struggling against the currents but is losing and about to drown. 
Do you save him? 
Yes or No: """) == "Yes"
	if choice:
		print "You saved your brother from certain death but in turn, you have fell into the river and got carried away."
	else:
		print "Your brother drowned."

brothertrouble()
	
