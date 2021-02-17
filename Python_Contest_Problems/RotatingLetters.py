def rotatingletters():


    word = input()
    if len(word) > 30:
        return "NO"
    
    index = ["I","O","S","H","Z","X","N"]

    for i in range(len(word)):
        if word[i] not in index:
            return "NO"

    return "YES"






        

print(rotatingletters())


