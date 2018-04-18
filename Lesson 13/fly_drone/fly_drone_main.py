from drone import Drone

def main():

    drone1 = Drone()

    oper = 1
    while oper != 0:
        oper = int(input('Enter 1 for accelerate, 2 for decelerate, '
                         '3 for ascend, 4 for descend, 0 for exit: '))
        if oper == 1:
            drone1.accelerate()
            print('Speed:', drone1.speed, 'Height:', drone1.height)
            print()
        elif oper == 2:
            drone1.decelerate()
            print('Speed:', drone1.speed, 'Height:', drone1.height)
            print()
        elif oper == 3:
            drone1.ascend()
            print('Speed:', drone1.speed, 'Height:', drone1.height)
            print()
        elif oper == 4:
            drone1.descend()
            print('Speed:', drone1.speed, 'Height:', drone1.height)
            print()

main()