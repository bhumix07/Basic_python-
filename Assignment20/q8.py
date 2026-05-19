'''enter n6
 654321
  65432
   6543
    654
     65
'''


# n = int(input("enter no : "))
for i in range(1,6):
    
    for k in range(1,i):
        
        print(" ",end=" ")
    for j in range(6,i-1,-1):
        print(j,end=" ")
        
    print()    