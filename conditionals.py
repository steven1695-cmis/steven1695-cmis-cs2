print "Stealing the Artifact of Dumbo"
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
#If you pick the bunny, you are given the choice of .

#If you have passed the following obstacles, you are now in front of the Artifact of Dumbo but there are two. One is a fake.
#You need to solve a series of questions to get the true artifact.
#If you get all of the questions right, you leave with the real artifact, if you get even one of them wrong, you leave the museum with the fake artifact.

#Defined Functions used in main
import random
def finaldestination():
	print "You have passed all the obstacles up to this point and you have reached the artifact of Dumbo. However, there are TWO! One is definitely a fake. In order for you to get the true artifact, you must solve three problems correctly. "
	cakeriddle = int(raw_input("What is the maximum amount of slices you can have with three cuts on a cake? "))
	foreignriddle = int(raw_input("In a certain country, ½ of 5 = 3. If the same proportion holds, what is the value of 1/3 of 10? "))
	phoneriddle = int(raw_input("What number do you get when you multiply all of the numbers on a telephone's number pad? "))
	numberwrong = 0
	if not cakeriddle == 8:
		numberwrong += 1
	if not foreignriddle == 4:
		numberwrong += 1
	if not phoneriddle == 0:
		numberwrong += 1
	if cakeriddle == 8 and foreignriddle == 4 and phoneriddle == 0:
		"All Correct! You have solved all the riddles correctly. And you run into the night with the Artifact of Dumbo in your grasp."
	else:
		say = """You were wrong {} times. You end up taking the fake Artifact of Dumbo.""" 
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
	print "Karate Bunny eyes you expectantly and you are hopelessly captivated by its adorable gaze. It suddenly gives grabs you by your pinky finger and slams you onto your backside over its head. You black out: Game Over"
def sensorbeams():
	print "You warily eyeball the sensor beams. Crossing your fingers, you attempt to move forward."
	possibility = random.randint(0, 1)
	if possibility:
		print "Through skill and sheer dumb luck, you successfully pass through the sensor beams without harm or detection."
		finaldestination()
	else:
		print "With an unfortunate misstep, you hit the sensor beams and was immediately arrested."
		
def yourweapon():
	pocket = raw_input("You chose to engage the two guards, you need a weapon. Which pocket will you put your hand into to find a weapon? (left/ right): ")
	if pocket == "left":
		leftweapon = raw_input("You rummage your left pocket to find three items. Which one do you pick as your weapon? (paper clip/ apple/ gun): ")
		if leftweapon == "paper clip":
			strength = random.random()*10
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
		finaldestination()
		
	else:
		print """Your poor choice in a weapon ended up with your loss. You are arrested by the guards: Game Over"""

#Main
def main():
	print "You are a robber and you are attempting to steal the Artifact of Dumbo. It is now night time and you decide on how to enter the museum which holds this sacred object."
	enter()

main()
