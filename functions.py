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
	j = 80 -len(a)
	return j*" " + a

print right_align("Hello")
print right_align("I'm depressed")
def center(a):
	j = 80 - len(a)
	k = j/2
	return " "*k + str(a) + " "*k

print center("Hello")
print center("Cheese")
def msg_box(a):
	lineone = "+" + "--" + len(a)*"-" + "--" + "+"
	linetwo = "|  " + str(a) + "  |"
	linethree = "+" + "--" + len(a)*"-" + "--" + "+"
	return lineone + "\n" + linetwo + "\n" + linethree

print msg_box("Hello")
print msg_box("Happy, so happy")

#Variables for function output
add1 = add(3, 4)
add2 = add(32, 23)
sub1 = sub(23, 3)
sub2 = sub(5, 43)
mul1 = mul(4, 2)
mul2 = mul(54, 2)
div1 = div(10,2)
div2 = div(9, 8.0)
hours_from_seconds1 = hours_from_seconds(86400)
hours_from_seconds2 = hours_from_seconds(7200)
circle_area1 = circle_area(5)
circle_area2 = circle_area(2.5)
sphere_volume1 = sphere_volume(5)
sphere_volume2 = sphere_volume(7) 
avg_volume1 = avg_volume(10, 20)
avg_volume2 = avg_volume(3, 5)
area1 = area(1, 2, 2.5)
area2 = area(5, 12, 13)
right_align1 = right_align("Hello")
right_align2 = right_align("I'm depressed")
center1 = center("Hello")
center2 = center("Cheese")
msg_box1 = msg_box("Hello")
msg_box2 = msg_box("Happy, so happy")

print msg_box(str(add1))
print msg_box(str(add2))
print msg_box(str(sub1))
print msg_box(str(sub2))
print msg_box(str(mul1))
print msg_box(str(mul2))
print msg_box(str(div1))
print msg_box(str(div2))
print msg_box(str(hours_from_seconds1))
print msg_box(str(hours_from_seconds2))
print msg_box(str(circle_area1))
print msg_box(str(circle_area2))
print msg_box(str(sphere_volume1))
print msg_box(str(sphere_volume2))
print msg_box(str(avg_volume1))
print msg_box(str(avg_volume2))
print msg_box(str(area1))
print msg_box(str(area2))
print msg_box(str(right_align1)) #doesn't work.
print msg_box(str(right_align2))
print msg_box(str(center1)) #doesn't work.
print msg_box(str(center2))
print msg_box(len(msg_box1) - (len(msg_box1) + 6)) #doesn't work.
print msg_box(str(msg_box2))
