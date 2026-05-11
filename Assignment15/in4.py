'''4.Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.'''

u = int(input("enter the unit "))

x = 5 if u < 100 else 7 if 101 < unit < 300 else 10 

t =   u*x

print(t)