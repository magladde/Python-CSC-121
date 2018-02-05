# Fasting glucose program

# program introduction
print('This program performs diabetes diagnosis for multiple patients')
print('based off of fasting plasma glucose levels (FPG).')
print()
print('If FPG is higher than 125, the patient has diabetes. If FPG is ')
print('Higher than 100 but not higher than 125, the patient has')
print('pre-diabetes. If FPG is 100 or lower the patient is considered ')
print('to have a healthy FPG.')
print()

# diagnosis loop
repeat = 'y'
while repeat == 'y':
	diagnosis = 'healthy fpg level'
	fpg = int(input('Enter fasting plasma glucose level: '))
	if fpg > 125:
		diagnosis = 'diabetes'
	elif fpg > 100 and fpg <= 125:
		diagnosis = 'pre-diabetes'
	print('This patient has ' + diagnosis + '.')
	repeat = input('Checking diabetes for another patient? [y/n] ')
	print()
