while True:
	user_input = input("Enter anything: ")
	if (user_input.lower() == "quit"):
		print("Program stopped")
		break
	try: 
		num = float(user_input)

		if (num >= 0):
			print("Positive")
		else:
			print("Negtive")
	except ValueError:
		print("invalid input")