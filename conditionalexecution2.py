def countup(n):
	if n >= 11:
		pass
	else:
		print n
		countup(n+1)

def countupfrom(start, stop):
	if start >= stop+1:
		pass
	else:
		print start
		countupfrom(start+1, stop)

def main():
	randnum = int(raw_input("Write a random number and it will count up to 10: "))
	countup(randnum)
	
	start = int(raw_input("Write a starting number: ")
	stop = int(raw_input("Write a stopping number to count up to: ")
	countupfrom(start, stop)
	
	
main()


