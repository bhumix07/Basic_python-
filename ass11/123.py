n  = int(input("enter no. : "))

t = len(str(n))
sum = 0

while n > 0:
    a = n % 10
    sum = sum + a**t
    n = n//10
    
   

if sum == n :
    print("arm")
else:
    print("not..arm") 
print(sum)