'''3)	WAP to find out all the leap years between two entered years'''
n = int(input("1st year : "))
m = int(input("2st year : "))

for i in range(n,m+1):
  if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
      print(i)


