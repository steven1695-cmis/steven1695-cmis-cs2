def euler1():
	counter = 0
	num = 0
	while counter < 1000:
		if counter %3 == 0 or counter %5 == 0:
			num += counter
		counter += 1
	return num

def euler2():
	term1 = 1
	term2 = 2
	num = 0
	while term1 + term2 < 4000000:
		if term1 %2 == 0:
			num += term1
		if term2 %2 == 0:
			num += term2
		
def main():
	print euler1()

main()
