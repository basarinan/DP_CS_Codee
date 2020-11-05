def readFiletoList(file):
	fhand = open(file,"r")
	contents = list()
	
	
	for line in fhand:
		
		split = line.split()
		for i in split:
			contents.append(i)

	
	print(contents)
readFiletoList("txt.txt")
		


