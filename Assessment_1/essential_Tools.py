
def base2to10(str):

	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):
		total = total + int(str[i]) * 2**n
		n = n + 1

	return total
#print(base2to10("01101101"))
#print(base2to10("11000111"))




def base10ToBase2(n):
	#Create empty string where you will convert base 10 into
	result = ""



	while n > 0:
	#Continues to loop until n is down to 0

		result = str(n % 2) + result
	#Divides n by mod 2 in order to add 0 or 1 as necessary for binary and turns value into a string

	#N is integer divided in order to go onto the next binary digit. 

		n = n//2

	return result

#print(base10ToBase2(53))
#print(base10ToBase2(62))
#print(base10ToBase2(45))


def hexToBase2_B(s):
	#Create Empty string to put Base 2 number into
	result = ""

	# Create a dictionary with the binary correspondent of each hexadecimal value


	DIC = { "0":"0000",
			"1":"0001",
			"2":"0010",
			"3":"0011",
			"4":"0100",
			"5":"0101",
			"6":"0110",
			"7":"0111",
			"8":"1000",
			"9":"1001",
			"A":"1010",
			"B":"1011",
			"C":"1100",
			"D":"1101",
			"E":"1110",
			"F":"1111"}

	#Loop through hexadecimal string

	
	for i in range(0, len(s), 1):
		#Add corresponding base 2 value to result
		result = result + DIC[s[i]]

	return result


#print(hexToBase2_B("0"))
#print(hexToBase2_B("A12"))
#print(hexToBase2_B("F"))


def base2toHex(s):
	#Create empty string
	

	result = ""

	#Create Dictionary of corresponding Hexadecimal values to binary values

	DIC = { "0000":"0",
			"0001":"1",
			"0010":"2",
			"0011":"3",
			"0100":"4",
			"0101":"5",
			"0110":"6",
			"0111":"7",
			"1000":"8",
			"1001":"9",
			"1010":"A",
			"1011":"B",
			"1100":"C",
			"1101":"D",
			"1110":"E",
			"1111":"F"}

	while (len(s)%4 != 0):
		s = "0" + s
		#Since binaries are read in groups of 4, make sure that if the last group is not a group of 4, to add 0s until it becomes one. To check for this we can use the mod division. If the return value is 0, that means it is divisible, else it is not.
	


	for i in range(0, len(s),4):
		#Loop in  increments of 4 in order to deal with each group individually
		v = s[i: i + 4]
		# In order to get all the values proceeding i, add 4 as to get the whole group 
		result = result + DIC[v]
		#Find the corresponding hexadecimal value and add to the empty string result.

	return result

BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
#Simple Test Case
for i in range (0, len(BIN),1):
	print(base2ToHexB(BIN[i]))

#print(base2ToHexB("1011110101")) #2 F 5
#print(base2ToHexB("1110111110110")) #1 D F 6



def sumdigits(a):
	#Castin is the process of changing type
	total = 0
	a = str(a)

	#Fundemental skill: Looping through strings

	#Count, check, change

	for i in range(0, len(a),1):
		#loop through sstring
		total = total + int(a[i])
	return total
	

#print(sumdigits(1234))




def findModSum1(lst):
	sums = 0
	#create a sums variable that you will add the integers to later
	#loop through list
	for i in range(len(lst)):
		if lst[i] % 3 ==0:
			#use od division to make sure it is a multiple of 3
			sums = sums + lst[i]
			#add to sums
	return sums
			 

samplelist = [1,2,3,4,5,6,7,8,9]
samplelist = [4,5,8,2,9,13,2]
#print(findModSum1(samplelist))

def findModSum2(lst,a,b):
	sums = 0
	#create sums variable that integers will be added to
	

	for i in range(len(lst)):
		#loop through list
		if lst[i] > a and lst[i] < b:
			#check whether the numbers in the list are between the two given,
			#if so, add it to sums
			
			sums = sums + lst[i]
	return sums
samplelist = [2,4,6,8,10,12]

#print(findModSum2(samplelist,3,9))

def findModSum3(lst,a,b):
	sums = 0
	#create sums variable where integers will be added 

	for i in range(len(lst)):
		#loop through list
		if lst[i] % a ==0 and lst[i] % b ==0:
			#make sure the numbers in the list are multiples of both a and b
			#if so, add them to sums
			sums = sums + lst[i]
	return sums
samplelist = (2,7,8,10,12,16,20)
#print(findModSum3(samplelist,2,4))

def findModSum4(lst):
	sums = 0
	#create sums variable where integers will be added
#Precondition: list cannot be empty
#loop through list
	for i in range(len(lst)):
		you = str(lst[i]).replace(".","")
		#for every value, remove decimals by replacing them with nothing 

		for j in range(len(you)):
			#loop through the string and add the integer value of it to sums
			sums = sums + int(you[j])
	return sums


samplelist = [12.3,2.56,3.236,6.4]

print(findModSum4(samplelist))

def reverseWordA(string):
	reversedstring = "".join(reversed(string))
	# This is actually a method I learned online that made my job extremely efficient
	return reversedstring

print(reverseWordA("body"))

def reverseWordB(a):
	lst = list()
	#create empty list
	for i in range(len(a)):
		#loop through list and use the reverse method
		
		reversedstring = "".join(reversed(a[i]))
		lst.append(reversedstring)
		#Add the reversed string to the empty list, lst

	lst[:] = ["".join(lst[:])]
	#use joining method in order to join the two words, since they have already been reversed, the newly combined word will be a combination of them
	return lst[0]
	#return the first value as they have all been joined within the list into a single element
		
print(reverseWordB(["turtle","leopard"]))

	

