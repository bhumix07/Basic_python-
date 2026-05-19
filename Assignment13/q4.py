'''
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31

'''
n = int(input("no. : "))

for i in range(2,n//2+1):
    if n%i==0:
        # print("not prime",n)
        
        for pre in range(n-1,1,-1):
            for i in range(2,pre):
                if pre%i==0:
                    # print("not prime",pre)
                    break
            else:
                print("prime no.",pre)
                break
        break        
    
else:
    # print("prime no.")
    
    for nxt in range(n+1,n*2):
        for i in range(2,nxt):
            if nxt%i==0:
                # print("not prime",nxt)/
                break
        else:
            print("prime",nxt)
            
