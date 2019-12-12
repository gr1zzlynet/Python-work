prompt = "\nPlease enter your toppings for your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"I'm adding {topping.title()} to your pizza!")