'''7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime'''



n=int(input("enter no."))
sum =0
for i in str(n):
    if int(i)%2 !=0:
        sum = sum + int(i)
print(sum)
i=2
while i < sum:
    if sum%i==0:
        print("not prime")
        break
    i+=1
else:
    print("prime")