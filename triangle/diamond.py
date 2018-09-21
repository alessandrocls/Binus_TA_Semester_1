# size = input("Input triangle size\n");
# increment = 0
# for i in range(size):
#     stars = ''
#     whiteSpace = ''
#     for j in range(0,size - i):
#         whiteSpace = whiteSpace + ' '
#     for k in range(i + 1 + increment):
#         stars += '*'
#     increment += 1
#     print(whiteSpace+ stars + '\n')
#
# for i in range(size, -1, -1):
#     stars = ''
#     whiteSpace = ''
#     for j in range(0,size - i):
#         whiteSpace = whiteSpace + ' '
#     for k in range(0, i + 1 + increment):
#         stars += '*'
#     increment -= 1
#     print(whiteSpace+ stars + '\n')


height = input("Input diamond height:\n");
for i in range(height-1):
    print((height-i) * ' ' + (2*i+1) * '*')
for i in range(height-1, -1, -1):
    print((height-i) * ' ' + (2*i+1) * '*')
