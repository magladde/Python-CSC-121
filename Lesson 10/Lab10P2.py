# Lesson 10 lab problem 2
def main():
    input_file = open('water.txt', 'r')
    user_input = []
    for line in input_file:
        info = line.split(' ')
        info[0] = info[0].strip()
        info[1] = info[1].strip()
        info[2] = info[2].strip()
        info[2] = int(info[2])
        user_input.append(info)

    for customer in user_input:
        if customer[1] == 'R':
            if int(customer[2]) <= 6000:
                print('Account number: ' + customer[0] + ' Water charge: ' + str((customer[2] * .005)))
            else:
                print('Account number: ' + customer[0] + ' Water charge: ' + str((30 + (customer[2] - 6000) * .007)))
        else:
            if int(customer[2]) <= 8000:
                print('Account number: ' + customer[0] + ' Water charge: ' + str((customer[2] * .006)))
            else:
                print('Account number: ' + customer [0] + 'Water charge: ' + str((48 + (customer[2] - 8000) * .008)))

    input_file.close()

main()