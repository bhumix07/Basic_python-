"""Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67"""


total = int(input("total run"))
overs = float(input("overs"))

x = overs*10
y = x%10
z = x//10 
totalbolls = z*6+y
h = totalbolls/6

runrate = total/h
print(totalbolls)
print(runrate)