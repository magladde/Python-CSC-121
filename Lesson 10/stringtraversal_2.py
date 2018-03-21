def main():

    """ Read comma delimited text file"""

    input_file = open('department_locations.txt', 'r')
    dept_list = []
    for line in input_file:
        dept = line.split(',')
        print(dept)
        dept[0] = dept[0].strip()
        dept[1] = dept[1].strip()
        dept[2] = dept[2].strip()
        dept_list.append(dept)
        print(dept_list)

    for dept in dept_list:
        print('Department:', dept[0])
        print('Building:', dept[1])
        print('Mail box:', dept[2] )

    input_file.close()

main()