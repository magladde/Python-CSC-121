# Lesson 10 lab problem 1

def main():
    data_file = open('water.txt', 'w')
    for i in range(4):
        account_num = input('Enter account number: ')
        data_file.write(account_num + ' ')
        cust_type = input('Enter R for residential, B for business: ')
        data_file.write(cust_type + ' ')
        num_gal = input('Enter number of gallons used: ')
        data_file.write(num_gal + '\n')

    data_file.close()

main()