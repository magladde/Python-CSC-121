# Lesson 10 lab problem 3
def main():
    user_input = input('Enter time [hh:mm:ss]: ')
    print(user_input)
    if user_input.count(':') != 2:
        print('Must separate hour, minute and second with colons')
        exit()
    userint_list = user_input.split(':')

    # determine if hour/minute/second is two digits and not a string
    if not userint_list[0].isnumeric():
        print('Hour must be a 2-digit number.')
        exit()
    if len(userint_list[0]) != 2:
        print('Hour must be a 2-digit number.')
        exit()
    if not userint_list[1].isnumeric():
        print('Minute must be a 2-digit number.')
        exit()
    if len(userint_list[1]) != 2:
        print('Minute must be a 2-digit number.')
        exit()
    if not userint_list[2].isnumeric():
        print('Second must be a 2-digit number.')
        exit()
    if len(userint_list[2]) != 2:
        print('Second must be a 2-digit number.')
        exit()

    # determine if hour/minute/second is the appropriate range of numbers
    hour = int(userint_list[0])
    if hour < 1 or hour > 24:
        print('Hour must be a 2-digit number between 0 and 23.')
        exit()
    minute = int(userint_list[1])
    if minute < 1 or minute > 59:
        print('Minute must be a 2-digit number between 0 and 59.')
        exit()
    second = int(userint_list[2])
    if second < 1 or second > 60:
        print('Second must be a 2-digit number between 0 and 59.')

    # if value entered is valid remove the colons and display the time
    time = userint_list[0] + userint_list[1] + userint_list[2]
    print('Time with colons removed:', time)

main()