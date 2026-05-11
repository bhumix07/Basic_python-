'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''


n = int(input("Enter the no1. : "))
fact = 1
f=1
sum =0
n1 = n
while n>0:
    a = n%10
    for i in range (1,a+1):
        f = f*i
    sum = sum+f
    f=1
    n=n//10
if sum == n1:
    print(sum,"strong no.")
