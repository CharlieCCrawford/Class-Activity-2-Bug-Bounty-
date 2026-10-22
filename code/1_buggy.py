grades = {'Alice': 85, 'Bob': 72, 'Carol': 91}
name = input('Enter student name: ')
if name in grades
    print(name, 'scored', grades[name])
else
    print('Student not found')
print('Class average:', sum(grades) / len(grades))
