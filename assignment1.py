MyName = "Steven Lee" #This is the variable for my name value
MyAgeInYears = 15.83 #This is the variable for my age in years value
MyHeightInMeters = 1.67 #This is the variable for my height in meters value
SquareLengthInFeet = 3 #This is the variable for a square's length in feet value
RectangleLengthInFeet = 2 #This is the variable for a rectangle's length in feet value
RectangleHeightInFeet = 4 #This is the variable for a rectangle's height in feet value
MyAgeInMonths = MyAgeInYears*12 #This is the variable for my age in months value
MyNumberOfYearsLeftToLive = 81.37 - MyAgeInYears #This is the variable for my number of years left to live value
MyHeightInFeet = 3.28084*MyHeightInMeters #This is the variable for my height in feet value
MyHeightDifferenceFromKoreanAverageInMeters = 175.26 - MyHeightInMeters #This is the variable for my height difference from the average korean value
SquareAreaInFeet = SquareLengthInFeet**2 #This is the variable for my square area in feet value
HalfTheVolumeofCubeWithSquareLengthInFeetCubed = (SquareLengthInFeet**3)/2.0 #This is the variable for half the volume of cube with square length in feet cubed value
OneNinthTheAreaOfRectangleInFeet = (RectangleLengthInFeet*RectangleHeightInFeet)/9.0 #This is the variable for 1/9 of the area of the rectangle in feet value
print "Hello, my name is " + str(MyName) + " and I am " + str(MyAgeInYears) + " years old. " + "If you take my age into account, I have " + str(MyNumberOfYearsLeftToLive) + " years left to live. " + "I am " + str(MyHeightInMeters) + " meters tall. " + "If converted into feet, I am " + str(MyHeightInFeet) + " feet tall." #This is a print talking about myself and my numbers
print 'I have a square that is', str(SquareLengthInFeet), 'feet in length.', "The square's area in feet is", str(SquareAreaInFeet), "feet.", "There is also a rectangle that has a length of", str(RectangleLengthInFeet), "feet and a height of", str(RectangleHeightInFeet), "feet.", "1/9 the area of the rectangle is roughly", str(OneNinthTheAreaOfRectangleInFeet), "feet." #This is a print talking about the square and rectangle and different values you can get from them via math
Wink = ";^)" #This is the variable for a winky face value
print str(Wink)*10000 #This is the print of 10,000 winky faces
