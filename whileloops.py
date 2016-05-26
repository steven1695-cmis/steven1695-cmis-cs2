def countdown(number):
	while number >= 0:
		print number
		number -= 1

def counter(num):
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

counter(5)
counter(-3)
