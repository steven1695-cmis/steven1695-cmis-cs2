#You will have three rounds to properly guess a number between 0 and 100. Each round gives you 5 chances to find the number
import random

def roundnumberme(times, correct):
	if times > 3:
		return correct
	else:
		print "Round" + str(times)
		correct += guess(6, 0, 0)
		return roundnumberme(times+1, correct)
		

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

def guesspc(down, up, pc, runs, correct):
	if runs == 0:
		print "LOL wrong!"
		return correct
	elif runs == -1:
		return correct
	else:
		print str(pc)
		mynum = raw_input("correct(c) higher(h) lower(l): ")
		if mynum == 'l':
			guess = (down+pc)/2
			return guesspc(down, pc, guess, runs-1, correct)  
		elif mynum == 'h':
			guess = (up+pc)/2
			return guesspc(pc, up, guess, runs-1, correct)
		else:
			print "Correct!"
			return guesspc(0, 100, 50, -1, correct+1)
			

def roundnumberpc(times, correct):
	if times > 3:
		return correct
	else:
		print "Round" + str(times)
		correct += guesspc(0, 100, 50, 6, 0)
		return roundnumberpc(times+1, correct)

def main():
	correctme = roundnumberme(1, 0)
	print "You were correct " + str(correctme) + " times."
	correctpc = roundnumberpc(1, 0)
	print "PC was correct " + str(correctpc) + " times."
	print "The score is " + str(correctme) + " to " + str(correctpc)
main()
