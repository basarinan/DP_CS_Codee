import math
x1 = 2
y1 = 4
x2 = 4
y2 = 8

n = y2-y1
t = x2-x1

r = Math.pow(Math.pow(n,2)+Math.pow(t,2),1/2)

a = r*r * 3.14159

a.toPrecision(5)

console.log(a)

