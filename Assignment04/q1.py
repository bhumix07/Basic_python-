"""Assignment 1: Restaurant Bill Split
A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.
Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75"""



bill = float(input("enter bill amount.."))
gst = float(input("enter gst"))
charge = float(input("enter charge"))
fnd = float(input("enter fnd"))

tax = gst + charge
extra = bill*tax/100 
total = extra + bill
each = total/fnd
print(total)
print(each)