'''
6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''


v =  input("any kind of data : ")
x = alpha if "a" <= v >= "z" else digit if 0 <= v >= 9 else 


print(x)

