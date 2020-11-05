#isEven takes a single integer value a >= 0 and 
#returns true if it is even and false otherwise.

def isEven(a):
	

	if a % 2 == 0:
		return True
	
	return False

print(isEven(12))

#Test numbers ranging from 1-99
for i in (0,100,1):
	print(isEven(i))
