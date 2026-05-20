'''5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password'''

p = input("enter pass ")
count=0
count1=0
if p[0].isupper() and p[-1].isdigit()and ' ' not in p and 8 <= len(p) <= 15:
    for c in p:
        if c.isdigit():
            count+=1
        elif c in "@#$%&*":
            count1+=1
        else:
            break

    print("Secure Password")
else:
    print("Insecure Password")