import random

# maximum value
max_val = int(input("Enter highest value: "))

# allow the user to roll again
roll_again = "yes"

# loop
while roll_again == "yes" or roll_again == "y":
	print("Rolling the Dice...")

	print (random.randint(1, max_val))

	roll_again = input("Roll again? (y/n): ")