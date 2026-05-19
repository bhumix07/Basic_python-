'''6.
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
'''


n = int(input("enter the no."))
n+=1
while True :
    flag = True 
    for i in range(2,n//2+1):
        if n%i==0:
            flag = False
            
    else:
        if flag == True:
           print("next prime cabin",n)
           break
        else:
           n+=1
