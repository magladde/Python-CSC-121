class Course:

    def __init__(self, course_code, quota):

        """ constructor creates three instance variables for course code,
        quota, and enrollment """

        self.course_code = course_code
        self.quota = quota
        self.enrollment = 0

    def add_student(self):

        if self.enrollment > self.quota:
            print('Course already full.')
        else:
            print('One student added.')
            self.enrollment = self.enrollment + 1

    def drop_student(self):

        if self.enrollment < 1:
            print('Course is empty.')
        else:
            print('One student dropped.')
            self.enrollment = self.enrollment - 1