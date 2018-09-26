import sys

def trianglePrettify(triangleList):
    for i in range(len(triangleList)):
        prettyLine = ''
        for j in range(len(triangleList), i-1, -1):
            prettyLine = prettyLine + ' '
        prettyLine = prettyLine +  ' '.join(str(tri) for tri in triangleList[i])
        print(prettyLine)


def pascal(height):
    triangle = []
    if height == 1:
        triangle.append([1])
    elif height == 0:
        trianglePrettify(triangle)
        sys.exit()
    elif height < 0:
        print("Invalid height.")
        sys.exit()
    elif height == 2:
        triangle.append([1])
        triangle.append([1,1])
    else:
        triangle.append([1])
        triangle.append([1,1])
        for i in range(3,height + 1):
            triangleLine = []
            for j in range(i):
                if j == 0 or j == (i-1):
                    triangleLine.append(1)
                else:
                    triangleLine.append(triangle[i-2][j-1] + triangle[i-2][j])
            triangle.append(triangleLine)
    trianglePrettify(triangle)

height = int(input("Input triangle height:\n"))
pascal(height)