import math
"""
NAME: Haani Khan
DATE: November 11, 2024
UNIT: 5
ASSIGNMENT:
"""

# code starts here
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def rectangle(length, width):
    area = length * width
    perimeter = (length + width) + (length + width)
    return area, perimeter

ans = (input("Would you like to work with rectangles or circles? "))
if ans == "rectangles":
    shape = 1
if ans == "circles":
    shape = 2
        
if (shape == 1):
    x = int(input("What is the length of the rectangle? \n"))
    y = int(input("What is the width of the rectangle? \n"))
    area, perimeter = rectangle(x, y)
    print(f"The area of the rectangle is {area} and the perimeter is {perimeter}")

if (shape == 2):
    r = int(input("What is the radius of the circle? \n"))
    area, circumference = circle(r)
    print(f"The area of the circle is {area} and the circumference is {circumference}")

# OUTPUT: 
"""
Would you like to work with rectangles or circles? rectangles
What is the length of the rectangle? 
4
What is the width of the rectangle? 
2
The area of the rectangle is 8 and the perimeter is 12

Would you like to work with rectangles or circles? circles
What is the radius of the circle? 
8
The area of the circle is 201.06192982974676 and the circumference is 50.26548245743669
"""

