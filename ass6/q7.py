"""
7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input. 
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000
"""

experience = int(input("experience year : "))
rating = int(input("rating : "))
salary = int(input("salary : "))



if experience >= 5:
    if rating >= 4:
        if salary <= 50000:
            a = salary*20/100
            bouns = a
            print("bonus : ",bouns)
        else:
            a = salary*10/100
            bouns = a
            print("bonus : ",bouns)
    else:
        a = salary*5/100
        bouns = a
        print("bonus : ",bouns)

else:
    print("no bonus is given")


