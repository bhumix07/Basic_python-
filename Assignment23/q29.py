'''29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
'''

for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print(i,end=" ")
        else:
            print("-",end=" ")
    print()            
            
    