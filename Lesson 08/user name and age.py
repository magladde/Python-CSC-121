def main():
    user_name, user_age = get_name_and_age()
    print(user_name, 'is', user_age, 'years old.')

def get_name_and_age():
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    return name, age

main()