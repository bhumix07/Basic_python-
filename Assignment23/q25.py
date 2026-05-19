'''25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321'''
    
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()  

#
for i in range(5, 0, -1):
    
    for j in range(5 - i):
        print(" ", end=" ")
    
    for k in range(1, i + 1):
        print(k, end=" ")

    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    print()



for i in range(2, 6):
  
    for j in range(5 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")
   
    for l in range(i - 1, 0, -1):
        print(l, end=" ")
    print()
    

   
    
