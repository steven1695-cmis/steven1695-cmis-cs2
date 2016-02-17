yourlife = raw_input("How good is your life? Tell us. >>> ")
yourlifesentence = "Your life is " + yourlife + "."
print yourlifesentence


def output(waterbottle, waterbottleage, waterbottleweight, waterbottlejob):
	output = """
Hello {}.
You are {} years old and weigh {} kilograms! Ha! 
Didn't think I knew that did you? 
I have obtained the all knowing eye!
I even know you are a {}!
""".format(waterbottle, waterbottleage, waterbottleweight, waterbottlejob)

def main():
	waterbottle = raw_input("Name your character:")
	waterbottleage = raw_input("Age:")
	waterbottleweight = raw_input("Weight in kilograms:")
	waterbottlejob = raw_input("Occupation:")



print output 
