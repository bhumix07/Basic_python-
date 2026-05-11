"""
*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
"""


n = int(input(" all digit : "))

count1 = 0
count2 = 0
while n >0:
    rem = n % 10
    count1 +=1
    n  = n//10

    if rem % 2 == 0:
        count2 +=1 
if count1 == count2:
    print("All Even")
else:
    print(" Not All Even")


