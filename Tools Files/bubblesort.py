def bubblesort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0, len(lst)-1-i):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [12,52,16,42,88,86]
print(bubblesort(lst))
        
        