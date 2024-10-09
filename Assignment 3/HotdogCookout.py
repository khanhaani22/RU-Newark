"""
NAME: Haani Khan
DATE: October 3, 2024
UNIT: 3
ASSIGNMENT:
"""

# code starts here
people = int(input("How many people will be attending the cookout? \n"))
dogs_per_person = int(input("How many hot dogs will each person be given? \n"))
dogs_needed = people * dogs_per_person
if ((dogs_needed % 10) != 0):
    dogpackages_needed = (dogs_needed / 10) + 1
else:
    dogpackages_needed = (dogs_needed / 10)
if ((dogs_needed % 8) != 0):
    bunpackages_needed = (dogs_needed / 8) + 1
else:
    bunpackages_needed = (dogs_needed / 8)
    
dogpackages_needed = int(dogpackages_needed)
bunpackages_needed = int(bunpackages_needed)

leftover_dogs = (dogpackages_needed * 10) - dogs_needed
leftover_buns = (bunpackages_needed * 8) - dogs_needed

print(f"Minimum number of packages of hotdogs: {dogpackages_needed}")
print(f"Minimum number of packages of hotdog buns: {bunpackages_needed}")
print(f"Hot dogs left over: {leftover_dogs}")
print(f"Hot dog buns left over: {leftover_buns}")



# OUTPUT: 
"""
Paste output here!
How many people will be attending the cookout? 
10
How many hot dogs will each person be given? 
2
Minimum number of packages of hotdogs: 2
Minimum number of packages of hotdog buns: 3
Hot dogs left over: 0
Hot dog buns left over: 4
"""