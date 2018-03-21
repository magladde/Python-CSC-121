def main():
    """ Store three departments in a text file"""

    output_file = open('departments.txt', 'a')
    output_file.write('Psychology' + '\n')
    output_file.write('History' + '\n')
    output_file.write('Sociology' + '\n')
    output_file.close()

main()