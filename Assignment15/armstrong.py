n = int(input("n : "))
size = len(str(n))
sum = 0
temp = n
for i in range(size):
    rem = temp % 10
    sum = sum + rem ** size
    temp = temp // 10
if sum == n:
    print("The number is an Armstrong number.")
else:    print("The number is not an Armstrong number.")