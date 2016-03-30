#You are a criminal, and you seek to steal the Artifact of Dumbo, priced at 3 pebbles.

#You reach the museum building in the night and decide on how to enter.
#Computer asks you how to enter: front door, back door

#If you pick the front door, you are spotted by the security on the way in.
#There are two guards, computer gives you choice: fight guards, run into the next room.
#If you choose to fight, you pick which pocket to pull out a weapon from to contest the batons of the guards. Left: paperclip, apple, gun/Right: dagger, cheesestick
#If you run, you are caught by the guards and arrested: Game Over

#If you pick backdoor, you enter without trouble.
#However, now there are red sensor beams you need to go through to the left or a bunny to the right.
#If you decide to go through the sensor beams, you have a 50% chance to succeed. If you fail: Game Over/ If you succeed: Continue
#If you pick the bunny, you are given the choice of feeding the bunny or touching the bunny. You can feed the bunny water or carrots and pass either way. If you touch the bunny, you lose.

#If you have passed the following obstacles, you are now in front of the Artifact of Dumbo but there are two. One is a fake.
#You need to solve 3 questions to get the true artifact.
#If you get all of the questions right, you leave with the real artifact, if you get even one of them wrong, you leave the museum with the fake artifact.

#There is a secret game mode that can only be accessed by typing "new game mode" over the options of how to enter. But its actually just a coin toss and memorization game.

import random

def finaldestination(Pass):
	if Pass:
		print """
You have passed all the obstacles up to this point and you have reached the artifact of Dumbo. However, there are TWO! One is definitely a fake. In order for you to get the true artifact, you must solve three problems correctly. """
		cakeriddle = int(raw_input("""
What is the maximum amount of slices you can have with three cuts on a cake? """))
		foreignriddle = int(raw_input("""
In a certain country, 1/2 of 5 = 3. If the same proportion holds, what is the value of 1/3 of 10? """))
		phoneriddle = int(raw_input("""
What number do you get when you multiply all of the numbers on a telephone's number pad? """))
		numberwrong = 0
		if not cakeriddle == 8:
			numberwrong += 1
		if foreignriddle != 4:
			numberwrong += 1
		if not phoneriddle == 0:
			numberwrong += 1
		if cakeriddle == 8 and foreignriddle == 4 and phoneriddle == 0:
			print """
All Correct! You have solved all the riddles correctly. And you run into the night with the Artifact of Dumbo in your grasp."""
		elif numberwrong > 1:
			say = """
You were wrong {} times. You end up taking the decoy Artifact of Dumbo.""".format(str(numberwrong)) 
			print say
		elif numberwrong == 1:
			print """
You were wrong 1 time. You end up taking the decoy Artifact of Dumbo."""
	else:
		return "My Apologies."
def enter():
	EnterChoice = raw_input("""
You make a choice of how to enter. (front door/ back door): """)

	if EnterChoice == "front door":
		print """
You enter through the front door. You run into two guards on night duty. Their batons look intimidating. Their power level is 5. """
		guardchoice = raw_input("""
Will you engage the guards or run away? (fight guards/ run away): """)
		if guardchoice == "fight guards":
			weaponchoice = yourweapon()
			winfail = guardfight(weaponchoice)
			finaldestination(winfail)
		elif guardchoice == "run away":
			print """
You attempted to flee but you were cornered by the guards and arrested: Game Over"""
		else:
			print "That is not a viable choice. Try again."
	elif EnterChoice == "back door":
		print "You enter through the back door. There are no guards. However, you are met by red sensor beams on the left and a karate rabbit on the right."
		choice = raw_input("Which side do you want to go to? (left/ right): ")
		if choice == "left":
			winfail = sensorbeams()
			finaldestination(winfail)
		elif choice == "right":
			winfail = karatebunny()
			finaldestination(winfail)
		else:
			print "Sorry, not an option. Try again."
	elif EnterChoice == "new game mode":
		newgamemode()
	else:
		print "You were unable to enter through the method of choice. Try again."

def newgamemode():
	pickgame = raw_input("Take a pick. (coin toss/memorization): ")
	if pickgame == "coin toss":
		cointoss()
	elif pickgame == "memorization":
		memorization()
	else:
		exit()

def cointoss():
	coin = random.randint(0,1)
	if coin == 0:
		print """
heads"""
	else:
		print """
tails"""
	choice = raw_input("""
Do you want to keep flipping? (yes/no): """)
	if choice == "yes":
		newgamemode()
	else:
		return "You'll never see this text because its a return and I don't want to print it out for you to see."

def memorization():
	print "We are going to play a little memorization game with some math ;D."
	mem1 = raw_input("Write a number: ")
	mem2 = raw_input("Write another: ")
	mem3 = raw_input("Write another: ")
	ans1 = raw_input("What is the value of your first number plus your third number?: ")
	ans2 = raw_input("What is your second number minus your first number?: ")
	ans3 = raw_input("What are all your numbers? List them in order.(i.e. 2 54 6): ")
	if ans1 == str(float(mem1) + float(mem3)):
		 print "Correct!"
	else:
		print "Wrong..."
	if ans2 == str(float(mem2) - float(mem1)):
		print "Correct!"
	else:
		print "Wrong..."
	if ans3 == mem1 + " " + " " + mem2 + " " + mem3:
		print "Correct!"
	else:
		print "Wrong..." 


def karatebunny():
	choice = raw_input("""
Karate Bunny eyes you expectantly and you are hopelessly captivated by its adorable gaze. There are carrots and a bowl of water on a pedestal next to the bunny. Perhaps you could feed the bunny? What will you do? (touch/ carrots/ water): """)
	if choice == "touch":
		print """
As you reach your hand out towards the rabbit, Karate Bunny's karate instincts kick in and it flips you over its head. You black out: Game Over."""
		return False
	elif choice == "carrots" or choice == "water":
		print """
You give the bunny """ + choice + ". It loves it. You walk pass the bunny without trouble."
		return True

def sensorbeams():
	print """
You warily eyeball the sensor beams. Crossing your fingers, you attempt to move forward."""
	possibility = random.randint(0, 1)
	if possibility:
		print """
Through skill and sheer dumb luck, you successfully pass through the sensor beams without harm or detection."""
		return True
	else:
		print """
With an unfortunate misstep, you hit the sensor beams and was immediately arrested: Game Over"""
		return False
def yourweapon():
	pocket = raw_input("You chose to engage the two guards, you need a weapon. Which pocket will you put your hand into to find a weapon? (left/ right): ")
	if pocket == "left":
		leftweapon = raw_input("You rummage your left pocket to find three items. Which one do you pick as your weapon? (paper clip/ apple/ gun): ")
		if leftweapon == "paper clip":
			strength = int(random.random()*10)
			print """
Your paper clip was a magical sword in disguise. It changes it's strength depending on its mood. Its power level today is """ + str(strength) + "."
			return strength
		elif leftweapon == "apple":
			print """
How do you expect to fight with an apple? Well... if you insist... Its power level is 1."""
			return 1
		elif leftweapon == "gun":
			print """
Wise choice, a gun should easily handle two guards. Its power level is 10."""
			return 10
		else:
			randomweapon = int(random.random()*50)
			print """
Instead of picking from the choices in your left pocket, you stick your hand into a mystical portal to draw out a """ + leftweapon + "." + " Your weapon's power level is " + str(randomweapon) + "."
			return randomweapon

	elif pocket == "right":
		rightweapon = raw_input("You rummage your right pocket to find two items. Which one do you pick as your weapon? (dagger/ cheesestick): ")
		if rightweapon == "dagger":
			print """
The dagger was actually made of rubber. It is harmless. Its power level is 0."""
			return 0
		elif rightweapon == "cheesestick":
			print """
For real man? A cheesestick as a weapon? Its power level is 2."""
			return 2
		else:
			randomweapon = int(random.random()*50)
			print """
Instead of picking from the choices in your right pocket, you stick your hand into a mystical portal to draw out """ + rightweapon + "." + " Your weapon's power level is " + str(randomweapon) + "."
			return randomweapon

def guardfight(yourweapon):
	baton = 5
	if yourweapon > baton:
		print "Your weapon of choice overpowers that of the guards."
		print "You win the fight with the guards"
		return True
		
	elif yourweapon < baton:
		print """Your poor choice in a weapon ended up with your loss. You are arrested by the guards: Game Over"""
		return False
#Main
def main():
	print "Stealing the Artifact of Dumbo"
	print """
You are a robber and you are attempting to steal the Artifact of Dumbo. It is now night time and you decide on how to enter the museum which holds this sacred object."""
	enter()
	

main()
