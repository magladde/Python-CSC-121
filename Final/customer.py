class Customer:

    def __init__(self, email):
        """ creates instance of Customer object """

        self.__last_name = ""
        self.__first_name = ""
        self.__age = 0
        self.__email = email
        self.__password = ""
        self.__card_number = ""
        self.__security_code = ""

    def Input_age(self):
        age_flag = True
        while age_flag == True:
            negative_flag = True
            numeric_flag = True
            age = input('Enter age: ')
            if age.isnumeric() == False:
                numeric_flag = False
                print('Age must be a number')
            if numeric_flag == True:
                if int(age) < 0:
                    negative_flag = False
                    print('Age cannot be negative.')
            if negative_flag == True and numeric_flag == True:
                age_flag = False
        self.__age = int(age)
        print()

    def Input_password(self):
        print('Your password must be 8-12 characters long containing at least '
              'one upper-case letter, one lower-case letter and one number.')

        password_flag = True

        while password_flag == True:
            password = input('Enter password: ')
            length_flag = True
            digit_flag = True
            alpha_flag = True
            lower_flag = True
            upper_flag = True
            if len(password) < 8:
                length_flag = False
                print('Your password must be at least 8 characters long.')
            if len(password) > 12:
                length_flag = False
                print('Your password must be no greater than 12 characters.')
            if password.isdigit() == True:
                digit_flag = False
                print('Your password must contain digits and letters.')
            if password.isalpha() == True:
                alpha_flag = False
                print('Your password must contain digits and letters.')
            if password.islower() == True:
                lower_flag = False
                print(
                    'Your password must contain upper-case and lower-case letters.')
            if password.isupper() == True:
                upper_flag = False
                print(
                    'Your password must contain upper-case and lower-case letters.')
            if length_flag == True and digit_flag == True and alpha_flag == True and \
                    lower_flag == True and upper_flag == True:
                password_flag = False
        self.__password = self.__password + password
        print('Valid password.')
        print()

    def input_card_number(self):
        card_flag = True

        while card_flag == True:
            num_flag = True
            len_flag = True
            card_num = input('Enter 16 digit credit card number: ')
            if card_num.isdigit() == False:
                print('Card number must only be numbers')
                num_flag = False
            if len(card_num) != 16:
                print('Card number must be 16 digits.')
                len_flag = False
            if num_flag == True and len_flag == True:
                card_flag = False
            self.__card_number = card_num
        print()

    def input_security_code(self):
        security_flag = True

        while security_flag == True:
            len_flag = True
            digit_flag = True
            security_code = input('Enter three digit security code: ')
            if len(security_code) != 3:
                print('PIN must be three digits long.')
                len_flag = False
            if security_code.isdigit() == False:
                print('PIN must be three digits.')
                digit_flag = False
            if len_flag == True and digit_flag == True:
                security_flag = False
        self.__security_code = security_code
        print()

    def input_info(self):
        first_name = input('Enter first name: ')
        self.__first_name = first_name
        last_name = input('Enter last name: ')
        self.__last_name = last_name
        self.Input_age()
        self.Input_password()
        self.input_card_number()
        self.input_security_code()

    def verify_info(self):
        change_var = 1
        while change_var != 0:
            print('1. First name:', self.__first_name)
            print('2. Last name:', self.__last_name)
            print('3. Email address:', self.__email)
            print('4. Password: ' + self.__password)
            print('5. Age: ' + str(self.__age))
            print('6. Card number: ' + str(self.__card_number))
            print('7. Security code: ' + str(self.__security_code))
            print()
            change_var = int(input("To correct any entry, enter the number "
                                   "and press RETURN. If everything is "
                                   "correct press 0:"))
            print()
            if change_var == 1:
                self.__first_name = input('Enter first name: ')
            if change_var == 2:
                self.__last_name = input('Enter last name: ')
            if change_var == 3:
                self.__email = input('Enter email address: ')
            if change_var == 4:
                self.Input_password()
            if change_var == 5:
                self.Input_age()
            if change_var == 6:
                self.input_card_number()
            if change_var == 7:
                self.input_security_code()
        print('Registration and verification completed for this customer.')

    def output_info(self):
       customer_info = ""
       customer_info = customer_info + self.__first_name + " "
       customer_info = customer_info + self.__last_name + " "
       customer_info = customer_info + str(self.__age) + " "
       customer_info = customer_info + self.__email + " "
       customer_info = customer_info + self.__password + " "
       customer_info = customer_info + self.__card_number + " "
       customer_info = customer_info + self.__security_code + "\n"
       return customer_info