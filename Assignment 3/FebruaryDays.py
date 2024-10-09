"""
NAME: Haani Khan
DATE: October 3, 2024
UNIT: 3
ASSIGNMENT:
"""

# code starts here
year = int(input("Enter a year: "))
if ((year % 100) == 0) and ((year % 400) == 0):
    print(f"In {year} February has 29 days.")
elif ((year % 4) == 0) and ((year % 100 != 0)):
    print(f"In {year} February has 29 days.")
else:
    print(f"In {year} February has 28 days.")



# OUTPUT: 
"""
Paste output here!
Enter a year: 3000
In 3000 February has 28 days.
"""