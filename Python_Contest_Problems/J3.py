year = input()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
lst = list()

while True:
    year = int(year) +1
    year = str(year)


    for i in range(len(year)):
        if year[i] == "1":
            count1 = count1 + 1
            lst.append(count1)
        if year[i] == "2":
            count2 = count2 +1
            lst.append(count2)
        if year[i] == "3":
            count3 = count3 + 1
            lst.append(count3)

        if year[i] == "4":
            count4 = count4 + 1
            lst.append(count4)
        if year[i] == "5":
            count5 = count5 +1
            lst.append(count5)
        if year[i] == "6":
            count6 = count6 +1
            lst.append(count6)
        if year[i] == "7":
            count7 = count7 + 1
            lst.append(count7)
            
        if year[i] == "8":
            count8 = count8 +1
            lst.append(count8)
        if year [i] == "9":
            count9 = count9 +1
            lst.append(count9)
        if year[i] == "0":
            count0 = count0 +1
            lst.append(count0)
    
    for i in range(len(lst)):
        if lst[i] > 1:
            
        
            
















    






