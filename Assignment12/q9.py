"""2.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number"""



n = int(input("enter the no."))
diff = 0
max = 0
m = str(n)
x = 0 
sum=0
newdiff = ""
for i in m:
    x+=1
    if diff == 0:
        diff = int(i)
    else:
        diff = diff - int(i)
        # print(abs(diff))
        sum += abs(int(diff))
        newdiff = newdiff+str(abs(diff))
        diff = int(i)
print("step diff",newdiff)
print("sum",sum)
newdiff=int(newdiff)
largest = 0 
while newdiff >0:
    digit = newdiff%10
    if digit>largest:
        largest = digit
    newdiff = newdiff//10
print("lagrest : ",largest)
length = len(str(n))
if n%x==0:
    print("Balance")
else:
    print("unbalance")
    