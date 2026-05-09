"""
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
"""


n1 = int(input("Enter the no1. : "))
n2 = int(input("Enter the no2. : "))

for i in range(n1+1,n2+1,2):
    if i % 5 == 0:
        print(i)
        
