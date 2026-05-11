# Assignment 1: Speed Calculator
# Write a Python program that:
# Accepts distance (in km) and time (in hours).Calculates speed.

# Input:
# Distance = 120
# Time = 2
# Output:
# Speed = 60 km/h

distance = float(input("Enter Distance in KM: "))
time =  float(input("Enter Time in Hrs: "))
print("Speed :",distance/time,"km/h")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 2: Salary Calculator
# Write a Python program that:
# Accepts daily wage and number of days. Calculates total salary.

# Input:
# Daily wage = 500
# Days = 26
# Output:
# Salary = 13000

wage, days = map(float,input("Enter Daily wage and Number of Days : ").split())
print(f"Salary : {wage*days}")


print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 3: Electricity Bill Calculator
# Write a Python program that:
# Accepts number of units.
# Calculates bill (₹6 per unit).

# Input:
# Units = 100
# Output:
# Bill = 600

units = float(input("Enter the number of units: "))
print("Bill : ",units*6,"₹",sep="")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 4: Area of Rectangle
# Write a Python program that:
#Accepts length and breadth. Calculates area.

# Input:
# Length = 10
# Breadth = 5
#Output:
#Area = 50

length = float(input("Enter Length\t: "))
breadth = float(input("Enter Breadth\t: "))
print("Area\t:",length*breadth)


print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 5: Average Marks Calculator
# Write a Python program that:
# Accepts marks of 3 subjects. Calculates average.

# Input:
# Marks = 80, 90, 70
# Output:
# Average = 80.0'''

m1,m2,m3 = map(float,input("Enter three subject marks: ").split())
print("Average : ",((m1+m2+m3)/3))

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 6: Discount Calculator
# Write a Python program that:
# Accepts total amount. Calculates 10% discount and final price.

amount = float(input("Enter total amount : "))
dis_value = amount*10/100
total = amount-dis_value
print("Total amount to be paid : ",total)



print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 7: Circle Area Calculator
# Write a Python program that:
# Accepts radius. Calculates area of circle.

# Input:
# Radius = 7
# Output:
# Area = 153.86

r = float(input("Enter the radius: "))
print("Area\t:",round(3.14*r*r,3))

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 8: Data Storage Converter
# Write a Python program that:
# Accepts value in MB.Converts into GB.

# Input:
# MB = 2048
# Output:
# GB = 2.0

value = float(input("Enter the value in MB: "))
print(value,"MB in GB is :",round(value/1024,2))


print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 9: Fuel Cost Calculator
# Write a Python program that:
# Accepts distance (km), mileage (km/litre), and petrol price. Calculates total fuel cost.

# Input:
# Distance = 100
# Mileage = 20
# Petrol Price = 100
# Output:
# Cost = 500

distance,mileage,price = map(float,input("Enter distance (km), mileage (km/litre), and petrol price: ").split())
print("Cost :",round(distance/mileage*price,3))

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 10: Percentage Calculator
# Write a Python program that:
# Accepts total marks and obtained marks. Calculates percentage.

# Input:
# Total = 500
# Obtained = 400
# Output:
# Percentage = 80%

total,obtained = map(float,input("Enter total and obtained marks :").split())
print("Percentage : ",(obtained/total*100),"%",sep="")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 11: Time Duration Adder
# Write a Python program that:
# Accepts hours, minutes, seconds. Converts into total seconds.

# Input:
# Hours = 1
# Minutes = 2
# Seconds = 30
# Output:
# Total Seconds = 3750

hrs,mins,sec = map(int,input("Enter hours, minutes, seconds: ").split())
print("Total Seconds: ",((hrs*3600)+(mins*60)+sec))

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 12: Change Return System
# Write a Python program that:
# Accepts amount. Calculates ₹100, ₹50, ₹10 notes.

# Input:
# Amount = 380
# Output:
# ₹100 x 3
# ₹50 x 1
# ₹10 x 3'''


amount = int(input("Enter Total Amount :"))
hundred_notes = amount//100
x = amount- (hundred_notes*100)
fifty_notes = x//50
y = x-(fifty_notes*50)
ten_notes = y//10

print("₹100 x",hundred_notes,"\n₹50 x",fifty_notes,"\n₹10 x",ten_notes)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 13: Compound Interest Calculator
# Write a Python program that:
# Accepts principal, rate, and time. Calculates compound interest.

# Input:
# Principal = 1000
# Rate = 10
# Time = 2
# Output:
# Amount = 1210.0
# Compound Interest = 210.0

principal,rate,time = map(float,input("Enter Principal, Rate, and Time: ").split())
CI = round(principal*(1+(rate/100))**time,2)
print("CI: ",CI,"\nAmount: ",CI+principal)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# Assignment 14: Simple Profit or Loss Calculator
# Write a Python program that:
# Accepts cost price and selling price.
# Calculates profit/loss and percentage.

# Input:
# Cost Price = 1000
# Selling Price = 1200
# Output:
# Profit = 200
# Profit % = 20.0'''

cost_price,selling_price= map(float,input("Enter Cost Price and Selling Price (use comma to separate) :").split(","))
if(cost_price>selling_price):
 loss = cost_price-selling_price
 print("Loss\t:",loss)
 print("Loss%\t:",(loss/cost_price)*100)
elif cost_price<selling_price:
 profit = selling_price - cost_price
 print("Profit\t:",profit)
 print("Profit%\t:",(profit/cost_price)*100)
else:
 print("No Profit , No Loss")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------


# Assignment 15: Average Speed for Multiple Trips
# Write a Python program that:
# Accepts distance1, time1, distance2, time2.
# Calculates average speed.

# Input:
# Distance1 = 60
# Time1 = 1
# Distance2 = 40
# Time2 = 1
# Output:
# Average Speed = 50 km/h'''

d1,t1 = map(float,input("Enter the Distance1,Time1 (Separate using comma): ").split(","))
d2,t2 = map(float,input("Enter the Distance2,Time2 (Separate using comma): ").split(","))
print("Average Speed: ",((d1+d2)/(t1+t2)),"km/h")

