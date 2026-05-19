'''9.
    1
   10
  101
 1010
10101
'''
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        if k%2==0:
            print(0,end="")    
        else:
            print(1,end="")
    print()        
                
