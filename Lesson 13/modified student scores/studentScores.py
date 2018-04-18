from student import Student


def main():
    name = input('Enter student name: ')
    student1 = Student(name)
    student1.inputScores()
    midterm = student1.getMidterm()
    final = student1.getFinal()
    if final - midterm > 10:
        print('Improvement target met. Five points added to the final exam '
              'score.')
        student1.setFinal(final + 5)
        print('New final exam score:', student1.getFinal())
    average = student1.calcAvg()
    print('Average score of this student:', average)

    print()
    name = input('Enter student name: ')
    student2 = Student(name)
    student2.inputScores()
    midterm = student2.getMidterm()
    final = student2.getFinal()
    if final - midterm > 10:
        print('Improvement target met. Five points added to the final exam '
              'score.')
        student2.setFinal(final + 5)
        print('New final exam score:', student2.getFinal())
    average = student2.calAvg()
    print('Average score of this student is:', average)

main()
