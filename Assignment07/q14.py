
'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

cc = input("Enter course category (Programming/Design/Marketing) : ")
ut = input("Enter user type (student/Working Professional/others):")

if cc=="programming":
    if ut=="student":
        cf = 5000-(5000*0.2) 
    elif ut=="working professional":
        cf = 5000-(5000*0.1)
    else:
        cf = 5000
elif cc=="design":
     if ut=="student":
        cf = 4000-(4000*0.2)
     elif ut=="working professional":
        cf = 4000-(4000*0.1)
     else:
        cf = 4000
else:
     if ut=="student":
        cf = 3000-(3000*0.2)
     elif ut=="working professional":
        cf = 3000-(3000*0.1)
     else:
        cf = 3000
     print(cf)

