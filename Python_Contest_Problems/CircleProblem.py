import math
#input
x1 = input()
x1= float(x1)
y1 = input()
y1 = float(y1)
x2 = input()
y2 = float(y2)
#process
#r = ((y2-y1)**(2) + (x2-x1)**(2))**(1/2)
r = math.sqrt((y2-y1)**(2) + (x2-x1)**(2))

a = 3.14159*r*r
a = round(a,,3)

print(a)



