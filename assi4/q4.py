"""Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
"""


speed = float(input("Enter speed"))
hrs , min = map(float, input("time hrs and min").split())
hrs1 = min/60
time = hrs+hrs1
dis = speed*time 

print(time)
print(dis)

