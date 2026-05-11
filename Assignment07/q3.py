"""3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000
"""

income = int(input("Enter annual income: "))

if income <= 250000:
    print("no tax")
elif 500000 >= income >= 250000:
    a = income*5/100
    print("Tax Payable: ",a)
elif 1000000 >= income >= 500001:
    a = income*20/100
    print("Tax Payable: ",a)
else:
    a = income*30/100
    print("Tax Payable: ",a)