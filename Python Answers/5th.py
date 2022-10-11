from collections import defaultdict
import math

def find(arr, option = 2):
    arr.sort(key = lambda x : int(x[2]))
    # print(arr)
    uniqueVisitors = dict()
    visits = dict()
    allVisitors = defaultdict(set)
    Time = dict()
    highestTimeSpent = dict()
    entryVisit = dict()
    highVisit = dict()
    roomNumbers = set()
    highVisitorsTime = dict()

    for roomNumber, visitorNumber, time in arr:
        # if (roomNumber == '6'):
        #     print(visitorNumber, time)
        roomNumbers.add(roomNumber)
        if visitorNumber not in allVisitors[roomNumber]:
            uniqueVisitors[roomNumber] = 1 + uniqueVisitors.get(roomNumber, 0)
            allVisitors[roomNumber].add(visitorNumber)

        if (roomNumber, visitorNumber) not in entryVisit:
            entryVisit[(roomNumber, visitorNumber)] = time
        else:
            entryTime = entryVisit[(roomNumber, visitorNumber)]
            timeSpent = int(time) - int(entryTime)
            Time[roomNumber] = timeSpent + Time.get(roomNumber, 0)
            visits[roomNumber] = 1 + visits.get(roomNumber, 0)
            highVisitorsTime[(roomNumber, visitorNumber)] = timeSpent + highVisitorsTime.get((roomNumber, visitorNumber), 0)
            highestVisitTime = highVisit.get(roomNumber, 0)
            currVisitorTime = highVisitorsTime[(roomNumber, visitorNumber)]
            if currVisitorTime > highestVisitTime:
                highVisit[roomNumber] = currVisitorTime
            del entryVisit[(roomNumber, visitorNumber)]

    res = []
    for i in roomNumbers:
        currRoomNumber = i
        currUniqueVisitors = uniqueVisitors[currRoomNumber]
        timeSpentTotal = Time[currRoomNumber]
        totalVisits = visits[currRoomNumber]
        currAverage = round(timeSpentTotal / totalVisits)
        currhighestVisitTime = highVisit[currRoomNumber]
        # print(highVisit[currRoomNumber])
        if option == 0 :
            res.append((currRoomNumber, currUniqueVisitors))
        elif option == 1 :
            res.append((currRoomNumber, currUniqueVisitors, currAverage))
        elif option == 2:
            res.append((currRoomNumber, currUniqueVisitors, currAverage, currhighestVisitTime))
    res.sort(key = lambda x : int(x[0]))
    print(res)

test_case = [('15', '3', '61'), ('15', '3', '45'), ('6', '0', '91'), ('10', '4', '76'), ('6', '0', '86'), ('6', '4', '2'), ('10', '1', '47'), ('6', '3', '17'), ('6', '4', '41'), ('15', '3', '36'), ('6', '2', '97'), ('15', '4', '58'), ('6', '0', '16'), ('10', '2', '21'), ('10', '4', '75'), ('6', '0', '76'), ('15', '4', '50'), ('10', '1', '64'), ('6', '3', '3'), ('15', '3', '35'), ('6', '2', '96'), ('10', '2', '35'), ('10', '2', '77'), ('10', '2', '48')]
find(test_case, 2)