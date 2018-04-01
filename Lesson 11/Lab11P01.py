# Lab 11 Problem 1
def main():
    # get user input
    user_input = input('Enter a string: ')
    dictionary = get_dictionary(user_input)
    print(dictionary)

    # take user input and check if in dictionary
    user_char = input('Choose a letter: ')
    dictionary = char_count(user_char, dictionary)
    print('Dictionary after that letter removed:', dictionary)

    # create a list that stores the letters in dictionary and srot and display list
    letters = dictionary.keys()
    sorted_characters = sorted(letters)
    print('Letters sorted:', sorted_characters)


# convert user input into a dictionary containing the count of each character
def get_dictionary(user_input):
    user_input = user_input.upper()

    # generate list of letters, non overlapping
    string_length = len(user_input)
    characters = []
    for i in range(string_length):
        if user_input[i].isalpha():
            if user_input[i] not in characters:
                characters.append(user_input[i])

    # count the occurance of characters in list characters
    char_count = []
    for i in range(len(characters)):
        char_count.append(user_input.count(characters[i]))

    # combine two lists, convert to dictionary
    combined = list(zip(characters, char_count))

    dictionary = dict(combined)
    return(dictionary)

# checks to see if character is in dictionary and displays frequency, removes character from dictionary
def char_count(x, dictionary):
    x = x.upper()
    if x in dictionary:
        print('Frequency count of that letter: ', dictionary[x])
        del dictionary[x]
    else:
        print('Letter not in dictionary.')
    return(dictionary)

main()