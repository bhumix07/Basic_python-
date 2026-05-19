'''23
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
'''


for i in range(1,6):
    for j in range(1,10):
        if i==5 or i+j==6 or j-i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            