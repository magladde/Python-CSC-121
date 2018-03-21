def main():

    """ Find total of numbers stored in text file"""

    input_file = open('scores.txt', 'r')
    score_list = []
    for line in input_file:
        number = float(line)
        score_list.append(number)

    total = 0
    for score in score_list:
        print(score)
        total = total + score

    input_file.close()
    print('Total:', total)

main()