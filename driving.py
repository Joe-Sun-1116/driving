country = input('Where are you from? ')
age = input('Please enter your age. ')
if country == 'Taiwan':
	if int(age) >= 18:
		print('You can drive')
	else:
		print('You can\'t drive.')