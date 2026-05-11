12
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15

n = int(input("n"))
c=1
for i in range(1,n+1):
    if i%2 != 0:
        c=c*(i)
print(c)        
        


2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4

n = int(input("n 1 : "))
m = int(input("n 2 : "))
c=0
for i in range(n,m+1):
    if i%7 == 0:
        c=c+1
print(c)  



3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35

n = int(input("n 1 : "))
m = int(input("n 2 : "))

for i in range(n,m+1):
    if i%5 == 0 and i%10 != 0:
        print(i)


4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
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


5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number
n = int(input("Enter the no1. : "))
sum =0
for i in str(n):
    sum = sum + int(i)
    
if n% sum ==0:
    print("Harshed no")
else:
    print("wrong no.")


6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number


7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number


n = input("Enter Number = ")
m = n
length = len(m)
if int(n)//10**(length-1)==0:
    print("Not Duck Number")
else:
    for i in n:
        if i=="0":
            print("Duck Number")
            break
    else:
        print("Not Duck Number")
      


8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified



9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number