'''26) Right Hollow Number Triangle
    1
    12
    1 3
    1  4
    12345'''
    
    
for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==j or i==5:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()  