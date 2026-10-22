grades = {'Alice': 85, 'Bob': 72, 'Carol': 91}
name = input('Enter student name: ')

# FIX 1: Added a colon at the end of the if statement.
# Python needs a ':' to mark where the if block starts; leaving it out is a SyntaxError.
if name in grades:
    print(name, 'scored', grades[name])

# FIX 2: Added a colon after else.
# Like if, else must end with ':' or Python raises a SyntaxError.
else:
    print('Student not found')

# FIX 3: Changed sum(grades) to sum(grades.values()).
# sum(grades) goes through the dictionary's KEYS (the names 'Alice', 'Bob', 'Carol'),
# and Python can't add strings to numbers, so it crashed with a TypeError.
# .values() gives the scores (85, 72, 91), so the average is worked out correctly.
# len(grades) needed no change because it already returns the number of students (3).
print('Class average:', sum(grades.values()) / len(grades))
