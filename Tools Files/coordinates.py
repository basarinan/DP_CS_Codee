def coordinates(text):

	fhand = open(text)
	lst = list()
	


	for line in fhand:
		lst.append(line)
	for i in range(len(lst)):
		if float(lst[i]) > 315 or float(lst[i]) < 45:
			print("North")
		elif float(lst[i]) > 45 and float(lst[i]) < 135:
			print("East")
		elif float(lst[i]) > 135 and float(lst[i]) < 225:
			print("South")
		elif float(lst[i]) > 225 and float(lst[i]) < 315:
			print("West")

coordinates("coordinates.txt")









