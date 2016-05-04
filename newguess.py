#You will have three rounds to properly guess a number between 0 and 100. Each round gives you 5 chances to find the numbe
import random

def roundnumber(number):
	print "Round" + str(number)
	roundnumber(number+1)

def guess(run, ans):
	if run == 0:
		print """Your not very good at this
"""
	elif run == 5:
		ans = random.randint(0, 100)
	else:
		inp = int(raw_input("Your guess: "))
		if inp > ans:
			print "Too high"
			guess(run-1, ans)
		elif inp < ans:
			print "Too low"
			guess(run-1, ans)
		else:
			print """Correct
"""

def main():
	guess(5,0)
	guess(5,0)
	guess(5,0)

main()
