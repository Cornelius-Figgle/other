import sys

finish = True
while finish:
	kg = float(input('Enter kg: '))
	total = kg * 2.2
	print(f'The converted kg is: {total}lbs')
	question = input('Do you want to quit?')
	if 'y' in question.lower(): #converts str to lowercase to compare whether it contains the str 'y'
		#finish = False #not needed here unless you need to access it later in the script
		print('Bye-Bye!')
		break #exit the while loop
	else:
		print('OK!')
		continue #restart loop, not actually needed as will continue to next iteration naturally, but can improve readability

print('Exiting Program')
sys.exit(0) #program will end naturally here, so `sys.exit(0)` isn't really needed but it can improve readability
