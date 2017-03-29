number = input("Choose a number: ")

validNumber = False

while validNumber == False: 

	try :
		number = int(number)
		validNumber = True
	
	except :
		number = input("That's not a number. Try again: ")

double = number*2

print("Double {} is {}.".format(number, double))