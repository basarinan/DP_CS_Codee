time = input()

h = time[0:2]
h = int(h)
m = time[3:5]
x = "AM" #assume AM

if(12<= h <=23):
	x = "PM"
	h = h-12


#Is there a process we can apply to convert either case
	print(str(h)+":"+str(m)+" "x)
for i in range(0,3,1):
	t = input()

	convertTime(t)
