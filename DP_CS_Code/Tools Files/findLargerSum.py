def findLargerSum(int1,int2,int3):
	sums = 0
	number = 2
	lst = list()
	lst2 = list()
	lst.append(int1)
	lst.append(int2)
	lst.append(int3)
	lst.sort(reverse = True)
	for i in range(len(lst)):
		lst2.append(lst[i])
		if len(lst2) is  number:
			for j in range(len(lst2)):
				sums = sums + lst2[j]



	return sums
		
print(findLargerSum(1,2,3))