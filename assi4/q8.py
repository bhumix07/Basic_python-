"""
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0 """



pri , rate , time = map(float, input("amount, ratae ,time").split())

year1 = pri*rate/100
total1 = pri+year1
year2 = total1*rate/100
ftotal = total1+year2


print("amount after interest :", ftotal)

