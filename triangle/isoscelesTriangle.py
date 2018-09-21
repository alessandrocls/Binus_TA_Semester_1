size = input("Input triangle size\n");
increment = 0
for i in range(size):
    stars = ''
    whiteSpace = ''
    for j in range(0,size - i):
        whiteSpace = whiteSpace + ' '
    for k in range(i + 1 + increment):
        stars += '*'
    increment += 1
    print(whiteSpace+ stars + '\n')