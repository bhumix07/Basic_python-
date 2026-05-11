'''
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

'''




n1 = int(input("Enter transaction id.1 : "))
sum = 0
rev = 0
n = n1


while n > 0:
    a = n%10
    rev = rev *10 + a
    n = n // 10
print("Reverse : ",rev)



diff = abs(rev - n1)
diff1  = diff 
sum1 = 0
print("diff is",diff)
if diff == 0:
    print("digit 1")

while diff > 0:
    x = diff % 10
    sum1 += 1
    diff = diff //10
print("digits",sum1)

if diff1 == 0:
    print("perfect match ")

elif diff1 // 9:
    print("Verified")

else:
    print("rejected")


	



