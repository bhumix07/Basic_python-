'''30) Extended Slanted Star Block
    ****
     ****
      ****
       ****
        ****'''
        
for i in range(1,6):        
    for j in range(1,9): 
        if i==j or j-i==1 or j-i==2 or j-i==3: 
            print("*",end=" ")
        else:      
            print(" ",end=" ")
    print()