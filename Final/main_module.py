from customer import Customer

def main():
    email = input('Enter email address: ')
    customer1 = Customer(email)
    customer1.input_info()
    customer1.verify_info()

    #email = input('Enter email address: ')
    #customer2 = Customer(email)
    #customer2.input_info()
    #customer2.verify_info()

main()