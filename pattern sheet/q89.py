'''
    1
   101
  10101
 1010101
101010101'''



num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,2*i-1+1):
        if k%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()