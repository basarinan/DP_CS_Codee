def question1(C):

	Total = 0

	for i in range(len(C)):
		if i % 2 == 0:
			Total = Total + C[i]
	return Total
#print(question1([1,2,3,4]))

def question2(C,n):
	Total = 0
	for i in range(len(C)):
		if C[i] > n:
			Total = Total +1
	return Total

#print(question2([1,4,5,3,7,9,10],5))

def question3(D):
	Total = 0
	x = 0
	for i in range(len(D)):
		if x == 1:
			Total = Total + float(D[i])
			x == -1
		else:
			x = x + 1
	return Total
Data = ["CandyA",100,0.5,"CandyB",45,1.25,"CandyC",200,0.9]
#print(question3(Data))

def tracetablequestion(N,L):

	D = N / L
	Z = 1
	B = False

	while Z < L:
		D = D / L
		Z = Z + 1
		B = not B

	if N != 0 and B:
		return D,B
	else:
		return Z, not B
#print(tracetablequestion(139,3))

def stockquestion(STOCK):
	lst = []


	for i in range(len(STOCK)):
		if STOCK[i] ==0:
			lst.append(i)

	return lst

#print(stockquestion( [100,99,14,0,72,0]))

def costquestion(STOCK,COST):

	Total = 0

	for i in range(len(STOCK)):
		Total = Total + (STOCK[i] * COST[i])
	return Total


#print(costquestion([100,99,14,0,72,0],[0.80,0.85,0.67,0.9,0.95,0.75]))

def combinelists(CANDY,STOCK,COST):

	newcollection = []

	for i in range(len(CANDY)):
		newword = (CANDY[i] + "-"+str(STOCK[i])+"-"+str(COST[i]))
		newcollection.append(newword)
	return newcollection

#print(combinelists(["Skor","Twix","Kit-Kat","Mr.Big","OH-Henry","Crunchy"],[100,99,14,0,72,0],[0.80,0.85,0.67,0.9,0.95,0.75]))

def lastquestion(D):

	Candy = list()
	Stock = list()
	Cost = list()
	

	for i in range(len(D)):
		N = D[i]
		N = str(N)
		for j in range(len(N)):
			if N[j] ==".":
				Cost.append(N)
			if N[j].startswith("C"):
				Candy.append(N)
			else:
				Stock.append(N)
	return Stock
	
	

DATA = ["CandyA",100,0.5,"CandyB",45,1.25,"CandyC",200,0.9]

print(lastquestion(DATA))

