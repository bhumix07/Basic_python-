'''87) Hollow Diamond Square
    ***********
    ****   ****
    ***     ***
    **       **
    *         *
    *         *
    **       **
    ***     ***
    ****   ****
    ***********'''
for i in range(1,11):
    for j in range(1,12):
        if i+j<=6 or j-i>=6 or i+j >=17 or i-j>=5 or i==1 or i==10:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
    