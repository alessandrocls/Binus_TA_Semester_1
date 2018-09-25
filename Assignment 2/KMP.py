def kmp(names):
    namesList = names.split('-')
    newName = ''
    for i in range(len(namesList)):
        newName = newName + namesList[i][0]
    print(newName)

kmp("Brock-Turner-Ham")