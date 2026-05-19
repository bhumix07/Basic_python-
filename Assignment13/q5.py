'''
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3

'''
n = int(input("no. : "))
c =0
for i in range(2,n//2+1):
    if n%i==0:
        # print("not prime",n)
        
        for nxt in range(n+1,n*2):
            c+=1
            for i in range(2,nxt):
                if nxt%i==0:
                    # print("not prime",nxt)/
                    break
            else:
                print("prime",nxt)
                break
        break        
    
else:
    # print("prime no.")
    
    for nxt in range(n+1,n*2):
        c+=1
        for i in range(2,nxt):
            if nxt%i==0:
                # print("not prime",nxt)/
                break
        else:
            print("prime",nxt)
print(c)     
