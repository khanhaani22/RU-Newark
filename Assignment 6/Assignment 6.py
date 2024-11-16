"""
NAME: Haani Khan
DATE: November 15, 2024
UNIT: 6
ASSIGNMENT:
"""

# code starts here
with open("Assignment 6/readme.txt","r") as file:
    lines = file.readlines()
scores = []
for line in lines:
    name, score = line.strip().split(",")
    scores.append((name,int(score)))
    
avg = sum([x[1] for x in scores])/len(scores)

max = max([x[1] for x in scores])
max_ind = 0
for x in scores:
    if x[1] == max:
        max_ind = scores.index(x)
max_name = scores[max_ind][0]
max_score = f'{max_name}, {max}'

min = min([x[1] for x in scores])
min_ind = 0
for x in scores:
    if x[1] == min:
        min_ind = scores.index(x)
min_name = scores[min_ind][0]
low_score = f'{min_name}, {min}'

out = open("Assignment 6/output.txt", "w")
out.write(f"Average Score: {avg}\n\n")
out.write(f"Highest Score: {max_score}\n\n")
out.write(f"Lowest Score: {low_score}\n\n")
    

