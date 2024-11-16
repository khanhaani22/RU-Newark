import random
"""
NAME: Haani Khan
DATE: November 11, 2024
UNIT: 5
ASSIGNMENT:
"""

# code starts here
def main():
    amtGuess = 0
    i = 0
    randomNumber = random.randint(1, 100)
    while (i == 0):
        guess = int(input("Guess the Number (1-100): "))
        if guess > randomNumber:
            print("Too high, try again")
            amtGuess += 1
        if guess < randomNumber:
            print("Too low, try again")
            amtGuess += 1
        if guess == randomNumber:
            amtGuess += 1
            print("Congratulations! Thats correct!")
            print(f"It took you {amtGuess} tries!")
            i += 1
            

x = 0
while (x == 0):
    main()
    print("Play again? Y/N")
    ans = input("")
    if ans == "N":
        x = 1
# OUTPUT: 
"""
Guess the Number (1-100): 25
Too low, try again
Guess the Number (1-100): 50
Too low, try again
Guess the Number (1-100): 75
Too low, try again
Guess the Number (1-100): 80
Too low, try again
Guess the Number (1-100): 90
Congratulations! Thats correct!
It took you 5 tries!
Play again? Y/N
Y
Guess the Number (1-100): 50
Too low, try again
Guess the Number (1-100): 75
Too high, try again
Guess the Number (1-100): 60
Too low, try again
Guess the Number (1-100): 65
Too high, try again
Guess the Number (1-100): 63
Too high, try again
Guess the Number (1-100): 3
Too low, try again
Guess the Number (1-100): 3
Too low, try again
Guess the Number (1-100): 61
Congratulations! Thats correct!
It took you 8 tries!
Play again? Y/N
N
"""

