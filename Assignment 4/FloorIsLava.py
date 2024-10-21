"""
NAME: Haani Khan
DATE: October 19, 2024
UNIT: 4
ASSIGNMENT:
"""

# code starts here
num = int(input("Enter the floor number: "))
num2 = int(2)
num3 = num
if ((num3 % 2) == 0):
    num3 -= 1
while (num2 <= num):
    print(num2)
    num2 += 2
while (num3 > 0):
    print(num3)
    num3 -= 2
    



# OUTPUT: 
"""
Enter the floor number: 14
2
4
6
8
10
12
14
13
11
9
7
5
3
1
"""

