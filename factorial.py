def factorial(number):
	""" Returns the factorial of an integer """
	if number == 0: # Base Case
		return 1
	return number * factorial(number - 1) # Recursive call