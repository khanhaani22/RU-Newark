"""
NAME: Haani Khan
DATE: October 3, 2024
UNIT: 3
ASSIGNMENT:
"""

# code starts here
total_seconds = int(input("How many seconds have passed? "))
first = total_seconds
days = 0
hours = 0
minutes = 0
if (total_seconds >= 86400):
    days = total_seconds//86400
    total_seconds %= 86400
    if (total_seconds >= 3600):
        hours = total_seconds//3600
        total_seconds %= 3600
    if(total_seconds >= 60):
        minutes = total_seconds//60
        total_seconds %= 60
    print(f"{first} seconds is equal to {days} days, {hours} hours, {minutes} minutes, {total_seconds} seconds.")

elif(total_seconds >= 3600 and total_seconds < 86400):
    hours = total_seconds//3600
    total_seconds %= 3600
    if(total_seconds >= 60):
        minutes = total_seconds//60
        total_seconds %= 60
    print(f"{first} seconds is equal to {hours} hours, {minutes} minutes, {total_seconds} seconds.")

elif(total_seconds >= 60 and total_seconds < 3600):
    minutes = total_seconds//60
    total_seconds %= 60
    print(f"{first} seconds is equal to {minutes} minutes, {total_seconds} seconds.")

elif(total_seconds < 0):
    print("The number of seconds cannot be negative")

else:
    print(total_seconds + " seconds is equal to " + total_seconds + " seconds.")        




# OUTPUT: 
"""
Paste output here!
How many seconds have passed? 1252108
1252108 seconds is equal to 14 days, 11 hours, 48 minutes, 28 seconds.
"""
