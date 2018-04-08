def main():

    """ Displays calendar of the years chosen by the user """

    # initialization
    terminate = False

    # program greeting
    print('This program will display a calendar for a given year')

    # continue to display calendar years until -1 entered
    while not terminate:
        year = get_year()

        if year == -1:
            termiante = True
        else:
            # construct calendar
            calendar_year = constructCalYear(year)

    # display calendar
    displayCalendar(calendar_year)



def get_year():

    """ Returns a year between 1800 and 2099, inclusive, or the value -1 """

    year = int(input('Enter year (yyyy) (-1 to quit): '))
    while (year < 1800 or year > 2009) and year != -1:
        print('INVALID INPUT - Year must be between 1800 and 2099')
        year = int(input('Enter year (yyyy) (-1 to quit): '))

    return year


def leapYear(year):
    """ Returns True if year a leap year, otherwise returns False. """

    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        leap_year = True
    else:
        leap_year = False

    return leap_year


def dayOfWeekJan1(year, leap_year):
    """ Returns the day of the week for January 1 of a given year.

        year must be between 1800 and 2099. leap_year must be True if
        year a leap year, and False if otherwise. """

    century_digits = year // 100
    year_digits = year % 100
    value = year_digits + (year_digits // 4)

    if century_digits == 18:
        value = value + 2
    elif century_digits == 20:
        value = value + 6

    # adjust for leap years
    if not leap_year:
        value = value + 1

    # return first day of month for Jan 1
    return (value + 1) % 7


def numDaysInMonth (month_num, leap_year):

    """ Returns the number of days in a given month

        month_num in the range 1-12, inclusive.
        leap_year True if month in a leap year, otherwise False. """

    num_days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # special check for February in leap year
    if (month_num == 2) and leap_year:
        num_days = 29
    else:
        num_days = num_days_in_month[month_num - 1]

    return num_days


def constructCalMonth (month_num, first_day, num_days_in_month):

    """ Returns a formatted calendar month for display on the scree.

        month_num in the range 1-12 inclusive.
        first_day in the range 0-6 (1-Sun, 2-Mon, ..., 0-Sat)

        Returns a list of string values of the form,
        [month_name, week1, week2, week3, week 4, ...]"""

    # init
    empty_str = ''
    blank_col = format(' ', '3')
    blank_week = format(' ', '21')
    month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December')

    calendar_month = [' ' + format(month_names[month_num - 1], '<20')]
    current_day = 1
    current_col = 1
    calendar_week = ''

    # init starting column
    if first_day == 0:
        starting_col = 7
    else:
        starting_col = first_day

    # add any needed leading spaces for first week of month
    while current_col < starting_col:
        calendar_week = calendar_week + blank_col
        current_col = current_col + 1

    # construct month for proper number of days
    while current_day <= num_days_in_month:

        # store day of month in field of length 3
        calendar_week = calendar_week + format(str(current_day), '>3')

        # append new week to month if at end of week
        if current_col == 7:
            calendar_month = calendar_month + [calendar_week]
            calendar_week = empty_str
            current_col = 1
        else:
            current_col = current_col + 1

        current_day = current_day + 1

    # if there is a final week, append to constructed month
    if calendar_week!= empty_str:
        calendar_month = calendar_month + [calendar_week]

    return calendar_month


def constructCalYear(year):

    """ Returns a formatted calendar year for display on the screen.

        year in the range 1800 - 2099, inclusive
        Returns a list beginning with the year, followed by
        twelve constructed months

            [year, month1, month2, month3, ..., month 12] """

    # init
    leap_year = leapYear(year)
    first_day_of_month = dayOfWeekJan1(year, leap_year)
    calendar_year = [year]

    # construct calendar from twelve constructed months
    for month_num in range (1, 13):
        num_days_in_month = numDaysInMonth(month_num, leap_year)

        calendar_year.append(constructCalMonth(
                            month_num,
                            first_day_of_month,
                            num_days_in_month))

        first_day_of_month = (first_day_of_month + num_days_in_month) % 7

    return calendar_year


def displayCalendar(calendar_year):

    """ Displays a calendar_year on the screen three months across. """

    # init
    month_separator = format(' ', '8')
    blank_week = format(' ', '21')

    # display year
    print('\n', calendar_year[0])

    # display months three across
    for month_index in [1, 4, 7, 10]:

        # init
        week = 1
        lines_to_print = True

        while lines_to_print:

            # init
            lines_to_print = False

            # print weeks of months side-by-side
            for k in range(month_index, month_index + 3):
                if week <= len(calendar_year[k]):
                    week_dates = calendar_year[k] [week -1]
                    print(week_dates + blank_week[len(week_dates):], end = '')
                    lines_to_print = True
                else:
                    print(blank_week, end = '')
                print(month_separator, end = '')

            # move to next screen line
            print()

            # increment week
            week = week + 1


main()
