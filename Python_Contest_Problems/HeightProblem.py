def convertmeters(h,u):
	allmeters = list()
	
	
	for i in range(len(u)):
		
		
		if u[i] == "m":
		
			h[i] = float(h[i])
			allmeters.append(h[i])
		elif u[i] == "dm":
			h[i] = float(h[i])/10
			


			allmeters.append(h[i])
		elif u[i] == "cm":
			h[i]= float(h[i])/100
			allmeters.append(h[i])
		elif u[i]== "mm":

			h[i] = float(h[i])/1000
			allmeters.append(h[i])
	return allmeters
convertmeters(height,metric)

file = open("Tallest.txt","r")
height = list()
names = list()
metric = list()

newlst = list()

for line in file:
	newlst = line.replace("\n"," ").split(" ")
	names.append(newlst[0])
	height.append(newlst[1])
	metric.append(newlst[2])











dictionary = dict()


for i in range(len(names)):
	

	dictionary[allmeters[i]] = (names[i])
	

for i in sorted (dictionary,reverse = True) : 
	print(dictionary[i])




















