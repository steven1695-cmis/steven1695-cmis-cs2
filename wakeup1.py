def evenodd(average):
    if average%2 == 0:
            return "even"
    else:
            return "odd"

def inourout(number):
	 if number >= 10 or number < 0:
	    return False
    else:
	    return True

def inourout2(boolean):
	if boolean:
		print str(number) + " is out of range."
    else:
	    total += number
	    division += 1

def main():
    total = 0
    division = 0

#Input
    n0 = float(raw_input("""
This program will ask you for 5 integer of float values.
It will calculate the average of all values form 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd.

n0: """))
    if n0 >= 10 or n0 < 0:
	    print str(n0) + " is out of range."
    else:
	    total += n0
	    division += 1

    n1 = float(raw_input("n1: "))
    if n1 >= 10 or n1 < 0:
	    print str(n1) + " is out of range."
    else:
	total += n1
	division += 1

    n2 = float(raw_input("n2: "))
    if n2 >= 10 or n2 < 0:
	    print str(n2) + " is out of range."
    else:
	    total += n2
	    division += 1

    n3 = float(raw_input("n3: "))
    if n3 >= 10 or n3 < 0:
	    print str(n3) + " is out of range."
    else:
	    total += n3
	    division += 1
    n4 = float(raw_input("n4: "))
    if n4 >= 10 or n4 < 0:
	    print str(n4) + " is out of range."
    else:
	    total += n4
	    division += 1

#Processing
    average = total/division
    eoro = evenodd(average)

#Output
    print "The average is " + str(average) + """
The integer part of the average is """ + str(int(average)) + "."+ """
The integer part is """ + eoro + "."


main()
