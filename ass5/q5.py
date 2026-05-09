"""5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
"""

user = input("Enter User name ")
passward = input("Enter pass")

if user == "admin" :
    print("valid user")
    if len(passward) >= 8:
        print("strong pass")
else :
    print("invalid")


