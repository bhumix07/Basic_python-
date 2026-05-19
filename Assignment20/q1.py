'''1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
'''

count = 0
for i in range(100,200+1):
    
    if i%9==0:
        count +=1
        
        
print(count)        
        