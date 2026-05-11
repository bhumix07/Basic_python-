'''
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''
n = int(input("Enter the no. : "))
count = 0
for i in range(1,n+1):
    if i % 7 == 0:
        count += 1



print(count)
        