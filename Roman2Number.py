dict = {
	# establish a dictionary 
	# list of all characters 
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

def romToDec(numeral):
	sum = 0
	for i in range(len(numeral) - 1):
		rom = numeral[i]
		num = numeral[i + 1]
		if dict[rom] < dict[num]:
			sum -= dict[rom]
		else:
			sum += dict[rom]

	sum += dict[numeral[-1]]
	return sum

to_change = input("Enter a Roman Numeral: ")

print(romToDec(to_change))