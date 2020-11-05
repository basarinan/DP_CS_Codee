def lists(lst1,lst2):
	n = 0
	i = 0
	lst3 = list()
	while 0 <= n < len(lst1)and 0 <= i <len(lst2):
		
		if lst1[n] == lst2[i]:
			


			lst3.append(lst1[n])
			i = 0
			n = n+1

			
		else:
			i = i+1
		if len(lst2) - i == 1:
			n = n+1
			i = 0
	return lst3


print(lists([1,2,3,4,5,],[2,4,6,8,10]))