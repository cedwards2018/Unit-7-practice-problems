def fibonacci(n):
	""" Returns the nth fibonacci number"""
	if n == 0: # Base case
		return 1
	elif n == 1: # Second base case
		return 1
	return fibonacci(n-2) + fibonacci(n-1) # Recursive call