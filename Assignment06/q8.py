"""8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500"""


unit1 = int(input("enter no.1 "))
unit2 = int(input("enter no.2 "))
unit3 = int(input("enter no.3 "))
unit4 = int(input("enter no.4 "))
unit5 = int(input("enter no.5 "))
unit6 = int(input("enter no.6 "))


if unit1 > unit2 and unit1 > unit3 and unit1 > unit4 and unit1 > unit5 and unit1 > unit6:
    print("Highest Stock = ",unit1)

elif  unit2 > unit3 and unit2 > unit4 and unit2 > unit5 and unit2 > unit6:
    print("Highest Stock = ",unit2)
elif  unit3 > unit4 and unit3 > unit5 and unit3 > unit6:
    print("Highest Stock = ",unit3)
elif  unit4 > unit5 and unit4 > unit6:
    print("Highest Stock = ",unit4)
elif  unit5 > unit6:
    print("Highest Stock = ",unit5)
else :
    print("Highest Stock = ",unit6)
