def findReverseNumber(integer):
	integer = str(integer)
	reversedinteger = "".join(reversed(integer))
	return reversedinteger
print(findReverseNumber(32))