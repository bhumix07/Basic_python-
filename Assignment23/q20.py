'''  
   1 
  2 3 
 4 5 6 
7 8 9 10 
 4 5 6 
  2 3 
   1 '''

num = 1


for i in range(1, 5):

    for j in range(4 - i):
        print(" ", end="")
    

    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


for i in range(3, 0, -1):

    for j in range(4 - i):
        print(" ", end="")
   
    if i == 3:
        num = 4
    elif i == 2:
        num = 2
    elif i == 1:
        num = 1
        
  
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()