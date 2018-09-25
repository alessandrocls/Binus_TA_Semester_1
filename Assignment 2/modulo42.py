def modulo42():
    numList = []
    modList = []
    for i in range(10):
        numList.append(int(input("Please input a number:\n")))
    for i in range(len(numList)):
        if numList[i] % 42 not in modList:
            modList.append(numList[i] % 42)
    print(len(modList))

modulo42()