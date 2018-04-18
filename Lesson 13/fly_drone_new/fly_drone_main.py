from drone import Drone

def main():

    drone1 = Drone()

    oper = 1
    while oper != 0:
        oper = int(input('Enter 1 for accelerate, 2 for decelerate, '
                         '3 for ascend, 4 for descend, 0 for exit: '))
        if oper == 1:
            drone1.accelerate()
            print(drone1)
            print()
        elif oper == 2:
            drone1.decelerate()
            print(drone1)
            print()
        elif oper == 3:
            drone1.ascend()
            print(drone1)
            print()
        elif oper == 4:
            drone1.descend()
            print(drone1)
            print()

main()