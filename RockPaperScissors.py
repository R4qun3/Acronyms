import random

choices = ["Rock", "Paper", "Scissors"]
opponent = random.choice(choices)
player = False
cpu_score = 0
player_score = 0

while True:
	player = input("Rock, Paper or Scissors?:\n").capitalize()
	# Here we will outline the conditions
	if player == opponent:
		print("Tie!")
	elif player == "Rock":
		if opponent == "Paper":
			print("You lose!", opponent, "covers", player)
			cpu_score += 1
		else:
			print("You win!", player, "smashes", opponent)
			player_score += 1
	elif player == "Paper":
		if opponent == "Scissors":
			print("You lose!", opponent, "cuts", player)
			cpu_score += 1
		else:
			print("You win!", player, "covers", opponent)
			player_score += 1
	elif player == "Scissors":
		if opponent == "Rock":
			print("You lose...", opponent, "smashes", player)
			cpu_score+=1
		else:
			print("You win!", player, "cut", opponent)
			player_score+=1
	elif player=='End':
		print("Final Scores:")
		print(f"CPU:{cpu_score}")
		print(f"Plaer:{player_score}")
		break