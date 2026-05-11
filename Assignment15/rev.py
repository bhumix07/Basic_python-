n = int(input("n : "))
rev = 0
for i in range(n):
    if n != 0:   
        rev = rev*10 +  n%10 
        n //= 10
   
print(rev)