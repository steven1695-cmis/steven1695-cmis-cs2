def countdown(number):
	while number >= 0:
		print number
		number -= 1

def count(num):
	if num > 0:
		while num >= 0:
			print num
			num -= 1
	elif num < 0:
		while num < 1:
			print num
			num += 1
	else:
		print num

#count(5)
#count(-3)

def countfrom(num1, num2):
	if num1 > num2:
		while num1 >= num2:
			print num1
			num1 -= 1
	elif num1 < num2:
		while num1 <= num2:
			print num1
			num1 += 1
	else:
		print "Uhhh.. Its done already."

#countfrom(-1, 1)
#countfrom(1, -1)

def sumofodds(num):
	total = 0
	if num > 0:
		while num > 0:
			if num % 2 == 1:
				total += num
				num = num-1
			else:
				num = num-1
		while num == 0:
			return total
	elif num < 0:
		while num < 0:
			if num % 2 == 1:
				total += num
				num = num+1
			else:
				num = num+1
		while num == 0:
			return total
	else:
		return num

#print sumofodds(5)
#print sumofodds(-9)

def grid(w, h):
	out = ""
	count = 0
	while h > 0:
		while w > 0:
			out +="."
			w -= 1
		out += "\n"
		h -= 1
	return out
	

print grid(10, 10)

