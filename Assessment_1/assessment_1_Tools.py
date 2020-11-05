def Tool1(lst1,lst2):
# Combine two lists into a third list, the values of the third list should be a combination of the two in the corresponding values of the initial lists

	lst3 = list()
	#create empty list
	result = list()
	#create empty list
	count = 0
	#create a count variable, this will be used later on in order to loop the bigger list in order to add the variables that don't exist in the shorter list into the third list

	if len(lst1) >= len(lst2):
		#determine which list is bigger, if lst 1 is bigger it will go into this loop, otherwise, it will go to the other body of code which accounts for list 2 is being biggerr
		for i in range(len(lst2)):
			#loop through both lists, but make sure to loop to the length of the smaller list in order to avoid out of index errors.

			count = count + 1


			lst3.append(lst1[i])

			lst3.append(lst2[i])
			lst3[:] = ["".join(lst3[:])]
			#Once the two values have been added into lst3, make sure to combine them by using this method

			result.append(lst3)
			lst3 = []
			#append lst3 to result, so that after one combination has been achieved, the list is reset and able to carry out the same function for the second combination
		for i in range(count,len(lst1),1):
			#Once we have the combinations, we have to loop through the elements of the list that weren't incorporated because they were not included in the lst2 index, and add them to the result list. This is because lst 1 is bigger 
			result.append(lst1[i])
		
		
			#This bit of code goes through the same process but in the case that lst 2 is bigger
	if len(lst1) < len(lst2):
		for i in range(len(lst1)):
			count = count +1
			lst3.append(lst2[i])
			
			lst3.append(lst1[i])
			lst3[:] = ["".join(lst3[:])]
			result.append(lst3)
			lst3 = []
		for i in range(count,len(lst2),1):
			result.append(lst2[i])


	return result


	
	
	

	
	


#print(Tool1(["dog","cat","turtle"],["fire"]))
#print(Tool1(["dog","cat","turtle"],["ice","fire"]))
#print(Tool1(["sedat","tulay"],["inan","yilmaz"]))
#print(Tool1(["dog"],["cat","turtle"]))


# This second tool is used for finding the numbers in even positions in the list and creating a single string by combining them. Then we will loop through the string in order to find the sum of these numbers. Although, it can be done simpler, we will make sure to create one string as to try to practice our combining skills.

def Tool2(lst):
	lst1 = list()
	
	#create an open list as well as a sums variable that we will use
	sums = 0
	for i in range(len(lst)):
		# loop through the lst
		if (i + 1) % 2 == 0:
			#this is used to define the variables in even position and add to the lst1
			lst1.append(lst[i])

		lst1[:] = ["".join(lst1[:])]
		# Then we will combine the different values in the list in order to 
		
	for i in range(len(lst1)):
		#loop through the word and create a variable for lst1[i] so it is easier to write while looping through it 
		x = lst1[i]
		for j in range(len(x)):
			#Once looping through the string, we will add each number to sums, it is important to change the value to an integer
			sums = sums + int(x[j])


	return sums
print(Tool2(["1","4","5","7","6","8"]))





def Tool3(d):
	#This program will take a list of students and their graduation years, For the graduates who graduated after 2010 it will  organize them by the order of graduation
	#We will incorporate tuples in order to acount for both the name and the graduation year.


	

	
	listt = []
	
	
	#we create two diff lists which will use later
	for key, value in d.items():
		#Make if statement to check whether they graduated after 2010
		if value > 2010:
		# we go into the dictionary with the tuples and append both the value and the key into listt. The value is the graduation year and the key is the name.
		#You have to add the value first so that when we ask it to reverse sort it will be able to.
			listt.append((value, key))
	
		
	
	return listt.sort(reverse=True)




	#Once appended, we will sort them from latest to earliest graduation dates by using the reverse = True method
	#This will help us get the latest graduation years first as they are bigger than the latter.
	
	#I thought that this was a good application of dictionary as it was not too complicated but introduced an idea that was improving my learning via the tuples.
#print(Tool3({'Lorenzo':2004, 'Tina':2023, 'Bene':2011, 'Tara':2022, 'Robert': 1993, 'Mitchell': 1987}))




	
	
	













