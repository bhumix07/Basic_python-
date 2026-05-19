'''4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected
'''






n = input("Enter number: ")

first_gap = abs(int(n[0]) - int(n[1]))
print("Initial Gap =", first_gap)

consistent = True

for i in range(1, len(n)-1):
    gap = abs(int(n[i]) - int(n[i+1]))
    
    if gap != first_gap:
        consistent = False
        break

if consistent:
    print("Consistent Pattern")
else:
    print("Pattern Break Detected")