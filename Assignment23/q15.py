'''15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *'''
    
    
    
for i in range(1,4):
    for j in range(1,6):
        if i==j or i+j==4 or j-i==4 or j-i==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")   
    print() 
    