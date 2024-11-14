import geometry
"""
NAME: Haani Khan
DATE: November 11, 2024
UNIT: 5
ASSIGNMENT:
"""

# code starts here
i = 0
while i == 0:
    print("Would you like to calculate... ")
    print("1. Area of a circle")
    print("2. Circumference of a circle")
    print("3. Area of a rectangle")
    print("4. Perimeter of a rectangle")
    print("q. Quit the program")
    ans = (input("Type the option (1,2,3,4, or q): \n"))
    if (ans == "1"):
        radius = int(input("What is the radius of the circle? \n"))
        geometry.areaCircle(radius)
    if (ans == adius"2"):
        radius = int(input("What is the radius of the circle? \n"))
        geometry.circumCircle(radius)
    if (ans == "3"):
        length = int(input("What is the length of the rectangle? \n"))
        width = int(input("What is the width of the rectangle? \n"))
        geometry.areaRect(length, width)
    if (ans == "4"): 
        length = int(input("What is the length of the rectangle? \n"))
        width = int(input("What is the width of the rectangle? \n"))
        geometry.periRect(length, width)
    if (ans == "q"):
        i += 1
# OUTPUT: 
"""
Would you like to calculate... 
1. Area of a circle
2. Circumference of a circle
3. Area of a rectangle
4. Perimeter of a rectangle
q. Quit the program
Type the option (1,2,3,4, or q): 
4
What is the length of the rectangle? 
8
What is the width of the rectangle? 
1
The perimeter is 18 units.
Would you like to calculate... 
1. Area of a circle
2. Circumference of a circle
3. Area of a rectangle
4. Perimeter of a rectangle
q. Quit the program
Type the option (1,2,3,4, or q): 
q
"""

