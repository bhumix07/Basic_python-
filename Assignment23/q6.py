'''6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9'''
    

for i in range(1,6):

    for j in range(5,i,-1):
        print("-", end=" ")

    k = i

    for l in range(1,i+1):
        print(k, end=" ")
        k += 1

    print()