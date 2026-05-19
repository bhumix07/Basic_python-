'''4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''

s = input(" Enter student name:")
c=0
for ch in s:
    if ch >= "a" and ch <= "z" or ch >= "A" and ch <= "Z":
        if ch not in "AEIOUaeiou":
            c+=1
            print(ch)
print(" Total consonants:",c)            