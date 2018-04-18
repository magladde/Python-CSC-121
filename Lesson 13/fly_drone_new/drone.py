class Drone:

    def __init__(self):

        """ constructor creates two instance variables for speed and height """

        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):

        """ increases the speed of the drone """

        self.__speed = self.__speed + 10



    def decelerate(self):

        """ decreases the speed of the drone, new speed cannot be negative """

        if self.__speed - 10 < 0:
            print('Error speed cannot be negative.')
        else:
            self.__speed = self.__speed - 10


    def ascend(self):

        """ increases the height of the drone """

        self.__height = self.__height + 10


    def descend(self):

        """ decreases the height of the drone"""

        if self.__height - 10 < 0:
            print('Error height cannot be negative.')
        else:
            self.__height = self.__height - 10


    def __str__(self):
        return 'Speed: ' + str(self.__speed) + ' Height: ' + str(self.__height)