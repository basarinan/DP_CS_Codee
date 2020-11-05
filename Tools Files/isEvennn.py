def isEvenn(n):
	even = True

	while(n>0) and (even ==True):
		if (n % 10) % 2 ==1:
			even = False
		n = n//10 #Integer division removes units digit

	return even
print(isEvenn(345))
print(isEvenn(246))