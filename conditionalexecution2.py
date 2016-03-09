#getAttackValue.py defines a function.
#This function asks for a raw input from the use on what attack value you want between 0 and 99
#However, this is irrelevant because your raw_input is a string so it will always be true in boolean
#and you will get a random number for your attack value from the "if" coding.
#The random number is then divided by 100 and becomes the return value.
#However, all this wouldn't work because "random" was not imported first hand.

import random

def getAttackValue():
 
    number = raw_input("Type attack value (0-99): ")

    if number > 99 or number < 0:
        number = random.randint(0, 99)

    attackValue = float(number)/100
    return attackValue    

print getAttackValue()

