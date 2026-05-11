"""1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15"""

n = int(input("Enter no. "))
pro = 1
for i in range(1,n+1,2):
   pro = pro*i    
print(pro)

