#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#The symbol is called the assignment operator and is used for connecting a value to a variable. The assignment operator places the value that comes after it into the variable that is before the assignment operator.
#
#
#2 3pts) Write a technical definition for 'function'
#A function is a named sequence of statements that performs a computation. 
#
#
#3 1pt) What does the keyword "return" do?
#"Return" is a keyword that returns the output of the function. When you use "return" in a function definition, the programming you have for the "return" statement is what you will get back when you "call" the function. It basically defines the return value of the function.
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean: True, False
#	2: string: "apple", "wonderland"
#	3: integer: 4, 456
#	4: float: 4.76, 9.0
#	5: tuple: ("cheeseburger", "sandwich", 34)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.
#
#A function call is the act of "calling" the function. Calling the function runs the function and produces its result, aka return value.
#They are different because the function definition defines the function and the function call uses the function.
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input
#	2:processing
#	3:output
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


def circlediameter(area):
	import math	
	radiussqrd = area/math.pi
	radius = math.sqrt(radiussqrd)
	diameter = radius*2
	return diameter

def output(d1, d2, d3, total):
	out = """
Circle	Diameter
c1	{}
c2	{}
c3	{}
TOTALS	{}
""".format(d1, d2, d3, total)
	return out

def main():
	a1 = int(raw_input("Area of C1: "))
	a2 = int(raw_input("Area of C2: "))
	a3 = int(raw_input("Area of C3: "))
	d1 = circlediameter(a1)
	d2 = circlediameter(a2)
	d3 = circlediameter(a3)
	total = d1 + d2 + d3
	out = output(d1, d2, d3, total)
	print out 

main()
