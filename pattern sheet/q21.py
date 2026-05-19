'''21.
1
22
3 3
4  4
55555
'''


for i in range(1,6):
    for j in range(1,i+1):
        if j==1:
            print(i,end="")
        elif i==5:
            print(i,end="")
        elif j==i:
            print(i,end="")
        else:
            print(" ",end="")
    print()