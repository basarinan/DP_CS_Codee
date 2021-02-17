duration= input()

lst = list()

while True:

    duration = int(duration)-1
    lst.append(duration)
    
    


    if duration == 0:break

lst.append(int(duration))





hours = 12
minutes = 0
count = 0
lst = len(lst)-1

for i in range(lst):
    minutes = int(minutes)
    hours = int(hours)
    minutes = minutes + 1 
    if minutes >= 60:
        minutes = minutes - 60
        if hours + 1 < 13:
            hours = hours + 1
            
            
        else:
            hours = (hours + 1) % 12
            
            
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = minutes 
    minutes = str(minutes)
    hours = str(hours)
    time = hours + minutes
        
    if len(time) == 3:
        if (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0])):
            count = count + 1 
    else:
        if ((int(time[3]) - int(time[2])) == (int(time[2]) - int(time[1]))) and ((int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0]))):
            count = count+ 1 
  

print(count)



    



