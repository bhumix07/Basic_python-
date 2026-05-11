'''1.Digit Product Analyzer System

A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

For every entered number, the system analyzes relationships between its digits.

Write a program to:

Find the product of every pair of adjacent digits
Display all the products
Find the sum of all these products
Find the smallest product value
If the sum of products is divisible by the total number of digits, print Stable Number
Otherwise print Unstable Number

Use loops wherever required.

Input:
57294

Output:
Products: 35 14 18 36
Sum = 103
Smallest = 14
Unstable Number
'''
n = input("Enter number: ")

sum_prod = 0
smallest = 9999

print("Products:", end=" ")

for i in range(len(n)-1):
    p = int(n[i]) * int(n[i+1])
    
    print(p, end=" ")   # direct print
    sum_prod += p
    
    if p < smallest:
        smallest = p

print("\nSum =", sum_prod)
print("Smallest =", smallest)

if sum_prod % len(n) == 0:
    print("Stable Number")
else:
    print("Unstable Number")