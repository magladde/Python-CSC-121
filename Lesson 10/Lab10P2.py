# Lesson 10 lab problem 2
def main():
    input_file = open('water.txt', 'r')
    for line in input_file:
        print(line)

    input_file.close()

main()