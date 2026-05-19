1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime
n = int(input("enter no."))
rev=""
sum=0
for i in str(n):
    rev=i+rev
    sum=sum+int(i)
print(rev)    
print(sum)
diff =abs(int(n)-int(rev))
final = sum+diff
print(diff)
print(final)


for i in range(2,final):
    if final%i==0:
        print("not prime") 
        break
else:
    print("prime")

