def addStringsSmallLarge(str1,str2):

	if len(str1) > len(str2):
		print(str1+str2)
	if len(str1) == len(str2):
		print(str1, str2)
		
	if len(str1)< len(str2):
		print(str2+str1)


addStringsSmallLarge("word","words")
addStringsSmallLarge("money","money")
addStringsSmallLarge("tree","cat")
