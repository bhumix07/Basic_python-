""""
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0"""


dis = int(input("distance"))
mil = int(input("per km "))
price = int(input("petrol price"))

petrol = dis/mil
total_cost = petrol*price 

print("petrol used",petrol)
print("total cost",total_cost)