
'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''

vt = input("Enter the Vehicle type (Bike/Car/Bus) : ")
hour = int(input("Enter the Hours parked : "))
if vt=="bike" or vt =="Bike":
   if hour<=5:
      fee = hour*10
   else:
      fee = (hour*10)+100
elif vt=="car" or vt=="Car":
   if hour<=5:
      fee = hour*20
   else:
      fee = (hour*20)+100
else:
   if hour<=5:
      fee = hour*50
   else:
      fee = (hour*50)+100

print("Total Parking Fee: ₹",fee) 