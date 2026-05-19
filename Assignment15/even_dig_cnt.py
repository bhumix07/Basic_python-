char = input("enter string  : ")
count=0
for i in str(char):
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
        
print("count of a is : ",count)
