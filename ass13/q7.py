'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
n = int(input("Enter number: "))

# Step 1: Sum of digits
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp = temp // 10

print("Sum =", sum)

# Step 2: Check prime
if sum <= 1:
    print("Normal Number")
else:
    prime = True

    for i in range(2, sum):
        if sum % i == 0:
            prime = False
            break

    if prime:
        print("Lucky Number")
    else:
        print("Normal Number")