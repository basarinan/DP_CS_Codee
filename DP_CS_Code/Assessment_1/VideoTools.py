import string
def longestWords(txt):
	#Initially I was planning on making a tool that did the same function but with a precondition that didn't allow punctuation
	
	txt = txt.translate(txt.maketrans('', '', string.punctuation))
	#This is an abstraction I used that I found off the internet
	#This method gets rid of the punctuations and allows us to worry about words only
	

	words = txt.split()
	#This is an instance function, it needs something inside to callit, however because I left it blank it looks like a statif function
	#This method splits the txt into just words and puts it in a list, it knows to do that because there is an empty string

	
	tupleslist = []
	#We create a list here so that we can create a list with a tuple

	for word in words:
		#we go through the list and append each word to tupleslist along with a new variable that has the length of the word
		wordlength = len(word)
		tupleslist.append((wordlength, word))

	tupleslist.sort(reverse = True)
	#Another abstraction used to sort lists, I don't know exactly how it runs but it does the job
	#We sort the list from biggest to smallest

	result = []
	#This list is not necessary but I chose to make a list named result just to clarify each list's functions

	for i in tupleslist:
		#we loop through this list and add the elements into the result list which we end up returning
		
		result.append(i)


	return result
#rint(longestWords("I am the fastest person here"))
#rint(longestWords("Flash: is here, don't worry"))

def StringChangeXY(string):
	#This function is designed to take a string and replace all xs inside with a y instead, after having done that it will replace the first and last letter in the word 

	

	
	
	for i in range(len(string)):
		#I have to loop through the string and essentially every letter

		
		if string[i] == "x":
			#Once that has been done I search for any letters that are x
			string = string.replace(string[i],"y")

			#If that is the case, I will instruct it to replace it with a "y", with the string.replace function
	
	front = string[0]
	#Here I am identifying the first letter of the list
	back = string[len(string)-1]
	#Here I am identifying the last letter of the list

	return back + string[1:len(string)-1] +front
	# Here I return the last letter, everything in between and the front#


	




	
print(StringChangeXY("thfyxui"))
print(StringChangeXY("xxxyzy"))
