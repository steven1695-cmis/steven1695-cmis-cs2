def add(a, b):
	return a+b

print add(3, 4)
print add(32, 23)
def sub(a, b):
	return a-b

print sub(23, 3)
print sub(5, 43)
def mul(a, b):
	return a*b

print mul(4, 2)
print mul(54, 2)
def div(a, b):
	return a/b

print div(10,2)
print div(9,8.0)
def hours_from_seconds(a):
	return a/3600.0

print hours_from_seconds(86400), "hours"
print hours_from_seconds(7200), "hours"
import math

def circle_area(a):
	return math.pi*(a**2)

print circle_area(5)
print circle_area(2.5)
def sphere_volume(a):
	return math.pi*(a**3)*4/3

print sphere_volume(5)
print sphere_volume(7)
def avg_volume(a,b): 
	j = a/2
	k = b/2
	s = math.pi*(j**3)*4/3 + math.pi*(k**3)*4/3
	d = s/2.0
	return d

print avg_volume(10, 20)
print avg_volume(3, 5)
def area(a, b, c):
	s = (a+b+c)/2.0
	j = (s-a)
	k = (s-b)
	l = (s-c)
	t = s*j*k*l
	d = math.sqrt(t)
	return d

print area(1, 2, 2.5)
print area(5, 12, 13)
def right_align(a):
	return a.rjust(80)

print right_align("Hello")
print right_align("I'm depressed")
def center(a):
	return a.center(80)

print center("Hello")
print center("Cheese")
