def modulo42():

    modList = []
    for i in range(10):
        num = int(input("Please input a number:\n")) % 42
        if num not in modList:
            modList.append(num)

    print(len(modList))

modulo42()