# Haani Khan
# I am not actually from Seattle sadly.
#ASSIGNMENT 1.1
print ("Haani Khan")
print ('2400 Jackson St')
print ('Seattle, Washington 98039')
print ("206-956-1055")
print ("I am a Computer Science Major.")

#ASSIGNMENT 1.2
total_sales = int(input("Total Sales: $"))
annual_profit = (total_sales * 0.23)
print("Annual Profit is $" + str(annual_profit))

#ASSIGNMENT 1.3
total_sqft = int(input("Total square feet in a tract of land? "))
num_acres = (total_sqft / 43560)
print("Total number of acres in the tract of land is " + str(num_acres) + " acres.")

#ASSIGNEMNT 1.4
print("SIMULATION!!!")
print("You are purchasing FIVE items...")
print("How much did each cost?")
item_a = int(input("Item 1: $"))
item_b = int(input("Item 2: $"))
item_c = int(input("Item 3: $"))
item_d = int(input("Item 4: $"))
item_e = int(input("Item 5: $"))
subtotal = item_a + item_b + item_c + item_d + item_e
tax = subtotal * 0.07
total = subtotal + tax
print("Subtotal: $" + str(subtotal))
print("7% Sales Tax")
print("Total: $" + str(total))

#ASSIGNMENT 1.5
speed_car = 70
d1 = speed_car * 6
d2 = speed_car * 10
d3 = speed_car * 15
print("The car will travel " + str(d1) + " miles in 6 hours.")
print("The car will travel " + str(d2) + " miles in 10 hours.")
print("The car will travel " + str(d3) + " miles in 15 hours.")

#ASSIGNMENT 1.6
price = int(input("How much was that last purchase...? $"))
print("5% State and 2.5% Country Sales Tax")
state_tax = price * 0.05
country_tax = price * 0.025
tax = state_tax + country_tax
total = price + tax
print("-----------------------------")
print("Purchase: $" + str(round(price, 2)))
print("State Sales Tax (5%): $" + str(round(state_tax, 2)))
print("Country Sales Tax (2.5%): $" + str(round(country_tax, 2)))
print("Total Sales Tax (State + Country): $" + str(round(tax, 2)))
print("Final Sale: $" + str(round(total, 2)))

#ASSIGNEMNT 1.7
miles_driven = float(input("Miles Driven? "))
gas_used = float(input(("Gallons of Gas Used? ")))
mpg = miles_driven / gas_used
print("The car used " + str(round(mpg, 3)) + " miles per gallon")

#ASSIGNMENT 1.8
print("Welcome to UNTITLED Restaurant!")
print("WARNING: Automatic 18% Tip and 7% Sales Tax!!!")
meal_purchase = float(input("How much was your meal? $"))
tip = meal_purchase * 0.18
sales_tax = meal_purchase * 0.07
total = meal_purchase + tip + sales_tax
print("----------------------------------")
print("-=+=- Your Tab -=+=-")
print("Item 1: $" + str(meal_purchase))
print("Tip Amount: $" + str(round(tip, 2)))
print("Sales Tax: $" + str(round(sales_tax, 2)))
print("TOTAL: $" + str(round(total, 2)))

#ASSIGNMENT 1.9
cel_input = input("Enter temperature in °C: ")
far_out = ((9/5) * float(cel_input) + 32)
print(cel_input + "° C is the same as " + str(round(far_out, 2)) + "° F.")