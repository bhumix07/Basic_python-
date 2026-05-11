#student details
name = input("Enter your name: ")
rollno = int(input("Enter your roll number: "))
branch = input("Enter your branch: ")
sub = input("Enter your subject: ")
# Question data
CorrectAnswer  = 1
WrongAnswer    = 0
PassMarks      = 4
TotalQuestions = 10

c=0
w=0
print("Q1. Which symbol is used for comments in Python?")
print("A. //        B. #       C. /*          D. <!--")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print()
print("Q2. What is the output of the following code: print(2 + 3 * 4)?")
print("A. 20         B. 14      C. 24          D. 10")
n = input("your ans : ").lower()
if n == "c":
    c +=1
else: 
    w +=1   
print()
print("Q3. Which of the following is a valid variable name in Python?")
print("A. 1variable   B. variable1   C. variable-1   D. variable 1")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print()     
print("Q4. What is the output of the following code: print(len('Hello World'))?")
print("A. 10         B. 11      C. 12          D. 13")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print() 
print("Q5. Which condition checks both statements are True?")
print("A. or        B. not     C. and       D. xor")
n = input("your ans : ").lower()
if n == "c":
    c +=1
else: 
    w +=1   
print()
print("Q6. What is the output of the following code: print(5 // 2)?")
print("A. 2.5        B. 2       C. 3           D. 2.0")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print()
print("Q7. Which of the following is used to stop the loops in Python?")
print("A. continue     B. break     C. pass         D. stop")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print()
print("Q8. What is the output of the following code: print(10 % 3)?")
print("A. 1          B. 2       C. 3           D.   0")
n = input("your ans : ").lower()
if n == "d":
    c +=1
else: 
    w +=1   
print() 
print("Q9. What will be the output? 2∗∗3")
print("A. 6          B. 8       C. 9           D. 12")
n = input("your ans : ").lower()
if n == "b":
    c +=1
else: 
    w +=1   
print()
print("Q10. Which of the following is used to skip the loops in  Python?")
print("A. continue     B. break     C. pass         D. skip")
n = input("your ans : ").lower()
if n == "a":
    c +=1
else: 
    w +=1   
print()

# Answer key
print("Correct Answers: ", c)
print("Wrong Answers: ", w)


print("===========================RESULT===============================")
print("Name           : ", name)
print("Roll No        : ", rollno) 
print("Branch         : ", branch)
print("Subject        : ", sub)

print("Total Questions: ", TotalQuestions)
print("Correct Answers: ", c)
print("Wrong Answers  : ", w)
print("persentage     : ", (c/TotalQuestions)*100, "%")
print("Result         : ", "Pass" if c >= PassMarks else "Fail")
x = "A" if c >= PassMarks else "B" 
print("Grade          : ", x)

print()
if c >= PassMarks:
    print("Congratulations! You passed the quiz.")  
else:
    print("Sorry, you did not pass the quiz. Better luck next time!")   