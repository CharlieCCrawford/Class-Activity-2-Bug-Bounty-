"""Look up a student's grade and display the class average."""

GRADES = {'Alice': 85, 'Bob': 72, 'Carol': 91}

student_name = input('Enter student name: ')

if student_name in GRADES:
    print(student_name, 'scored', GRADES[student_name])
else:
    print('Student not found')

class_average = sum(GRADES.values()) / len(GRADES)
print('Class average:', class_average)
