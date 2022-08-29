#!/usr/bin/env python3

user_input = str(input("Please enter a phrase (only characters A-Z): "))

phrase = user_input.split()
result = " "

for i in phrase:
	result += str(i[0]).upper()

print (result)