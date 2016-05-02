
def counting(number, run, divis):
	inp = float(raw_input("Number: "))
	if inp >= 10 or number < 0:
		print str(inp)+" is out of range."
		counting(number, run-1, divis)
	elif run == 1:
		number += inp
		result = (number, divis+1)
		return result
	else:
		number += inp
		counting(number, run-1, divis+1)

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

	number, division = counting(0, 5, 0)
	average = number/division	
	eoro = evenodd(average)

#Output
	print "The average is " + str(average) + """
The integer part of the average is """ + str(int(average)) + "."+ """
The integer part is """ + eoro + "."


main()
