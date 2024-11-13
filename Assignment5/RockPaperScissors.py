import random
"""
NAME: Haani Khan
DATE: November 11, 2024
UNIT: 5
ASSIGNMENT:
"""

# code starts here
def main():
    global user
    global cpu
    cpu = random.randint(1, 3)
    user = input("Rock, Paper, or Scissors?: ")
    if user == "rock":
        user = 1
    if user == "paper":
        user = 2
    if user == "scissors":
        user = 3
    checkWin()

def checkWin():
    if (user == 1):
        if (cpu == 1):
            print ("Cpu chose Rock")
            print("Rock vs Rock, try again!")
            main()
        if (cpu == 2):
            print ("Cpu chose Paper")
            print("Rock vs Paper, you lose!")
        if (cpu == 3):
            print ("Cpu chose Scissors")
            print("Rock vs Scissors, you win!")
    if (user == 2):
        if (cpu == 1):
            print ("Cpu chose Rock")
            print("Paper vs Rock, you win!")
        if (cpu == 2):
            print ("Cpu chose Paper")
            print("Paper vs Paper, try again!")
            main()
        if (cpu == 3):
            print ("Cpu chose Scissors")
            print("Paper vs Scissors, you lose!")
    if (user == 3):
        if (cpu == 1):
            print ("Cpu chose Rock")
            print("Scissors vs Rock, you lose!")
        if (cpu == 2):
            print ("Cpu chose Paper")
            print("Scissors vs Paper, you win!")
        if (cpu == 3):
            print ("Cpu chose Scissors")
            print("Scissors vs Scissors, try again!")
            main()

main()


# OUTPUT: 
"""
Rock, Paper, or Scissors?: scissors
Cpu chose Scissors
Scissors vs Scissors, try again!
Rock, Paper, or Scissors?: paper
Cpu chose Paper
Paper vs Paper, try again!
Rock, Paper, or Scissors?: rock
Cpu chose Rock
Rock vs Rock, try again!
Rock, Paper, or Scissors?: rock
Cpu chose Paper
Rock vs Paper, you lose!
"""

