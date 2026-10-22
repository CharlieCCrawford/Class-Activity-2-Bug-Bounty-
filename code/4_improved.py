"""Look up a student's grade and display the class average."""

GRADES = {'Alice': 85, 'Bob': 72, 'Carol': 91}


def find_student(name, grades):
    """Return the stored name matching name, ignoring case and spaces."""
    target = name.strip().casefold()
    for student in grades:
        if student.casefold() == target:
            return student
    return None


def main():
    """Ask for a student's name, then show their grade and the average."""
    student_name = input('Enter student name: ').strip()

    if not student_name:
        print('No name entered')
    else:
        match = find_student(student_name, GRADES)
        if match is not None:
            print(match, 'scored', GRADES[match])
        else:
            print('Student not found')

    if GRADES:
        class_average = sum(GRADES.values()) / len(GRADES)
        print(f'Class average: {class_average:.2f}')
    else:
        print('No grades recorded')


if __name__ == '__main__':
    main()
