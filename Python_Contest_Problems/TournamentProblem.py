first = input()
second = input()
third = input()
fourth = input()
fifth = input()
sixth = input()

# First = "W"
# Second = "L"
# Third = "W"
# Fourth = "L"
# Fifth ="W"
# Sixth = "L"


lst = list()
lst.append(first)
lst.append(second)
lst.append(third)
lst.append(fourth)
lst.append(fifth)
lst.append(sixth)
wins = 0

for i in range(len(lst)):
	if lst[i] == "W":
		wins = wins+1

if wins == 0:
	print(-1)
if wins == 1 or wins == 2:
	print(3)
if wins == 3 or wins == 4:
	print(2)
if wins == 5 or wins == 6:
	print(1)


