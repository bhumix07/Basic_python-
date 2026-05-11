"""5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome
"""


n = int(input(" palindrome no. : "))
a = 0
n1 = n 
while n >0:
    rem = n % 10 
    a = a * 10 + rem
    n = n//10 

if n1 == a :


    print("is a palindrome")
else:
    print("not palindrome ")
