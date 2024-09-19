"""
NAME: Haani Khan 
DATE: September 19, 2024
UNIT: 2
ASSIGNMENT: Stock Transaction Program
"""

# code starts here

shares_bought = 2000
paid_stock =  (shares_bought * 40)
shares_sold = 2000
sold_stock = (shares_sold * 42.75)
money_total = (sold_stock - paid_stock)
money_broker = ((money_total) * 0.03)
money_you = (money_total - money_broker)
print("Joe paid $" + str(paid_stock) + " for the stock.")
print("Joe sold the stock for $"+ str(sold_stock) + ".")
print("Joe has $" + str(money_total) + " after he sold the stock.")
print("Joe paid the broker $" + str(money_broker) + ".")
print("Joe has $" + str(money_you) + " after he paid the broker.")


# OUTPUT: 
"""
Paste output here!
Joe paid $80000 for the stock.
Joe sold the stock for $85500.0.
Joe has $5500.0 after he sold the stock.
Joe paid the broker $165.0.
Joe has $5335.0 after he paid the broker.

"""