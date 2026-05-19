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

if p[0].isupper() and p[-1].isdigit() and sum(c.isdigit() for c in p) >= 2 and any(c in '@#$%&*' for c in p) and ' ' not in p and 8 <= len(p) <= 15:
    print("Secure Password")
else:
    print("Insecure Password")
