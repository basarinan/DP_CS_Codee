def whereisn():
    num = input()
    num = int(num)

    if num == 1 or num >= 9:
        return 1
    elif num == 2 or num <= 3 or num >= 7:
        return 2
    else:
        return 3
    



    # if num == "1":
    #     return 1
    # elif num == "2":
    #     return 2
    # elif num == "3":
    #     return 2
    # elif num == "4":
    #     return 3
    # elif num == "5":
    #     return 3
    # elif num == "6":
    #     return 3
    # elif num == "7":
    #     return 2
    # elif num == "8":
    #     return 2
    # elif num == "9":
    #     return 1
    # elif num == "10":
    #     return 1
print(whereisn())