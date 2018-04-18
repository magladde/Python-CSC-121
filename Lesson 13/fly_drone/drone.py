class Drone:

    def __init__(self):

        """ constructor creates two instance variables for speed and height """

        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):

        """ increases the speed of the drone """

        self.speed = self.speed + 10.0



    def decelerate(self):

        """ decreases the speed of the drone, new speed cannot be negative """

        if self.speed - 10 < 0:
            print('Error speed cannot be negative.')
        else:
            self.speed = self.speed - 10.0


    def ascend(self):

        """ increases the height of the drone """

        self.height = self.height + 10.0


    def descend(self):

        """ decreases the height of the drone"""

        if self.height - 10 < 0:
            print('Error height cannot be negative.')
        else:
            self.height = self.height - 10.0