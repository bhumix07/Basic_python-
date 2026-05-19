n = int(input("Enter a number: "))
n1 = n
rev = 0
for i in range(n):
    if n != 0:   
        rev = rev*10 +  n%10 
        n //= 10    
        
if n1 == rev:
    print("The number is a palindrome.")
else:    print("The number is not a palindrome.")        