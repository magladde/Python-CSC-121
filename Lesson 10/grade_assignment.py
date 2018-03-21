def main():

    """ Assign letter grades to scores"""

    input_file = open('scores.txt', 'r')
    output_file = open('scores_grades.txt', 'w')

    for line in input_file:
        score = float(line)
        if 100 >= score >= 90:
            grade = 'A'
        elif 90 > score >= 80:
            grade = 'B'
        elif 80 > score >= 70:
            grade = 'C'
        elif 70 > score >= 60:
            grade = 'D'
        elif 60 > score >= 0:
            grade = 'F'
        output_string = str(score) + ' ' + grade + '\n'
        output_file.write(output_string)\

    input_file.close()
    output_file.close()

main()