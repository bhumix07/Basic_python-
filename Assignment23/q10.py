'''
10) Slanted Star Block
    ****
     ****
      ****
       ****'''

num = int(input("Enter Number: "))
i = 1
while i<=num:
    print()
    j = 1
    while j<i:
        print(" ",end="")
        j+=1
    j =1
    while j<=num:
        print("*",end="")
        j+=1
    i+=1