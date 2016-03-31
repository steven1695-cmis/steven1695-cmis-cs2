#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a)3 != 5
#b)"Water" == "Water"
#c)36 >= 4
#
#2) What does 'return' do?
#
#Return is the resultant value you recieve from a function after you finish running it.
#
#
#3) What are 2 ways indentation is important in python code?
#a)Indentation specifies that the indented coding is inside another peace of coding that is above it. Say that I have a False boolean expression and some coding below it. It the coding below the boolean expression is not indented, it will still run the coding because it will not be considered a part of the coding that will trigger when the boolean expression is determined to be false or true. It will just be another line of code unassociated with the boolean expression. The indent associates the coding with the boolean expression above it.
#b)Indentation is also necessary when you are defining a function. Every line of code that is a part of the function you are defining needs to be indented for it to be a part of the function. If it is not indented, it will not be a part of the function.
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) -36
#problem1_b) -(square root of 3)
#problem1_c) 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 0.5
#problem3_d) 0.5
#
#problem4_a) 24
#problem4_b) 6
#problem4_c) 1.5
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)
def processing(A, B, C):
	if A != B and B != C and C != A:
		if A > B and A > C:
			output(True, A)
		elif B > A and B > C:
			output(True, B)
		elif C > A and C > B:
			output(True, C)
	else:
		output(False, A)

def output(directions, largestnumber):
	if directions:
		print "The largest number was {}".format(largestnumber)

	else:
		print "You didn't follow directions"
		

def main():
	#Input
	A = float(raw_input("""Type in 3 different numbers (decimals are OK!)
A: """))
	B = float(raw_input("B: "))
	C = float(raw_input("C: "))

	#Processing + Output
	processing(A, B, C) 
	

main()
