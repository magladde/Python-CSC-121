def main():

    """ Display strings read from text file"""

    input_file = open('instructors.txt', 'r')
    for line in input_file:
        print(line)
    input_file.close()

main()