from customer import Customer


def main():
    # get customer 1 data
    print('Customer 1')
    email = input('Enter email address: ')
    customer1 = Customer(email)
    customer1.input_info()
    customer1.verify_info()
    customer1_output_string = customer1.output_info()
    print()
    # get customer 2 data
    print('Customer 2')
    email = input('Enter email address: ')
    customer2 = Customer(email)
    customer2.input_info()
    customer2.verify_info()
    customer2_output_string = customer2.output_info()
    print()
    # export data to text file
    customer_output_string = customer1_output_string + customer2_output_string
    output_file = open('customers.txt', 'w')
    output_file.write(customer_output_string)
    output_file.close()
    print("Data of two customers written to the file 'customers.txt'.")


main()
