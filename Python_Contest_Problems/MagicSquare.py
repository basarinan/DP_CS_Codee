file = open("MagicSquare.txt","r")
#Each c stands for the column. If we make a list of every column we can test whether the product of all the columns are the same
c1 = list()
c2  = list()
c3 = list()
c4 = list()


for line in file:
	newlst = line.replace("\n"," ").split(" ")
	c1.append(newlst[0])
	c2.append(newlst[1])
	c3.append(newlst[2])
	c4.append(newlst[3])



sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
rowtotal = 0
rowlst = list()

for i in range(len(c1)):
	sum1 = float(c1[i]) + sum1
	sum2 = float(c2[i]) + sum2
	sum3 = float(c3[i]) + sum3
	sum4 = float(c4[i]) + sum4
	

for i in range(len(c1)):
	rowtotal = float(c1[i]) + float(c2[i])+float(c3[i])+float(c4[i])
	rowlst.append(rowtotal)

if sum1 == rowlst[1]:
	print("magic")
else:
	print("not magic")















