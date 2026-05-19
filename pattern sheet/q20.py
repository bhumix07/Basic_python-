'''20.
1
12
1 3
1  4
12345'''


for i in range(1,6):
    for j in range(1,i+1):
        if j==1:
            print("1",end="")
        elif i==5:
            print(j,end="")
        elif j==i:
            print(i,end="")
        else:
            print(" ",end="")
    print()