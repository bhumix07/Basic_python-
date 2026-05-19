'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8'''



char = input("enter string  : ")
count=0
for i in str(char):
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
        
print("count of a is : ",count)
