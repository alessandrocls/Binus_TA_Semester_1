cups = [1,0,0]

def switcharoo (list, move):
    move = move.lower()
    if move == 'a':
        list[0], list[1] = list[1], list[0]
    elif move == 'b':
        list[1], list[2] = list[2], list[1]
    elif move == 'c':
        list[0], list[2] = list[2], list[0]
    return list

def cupsAndBalls (cups,moves):
    for i in range(len(moves)):
        list = switcharoo(cups, moves[i])
    location = list.index(1) + 1
    print(location)


cupsAndBalls(cups, 'AB')