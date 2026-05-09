
'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600
'''

srly = int(input("Enter salary:"))
rat = int(input("Enter Rating(1-5):"))

if rat >4:
    if srly<20000:
        rs= srly + (srly*0.25) +2000
        print("Revised Salary: ₹",rs)
    else:
        rs= srly + (srly*0.25)
        print("Revised Salary: ₹",rs)
elif rat<5 and rat>3:
     if srly<20000:
        rs= srly + (srly*0.20) +2000
        print("Revised Salary: ₹",rs)
     else:
        rs= srly + (srly*0.20)
        print("Revised Salary: ₹",rs)
elif rat>2 and rat<4:
    rs= srly + (srly*0.10)
    print("Revised Salary: ₹",rs)

elif rat>1 and rat<3:
    rs= srly + (srly*0.05)
    print("Revised Salary: ₹",rs)
else:
    print("No hike")
    print("Revised Salary: ₹",srly)

