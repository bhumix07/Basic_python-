'''
2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.
'''
m = int(input("enter the marks   "))
print("A+" if m >= 90 else "A" if m >= 75 else "B" if m >=60 else "c" if m>=50 else "Fail" )