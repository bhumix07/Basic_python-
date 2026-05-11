"""
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5"""

salary = int(input("enter salary.."))
days =int(input("total days of work"))
hrs =int(input("total hrs of work"))

perday = salary/ days
perhrs = perday/hrs


print(perday)
print(perhrs)