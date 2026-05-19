'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''

p = input("Enter PNR: ")
if p[0:3]=="PNR" and len(p)==12 and p[3:].isdigit():
    print("Valid PNR Number")
else:
    print("Invalid PNR Number")
