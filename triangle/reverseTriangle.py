size = input("Input triangle size\n");

for i in range(size):
    stars = ''
    whiteSpace = ''
    for j in range(size - i):
        whiteSpace = whiteSpace + ' '
    for k in range(i + 1):
        stars += '*'
    print(whiteSpace+ stars + '\n')