'''5.
Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.
'''
y = int(input("enter the year : "))


x = "Leap year" if y%4==0 or y%400==0 and y%100 else "not leap year"
print(x) 