2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17



n = int(input("enter the no."))
n+=1
while True :
    flag = True 
    for i in range(2,n//2+1):
        if n%i==0:
            flag = False
            
    else:
        if flag == True:
           print(n)
           break
        else:
           n+=1
        