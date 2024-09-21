"""
NAME: Haani Khan
DATE: September 19, 2024
UNIT: 2
ASSIGNMENT 1: Compound Interest
"""

# code starts here
print("-=+=- COMPOUND INTEREST CALCULATOR")
original_deposit = float(input ("How much would you like to deposit? \n$"))
interest_rate = (input("What is the annual interest rate? (in percentage) \n%"))
interest_rate = int(interest_rate) / 100
ans = (input("How many times is interest compounded? (Monthly or Quarterly?) \n"))
if (ans == "Monthly"):
    num_compounds = 12 
if (ans == "Quarterly"):
    num_compounds = 4
years = (input("How many years will the account be left to earn interest? \n"))
final_amount = original_deposit * (1 + ((interest_rate) / (num_compounds))) ** (int(num_compounds) * int(years))
print("The account will have $" + str(round(final_amount, 2)) + " after " + years + " years.")





# OUTPUT: 
"""
Paste output here!
-=+=- COMPOUND INTEREST CALCULATOR
How much would you like to deposit? 
$1002
What is the annual interest rate? (in percentage) 
%7
How many times is interest compounded? (Monthly or Quarterly?) 
Monthly
How many years will the account be left to earn interest? 
24
The account will have $5350.11 after 24 years.
"""