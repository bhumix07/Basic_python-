'''5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number'''


n = int(input("enter no."))
x = 0

for i in str(n):
    
    if x == 0:
        x = int(i)
        
        continue
    if int(i) <=x:
        print("unstable")
        break
    x = int(i)
else:
    print("stable")