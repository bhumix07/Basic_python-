'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''

id = input("enter the no. : ")
digit=0

if id[0:3]=="EMP" and len(id)==8:
    for i in id:
        if i>="0" and i<="9":
            digit=1
    
if digit==1:
    print(id,"its valid")
else:
    print("its not valid")
        