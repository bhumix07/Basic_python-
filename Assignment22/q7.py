

'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''
n = input("num plate : ")

if (len(n) == 10 and
    n[:2].isalpha() and
    n[2:4].isdigit() and
    n[4:6].isalpha() and
    n[6:].isdigit()):

    print("Valid Vehicle Number")

else:
    print("Invalid Vehicle Number")
