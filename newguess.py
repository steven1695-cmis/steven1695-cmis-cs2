#You will have three rounds to properly guess a number between 0 and 100. Each round gives you 5 chances to find the number
import random

def roundnumber(times, correct):
	if times > 3:
		return correct
	else:
		print "Round" + str(times)
		correct += guess(6, 0, 0)
		return roundnumber(times+1, correct)
		

def guess(run, ans, correct):
	if run == 0:
		print """Your not very good at this
"""
		return correct 
	elif run == -1:
		return correct
	elif run == 6:
		ans = random.randint(0, 100)
		return guess(run-1, ans, correct)
	else:
		inp = int(raw_input("Your guess: "))
		if inp > ans:
			print "Too high"
			return guess(run-1, ans, correct)
		elif inp < ans:
			print "Too low"
			return guess(run-1, ans, correct)
		else:
			print """Correct
"""
			return guess(-1, ans, correct+1)

#def guesspc():
#	pcguess = 100
#	print str(pcguess/2)
#	mynum = raw_input("correct(c) high(h) low(l): ")
#	if mynum == l:
#
	

def main():
	correct = roundnumber(1, 0)
	print "You were correct " + str(correct) + " times."

main()
