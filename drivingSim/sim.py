import matplotlib.pyplot as plt


time = int(input("Time spent on road?\n"))
acceleration = int(input("Acceleration of car?\n"))
distance = int(input("Distance travelled?\n"))
distanceList = []
timeList = [i for i in range(time+1)]
speeding = False
destinationReached = False
finalSpeed = acceleration * time


for i in timeList:
    travelled = 0.5 * acceleration * i**2
    distanceList.append(travelled)
    travelledStars = int(travelled / 10)
    print("Duration: {} Distance: {}".format(i, '*' * travelledStars))

finalDistance = distanceList[-1]

if finalSpeed > 60 :
    print("The person went over the speed limit. (Max speed was {}m/s)".format(finalSpeed))
else:
    print("The person did not go over the speed limit. (Max speed was {}m/s)".format(finalSpeed))

if finalDistance < distance:
    print("The person did not reach the destination. (Reached {}m)".format(finalDistance))
else:
    print("The person reached the destination. (Reached {}m)".format(finalDistance))
plt.plot(timeList, distanceList, 'r-')
plt.ylabel("Distance (m)")
plt.xlabel("Time (s)")

# print(distanceList)
plt.show()
