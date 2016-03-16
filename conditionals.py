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


def guardfight(yourweapon):
	baton = 5
	if yourweapon > baton:
		print "You win the fight with the guards"
	else:
		print """You are arrested by the guards: Game Over"""

def main():
	print "You are a robber and you are attempting to steal the Artifact of Dumbo. It is now night time and you decide on how to enter the museum which holds this sacred object."

	EnterChoice = raw_input("You make a choice of how to enter. (Front Door/ Back Door): ")

	if EnterChoice == "Front Door":
		print "You enter through the front door. You run into two guards on night duty."
	elif EnterChoice == "Back Door":
		print "You enter through the back door. There are no guards. However, you are met by red sensor beams on the left and a karate rabbit on the right."
	else:
		print "You were unable to enter through the method of choice. Try again."
		
	

main()
