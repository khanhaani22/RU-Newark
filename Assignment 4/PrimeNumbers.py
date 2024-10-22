"""
NAME: Haani Khan
DATE: October 19, 2024
UNIT: 4
ASSIGNMENT:
"""

# code starts here
num = int(input("Enter a number: "))
print(f"The prime numbers up to {num} are:")
for num2 in range(2, num + 1):
    for i in range(2, int(num2**0.5) + 1):
        if num2 % i == 0:
            break
    else:
        print(num2)

# OUTPUT: 
"""
Enter a number: 21
The prime numbers up to 21 are:
2
3
5
7
11
13
17
19
"""

