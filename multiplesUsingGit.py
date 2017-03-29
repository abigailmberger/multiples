number = input("Choose a number: ")

validNumber = False

while validNumber == False: 

	try :
		number = int(number)
		validNumber = True
	
	except :
		number = input("That's not a number. Try again: ")

index = 0
output = ""

while index < 10:
	index += 1
	multiple = number * index
	output += ("{} * {} = {}\n".format(number, index, multiple))

print(output)