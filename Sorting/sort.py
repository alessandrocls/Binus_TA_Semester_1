import time
from random import shuffle


list = list(range(1,1001))
shuffle(list)

def selection(list):
    for i in range(len(list)):
        index = i
        for j in range(i + 1, len(list)):
            if list[index] > list[j]:
                index = j
        list[i], list[index] = list[index], list[i]
    return list

def bubble(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def insertion(list):
    for i in range(1, len(list)):
        comparison = list[i]
        j = i - 1
        while j >= 0 and comparison < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = comparison
    return list

def main():
    print(list)
    print("\n")
    sortType = input("Which type of sorting method would you like to use? (Selection, Bubble, Insertion): \n").lower()
    if sortType == "selection":
        start = time.time()
        sortedList = selection(list)
        end = time.time()
        print(sortedList)
        print('{} {} {}'.format("The program took", end-start, "seconds to run."))
    elif sortType == "bubble":
        start = time.time()
        sortedList = bubble(list)
        end = time.time()
        print(sortedList)
        print('{} {} {}'.format("The program took", end-start, "seconds to run."))
    elif sortType == "insertion":
        start = time.time()
        sortedList = insertion(list)
        end = time.time()
        print(sortedList)
        print('{} {} {}'.format("The program took", end-start, "seconds to run."))
    else:
        print("Invalid sort type.")
        main()


main()