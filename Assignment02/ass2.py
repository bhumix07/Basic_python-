print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 1. Write a Python program that:
# Accepts the total event duration in seconds as input.
# Calculates how many hours, minutes, and seconds it corresponds to.
# Displays the output in the format:
# Hours: x, Minutes: y, Seconds: z

# Sample Input:
# Total event duration in seconds: 3672
# Sample Output:
# Hours: 1, Minutes: 1, Seconds: 12  

total = int(input("Enter Total event duration in seconds : "))
hrs =  total // 3600
x = total %  (hrs*3600)
min = x // 60
sec = total - (hrs*3600+min*60)
print("Hours: ",hrs, "Minutes: ",min,"Seconds: ",sec)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 2. You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

# Write a Python program that:
# Accepts the user’s age in years as input.
# Calculates the approximate number of:
# Days lived (1 year = 365 days)
# Hours lived
# Minutes lived
# Displays the output in the format:
# You've lived approximately:
# Days: xxx
# Hours: yyy
# Minutes: zzz

# Sample Input:
# Enter your age in years: 18
# Sample Output:
# You've lived approximately:
# Days: 6570
# Hours: 157680
# Minutes: 9460800'''

age = int(input("Enter your age in years: "))
days = age*365
hours = days*24
mins = hours*60
print("You've lived approximately: \nDays: ",days)
print("Hours: ",hours,"\nMinutes: ",mins)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 3. You and your friends went out to eat. The bill was quite high and you want to split it evenly.

# Write a Python program that:
# Accepts the total bill amount.
# Accepts the number of friends.
# Displays how much each person should pay.

# Example:
# Total bill = 1250
# Friends = 5
# Each should pay = 250.0'''


amount = float(input("Enter the total bill amount: "))
frnds = float(input("Enter the number of friends: "))
print("Each should pay = ",amount/frnds)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 4. A cab company charges ₹15 per kilometer.

# Write a Python program that:
# Accepts the number of kilometers traveled.
# Calculates the total fare.
# Displays the result.

# Example:
# Distance = 20 km
# Total fare = ₹300'''

distance = float(input("Enter the number of kilometers traveled: "))
fare = distance*15
print("Total fare = ₹",fare,sep="")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 5. Your shopping cart total doesn’t include tax. A 12% GST is applied.

# Write a Python program that:
# Accepts the cart total amount.
# Calculates 12% tax.
# Displays the tax and final total amount.

# Example:
# Cart = ₹2000
# Tax = ₹240
# Total = ₹2240'''

total = float(input("Enter the cart amount: "))
tax = total*12/100
print("Tax = ₹",tax,sep="")
print("Total = ₹",total+tax,sep="")

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 6. You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

# Write a Python program that:
# Accepts the total amount.
# Calculates how many ₹10 coins and ₹5 coins will be dispensed.
# Displays the result.

# Example:
# Amount = ₹35
# Output = ₹10 x 3, ₹5 x 1'''


total = int(input("Enter the total amount: "))
ten_coins = total//10
x = total%(ten_coins*10)
five_coins = x//5
print("₹10 X",ten_coins,", ₹5 X",five_coins)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

# 7. A weather application needs to convert temperature from Celsius to Fahrenheit.

# Write a Python program that:
# Accepts temperature in Celsius as input.
# Converts it to Fahrenheit using the formula:
# F = (C × 9/5) + 32
# Displays the result.

# Example:
# Celsius = 25
# Fahrenheit = 77.0'''

c = float(input("Enter the temperature in Celcius : "))
f = (c*9/5) + 32
print("Fahrenheit =",f)

print("------------------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------------------------

 # 8. A bank wants to help customers calculate the simple interest on their savings.

# Write a Python program that:
# Accepts principal amount, rate of interest, and time (in years) as input.
# Calculates the simple interest using the formula:
# SI = (P × R × T) / 100
# Displays the simple interest.

# Example:
# Principal = 1000
# Rate = 5
# Time = 2
# Simple Interest = 100.0'''


principle,rate,time = map(float,input("Enter Priciple , Rate , Time :\n(Give space after each value )").split())
SI = (principle*rate*time)/100
print("Simple Interest =",SI)




