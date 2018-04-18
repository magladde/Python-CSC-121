from student import Student

def main():
    name = input('Enter student name: ')
    student1 = Student(name)
    student1.inputScores()
    average = student1.calcAvg()
    print('Average score of this student:', average)

    name = input('Enter student name: ')
    student2 = Student(name)
    student2.inputScores()
    average = student2.calcAvg()
    print('Average score fo this student:', average)

main()