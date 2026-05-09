'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2

'''
n = int(input("Enter number: "))

count = 0
smallest = None

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

        if i > 1 and smallest is None:
            smallest = i

if count > 2:
    print("Composite Number")
    print("Factors Count =", count)
    print("Smallest Factor =", smallest)
else:
    print("Not Composite Number")
    print("Factors Count =", count)