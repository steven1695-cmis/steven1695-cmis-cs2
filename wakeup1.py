total = 0
count = 0

def counting(n):
	run = 0
	if n <= 0:
		pass
	else:
		number = float(raw_input("n"+str(run)+": "))
		if number >= 10 or number < 0:
			print str(number)+" is out of range."
		else:
			total += number
			count += 1
	run += 1
	counting(n-1)

def evenodd(average):
	if average%2 == 0:
		return "even"
	else:
		return "odd"

def main():
	print """
This program will ask you for 5 integer of float values.
It will calculate the average of all values form 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd."""

	counting(5)

	eoro = evenodd(average)

#Output
	print "The average is " + str(average) + """
The integer part of the average is """ + str(int(average)) + "."+ """
The integer part is """ + eoro + "."


main()
