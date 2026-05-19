n = int(input("n : "))

sum = 0
for i in range(n):
    if i!= 0:
        a = n%10
        
        if a % 2 == 0:
            sum += 1
        n = n//10    
print("Count of even digits:", sum)