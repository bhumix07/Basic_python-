'''23) Plus Star Pattern
          *
          *
    *********
          *
          *'''
          
for i in range(1,6):
    for j in range(1,10):
        if i==3 or j==7:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            