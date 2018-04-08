import circle       # import circle module
import rectangle    # import rectangle module

def main():

    """ Calculates the area and perimeter of rectangle or circle """

    print('This program calculates area and perimeter of a rectangle or circle.')
    choice = int(input('Enter 1 for rectangle or 2 for circle: '))

    if choice == 1:
        length = float(input('Enter length of rectangle: '))
        width = float(input('Enter width of rectangle: '))
        rect_area = rectangle.area(length, width)
        rect_perimeter = rectangle.perimeter(length, width)
        print('Area:', rect_area, 'Perimeter:', rect_perimeter)

    elif choice == 2:
        print('Value of PI in circulations:', circle.PI)
        radius = float(input('Enter radius of circle: '))
        circle_area = circle.area(radius)
        circle_perimeter = circle.circumference(radius)
        print('Area:', circle_area, 'Perimeter:', circle_perimeter)
    else:
        print('Invalid choice')

main()