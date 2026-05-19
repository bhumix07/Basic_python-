'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username'''

usr = input("enter username  : ")

case = 0
ltr=0
dgt=0
upr=0
if usr[0]>="a" and usr[0]<="z":

    if len(usr)>=5 and len(usr)<=12:

        for i in  range(len(usr)):
            if usr[i]<="z" and usr[i]>="a":
             
                ltr=1
            elif usr[i]<="9" and usr[i]>="0":
       
                dgt=1
            elif usr[i] == "_" :
       
                upr =1
            else:
          
                case =1
                break
                
                
if ltr==1 and dgt==1 and upr==1 and case==0:
    print("valid")
        
else:
    print("not valid")