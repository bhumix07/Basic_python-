'''5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
'''
for i in range(4,0,-1): 
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,(4-i)*2+1):
        print("*",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")
    print()            
    