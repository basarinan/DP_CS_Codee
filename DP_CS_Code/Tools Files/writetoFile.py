def writeListtoFile(name,a,state):

	file = open(name,state)

	for i in range(len(a)):
		file.write(a[i]+"\n")


	file.close()


strings =["dad","mom","cat","tree"]

writeListtoFile("test.txt",strings)



