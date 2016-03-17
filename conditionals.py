print "Stealing the Artifact of Dumbo"
#You are a criminal, and you seek to steal the Artifact of Dumbo, priced at 3 pebbles.

#You reach the museum building in the night and decide on how to enter.
#Computer asks you how to enter: front door, back door

#If you pick the front door, you are spotted by the security on the way in.
#There are two guards, computer gives you choice: fight guards, run into the next room.
#If you choose to fight, you pick which pocket to pull out a weapon from to contest the batons of the guards. Left: paperclip, apple, gun/Right: dagger, cheesestick
#If you run, you are caught by the guards and arrested: Game Over

#If you pick backdoor, you enter without trouble.
#However, now there are red sensor beams you need to go through to the left or a bunny you need to fight to the right.
#If you decide to go through the sensor beams, you have a 50% chance to succeed. If you fail: Game Over/ If you succeed: Continue
#If you fight the bunny, you are instantly grandslammed but out of pity bunny lets you through.

#If you have passed the following obstacles, you are now in front of the Artifact of Dumbo but there are two. One is a fake.
#You pick one out on random and leave the museum with the artifact.

#Defined Functions used in main
import random
def enter():
	EnterChoice = raw_input("You make a choice of how to enter. (front door/ back door): ")

	if EnterChoice == "front door":
		print "You enter through the front door. You run into two guards on night duty."
		guardchoice = raw_input("Will you engage the guards or run away? (fight guards/ run away): ")
		if guardchoice == "fight guards":
			weaponchoice = yourweapon()
			guardfight(weaponchoice)
		elif guardchoice == "run away":
			print "You attempted to flee but you were cornered by the guards and arrested"
		else:
			print "That is not a viable choice. Try again."
	elif EnterChoice == "back door":
		print "You enter through the back door. There are no guards. However, you are met by red sensor beams on the left and a karate rabbit on the right."
		choice = raw_input("Which side do you want to go to? (left/ right): ")
		if choice == "left":
			sensorbeams()
		elif choice == "right":
			karatebunny()
		else:
			print "Sorry, not an option. Try again."
	else:
		print "You were unable to enter through the method of choice. Try again."
def karatebunny():
def sensorbeams():
def yourweapon():
	pocket = raw_input("You chose to engage the two guards, you need a weapon. Which pocket will you put your hand into to find a weapon? (left/ right): ")
	if pocket == "left":
		leftweapon = raw_input("You rummage your left pocket to find three items. Which one do you pick as your weapon? (paper clip/ apple/ gun): ")
		if leftweapon == "paper clip":
			strength = random.randint(0, 10)
			print "Your paper clip was a magical sword in disguise. It changes it's strength depending on its mood. Its power level today is " + str(strength) + "."
			return strength
		elif leftweapon == "apple":
			print "How do you expect to fight with an apple? Well... if you insist..."
			return 1
		elif leftweapon == "gun":
			print "Wise choice, a gun should easily handle two guards."
			return 10
		else:
			print "Sorry, not an option. Try again."

	elif pocket == "right":
		rightweapon = raw_input("You rummage your right pocket to find two items. Which one do you pick as your weapon? (dagger/ cheesestick): ")
		if rightweapon == "dagger":
			print "The dagger was actually made of rubber. It is harmless."
			return 0
		elif rightweapon == "cheesestick":
			print "For real man? A cheesestick as a weapon?"
			return 2
		else:
			print "Sorry, not an option. Try again."
	else:
		print "Are you sure thats how you write left or right?"

def guardfight(yourweapon):
	baton = 5
	if yourweapon > baton:
		print "Your weapon of choice overpowers that of the guards."
		print "You win the fight with the guards"
	else:
		print """Your poor choice in a weapon ended up with your loss. You are arrested by the guards: Game Over"""

#Main
def main():
	print "You are a robber and you are attempting to steal the Artifact of Dumbo. It is now night time and you decide on how to enter the museum which holds this sacred object."
	enter()

main()
