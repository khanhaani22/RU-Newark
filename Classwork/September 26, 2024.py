#1.1
day = input("Whats the day today? (Type out day of the week)\n")
if day == ["Monday","Tuesday","Wednesday", "Friday"]:
    print("Time to study!")
elif day == "Thursday":
    print("Class")
elif day == ["Saturday","Sunday"]:
    print("Have fun!")

#1.2
age = int(input("How old are you? (Input number)\n"))
if (age == 1):
    print("You are an infant.")
elif (age > 1 and age < 13):
    print("You are a child.")
elif (age > 12 and age < 21):
    print("You are a teenager.")
elif (age > 20):
    print("You are an adult.")
else:
    print("You are not born.")