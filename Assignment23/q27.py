'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''


k = 1

for i in range(1,5):

    for j in range(1,8):

        if j >= 5-i and j <= i+3 and (i+j)%2==1:
            print(k, end=" ")
            k += 1

        else:
            print(" ", end=" ")

    print()