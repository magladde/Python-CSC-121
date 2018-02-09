# Home Loan Amortization program

# program introduction
print('This program calculates the monthly mortgage payments for a')
print('given loan amount, term, and range of interest rates from')
print('3% to 18%.')
print()

# get userinput for loan_amount and term
loan_amount = int(input('Enter loan amount: '))
term_length = int(input('Enter length of the loan: '))

print('Loan amount: $' + str(loan_amount), end = '     ')
print('Term: ' + str(term_length), 'years')
print()
print('Interest Rate', end = '          ')
print('Monthly Payment')
