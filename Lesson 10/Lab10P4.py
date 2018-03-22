# Lesson 10 lab problem 4

def main():
    # get user input, convert to uppercase
    user_input = input('Enter a string: ')
    user_input = user_input.upper()

    # generate list of letters, non overlapping
    number_characters = len(user_input)
    alphabet = []
    for i in range(number_characters):
        if user_input[i].isalpha():
            if user_input[i] not in alphabet:
                alphabet.append(user_input[i])

    # count the occurence of letters in alphabet in userinput
    letter_count = []
    num_letters_to_count = len(alphabet)
    for i in range(num_letters_to_count):
        letter_count.append(user_input.count(alphabet[i]))

    # combine two lists and display
    for i in range(len(alphabet)):
        print(str(alphabet[i]) + " " + str(letter_count[i]))
main()