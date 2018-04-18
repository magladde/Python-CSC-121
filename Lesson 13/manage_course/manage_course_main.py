from course import Course


def main():
    course_code = input('Enter course code: ')
    quota = int(input('Enter course quota: '))
    course1 = Course(course_code, quota)

    oper = 1
    while oper != 0:
        oper = int(input('Enter 1 for add student, 2 for drop student, '
                     '3 for course info, 0 for exit: '))
        if oper == 1:
            course1.add_student()
            print('Enrollment:', course1.enrollment)
            print()
        elif oper == 2:
            course1.drop_student()
            print('Enrollment:', course1.enrollment)
            print()
        elif oper == 3:
            print('Course code:', course1.course_code)
            print('Quota:', course1.quota)
            print('Enrollment:', course1.enrollment)
            print()


main()
