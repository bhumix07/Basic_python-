for i in range(1,6):
    for j in range(1,12):
        if i+j<=6 or j-i>=6 or  i==1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  