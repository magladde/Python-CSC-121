from Dinner_combo import Dinner_combo
from Delux_dinner_combo import Delux_dinner_combo


def main():
    dinner_combo = int(input('Enter 1 for dinner combo and 2 for delux dinner '
                             'combo: '))
    if dinner_combo == 1:
        dinnerCombo()
    elif dinner_combo == 2:
        deluxDinnerCombo()


def dinnerCombo():
    dinner1 = Dinner_combo()
    soup = int(input('Enter 1 for egg drop soup [$1.25] or 2 for wanton '
                          'soup [$1.50]: '))
    dinner1.choose_soup(soup)
    dish = int(input('Enter 1 for sweet and sour pork [$7], 2 for sesame '
                     'chicken [$8], or 3 for shrimp fried rice [$9]: '))
    dinner1.choose_dish(dish)
    dinner1.displayOrder()


def deluxDinnerCombo():
    dinner1 = Delux_dinner_combo()
    appetizer = int(input('Enter 1 for spring roll [$1.25] or 2 for chicken '
                          'wing [$1.50]: '))
    dinner1.choose_appetizer(appetizer)
    soup = int(input('Enter 1 for egg drop soup [$1.25] or 2 for wanton '
                          'soup [$1.50]: '))
    dinner1.choose_soup(soup)
    dish = int(input('Enter 1 for sweet and sour pork [$7], 2 for sesame '
                     'chicken [$8], or 3 for shrimp fried rice [$9]: '))
    dinner1.choose_dish(dish)
    dinner1.displayOrder()


main()