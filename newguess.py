#You will have three rounds to properly guess a number between 0 and 100. Each round gives you 5 chances to find the numbe
import random

def roundnumber(times):
	if times > 3:
		pass
	else:
		print "Round" + str(times)
		guess(8, 0, 0)
		return roundnumber(times+1)
		

def guess(run, ans, correct):
	if run == 0:
		print """Your not very good at this
"""
	elif run == 8:
		ans = random.randint(0, 100)
		guess(run-1, ans, correct)
	else:
		inp = int(raw_input("Your guess: "))
		if inp > ans:
			print "Too high"
			guess(run-1, ans, correct)
		elif inp < ans:
			print "Too low"
			guess(run-1, ans, correct)
		else:
			print """Correct
"""
			guess(run-1, ans, correct+1)

def main():
	roundnumber(1)
	print "You were correct " + str(correct) + " times."

main()