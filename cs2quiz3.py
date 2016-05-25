#Section 1: Terminology
# 1) What is a recursive function?
#A function that calls itself.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#It becomes an infinite recursion function with no way to end although the computer has set limitations so that a function does not run forever even if it doesn't have a base case.
#
#
# 3) What is the first thing to consider when designing a recursive function?
#How the function will end, a base case.
#
#
# 4) How do we put data into a function call?
#With the parameters of a function. You plug in your values in for it to use.
#
# 
# 5) How do we get data out of a function call?
#Return.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2 
#b3 = 4

#c1 = -2
#c2 = 4
#c3 = 45

#d1 = 6
#d2 = 8
#d3 = 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.
def question(count, total):
	num = raw_input("Next: ")
	if num == '':
		ans = float(total)/float(count)
		print "The average of your odd numbers was " + str(ans) + "."
	elif float(num)%2 == 0:
		return question(count, total)
	elif float(num)%2 == 1:
		return question(count+1, total+int(num))
	else:
		exit()

def main():
	question(0, 0)

#main()

def function1(x, n):
	if n <= 0:
		return x
	else:
		return 1 + function1(x, n-1)

def function2(a, b):
	if a <= 0:
		return 1 + function2(a+1, b**a)
	else:
		return b

def function3(a, b):
	if b <= 0:
		return a
	else:
		return a + b + function3(a, b - 1)

def function4(a, b, c):
	if a > b and a > c:
		return 1 + function4(b + 1, c, a)
	elif b > a or b > c:
		return 1 - function4(b - 1, c, a)
	else:
		return a + b + c

print function1(2, 6)
print function1(6, 2)
print function1(-1, -1)

print function2(2, 2)
print function2(0, 0)
print function2(-2, -2)

print function3(-2, 3)
print function3(4, -2)
print function3(5, 5)

print function4(1,2,3)
print function4(3,2,1)
print function4(1,3,2)




