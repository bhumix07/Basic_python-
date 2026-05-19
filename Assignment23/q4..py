'''4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
'''
for i in range(1,8):
    for j in range(1,8):
        if i+j==5   or i+j==11 or i-j==3 or j-i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()          