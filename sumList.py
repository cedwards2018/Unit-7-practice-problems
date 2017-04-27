def sumList(list):
	""" Returns the sum of a list recursively """
	if len(list) == 0: # Base case
		return 0
	
	return (list[0]) + sumList(list[1:]) # Recursive call