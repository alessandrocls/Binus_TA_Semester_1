size = input("Input triangle size\n");

for i in range(size):
    stars = ''
    for j in range(i + 1):
        stars += '*'
    print(stars + '\n')