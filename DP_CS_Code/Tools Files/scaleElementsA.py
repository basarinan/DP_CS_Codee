def scaleElementsA(a,b):
	for i in range(len(b)):
		b[i] = b[i] * a
	print(b)



scaleElementsA(2,[1,2,3,4])

def scaleElementsB(a,b):
	newlist= []
	for i in range(len(b)):
		num = b[i] * 2
		newlist.append(num)
	print(newlist)
	print(b)

scaleElementsB(2,[1,2,3,4])




