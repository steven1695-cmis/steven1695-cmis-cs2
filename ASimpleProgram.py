def recvol(l, w, h):
	return l*w*h

def recsurfarea(l, w, h):
	return 2*l*w + 2*l*h + 2*w*h

def output(h, l, w, rpsa, rpv):
	out = """
So the height of the rectangular prism is {},
the length of the rectangular prism is {},
and the width of the rectangular prism is {}.
Correct? Then the surface area of that recta ngular prism is {}
and the volume is {}.
""".format(h, l, w, rpsa, rpv)
	return out

def main():
	height = raw_input("Decide upon the numbers of a rectangular prism. What is its height?:" )
	length = raw_input("What is its length?:")
	width = raw_input("What is its width?:")
	rpsa = recsurfarea(float(length), float(width), float(height))
	rpv = recvol(float(length), float(width), float(height))

	out = output(height, length, width, rpsa, rpv)
	print out

main()
