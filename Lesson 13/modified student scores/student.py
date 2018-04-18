class Student:

    def __init__(self, student_name):

        """ constructor of class Student """

        self.__name = student_name
        self.__project = 0.0
        self.__midterm = 0.0
        self.__final = 0.0


    def inputScores(self):

        """ input scores from user """

        self.__project = float(input('Enter project score: '))
        self.__midterm = float(input('Enter midterm score: '))
        self.__final = float(input('Enter final score: '))


    def calAvg(self):

        """return average of project, midterm, and final """

        avg = (self.__project + self.__midterm + self.__final) / 3
        return avg


    def getMidterm(self):
        return self.__midterm


    def getFinal(self):
        return self.__final

    def setFinal(self, final_score):
        self.__final = final_score