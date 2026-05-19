'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
    '''

for i in range(5):

    for j in range(i):
        print(2*i-j, end=" ")

        

    for l in range(4-i):
        print("-", end=" ")

    print()