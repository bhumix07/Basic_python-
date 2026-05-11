"""
Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
"""

price , pay , irate , month = map(float,input("enter price pay irate and month.").split())

rem_amount = price - pay

int_rate = rem_amount*month/100

total_i = rem_amount + int_rate

month_emi = total_i/month 


print(rem_amount)
print(total_i)
print(month_emi)




