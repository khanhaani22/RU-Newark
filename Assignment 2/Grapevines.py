"""
NAME: Haani Khan
DATE: September 19, 2024
UNIT: 2
ASSIGNMENT: Planting Grapevines
"""

# code starts here
print("Assignment 2.2 - Planting Grapevines")
row_length = (input("How long is the row? (in feet) \n"))
feet_space = (input("How much space is an end-post assembly? (in feet)\n"))
vine_space = (input("How much space is between the vines? (in feet) \n"))
gpvines_fit = ((float(row_length) - 2 * float(feet_space)) / float(vine_space))
print(str(gpvines_fit) + " grapevines fit in the row.")



# OUTPUT: 
"""
Paste output here!
Assignment 2.2 - Planting Grapevines
How long is the row? (in feet) 
10
How much space is an end-post assembly? (in feet)
1
How much space is between the vines? (in feet) 
0.5
16.0 grapevines fit in the row.
"""

