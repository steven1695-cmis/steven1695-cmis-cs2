#Recursion
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

def countdownfrom(start, stop):
	if start <= stop-1:
		pass
	else:
		print start
		countdownfrom(start-1, stop)

def adder(number):
	total = 0
	total += number
	count = (raw_input("Running total: " + str(total) + """:
Next number: """))
	if count == '':
		print "The sum is " + str(total)
	else:
		total += float(count)
		adder(total)

def biggest(lastnumber):
	number = raw_input("Next: ")
	if number == '':
		print str(lastnumber)
	elif float(number) > lastnumber:
		biggest(float(number))
	else:
		biggest(lastnumber)

def smallest(lastnumber):
	number = raw_input("Next: ")
	if number == '':
		print str(lastnumber)
	elif float(number) < lastnumber:
		smallest(float(number))
	else:
		smallest(lastnumber)

def pow(x, n):
	

def main():
#	randnum = int(raw_input("Write a random number and it will count up to 10: "))
#	countup(randnum)
#	countupfrom(1,10)
#	countdownfrom(10,1)
#	adder(0)
#	biggest(-float("inf"))
#	smallest(float('inf'))
	pow(3, 3)

main()

