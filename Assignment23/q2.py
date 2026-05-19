'''2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********'''
    
    
for i in range(1,6):
    for j in range(1,10):
        if i==1 or i==5 or j==1 or j==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
            
              
                