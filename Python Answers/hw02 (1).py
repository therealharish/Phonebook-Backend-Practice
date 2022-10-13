"""

Homework 2

"""
import sys
import string
from collections import defaultdict

def buy_and_hold(prices, start_index=0, starting_money=100.0):
    """
    Buy and hold strategy


    Parameters:
        prices (list): stock prices
        start_index (positive integer, optional): index from which to start the strategy
        starting_money (float, optional): starting cash position. Defaults to 100.0.

    Returns:
        list containing value of position using buy and hold strategy

    Example use:
    >>> res = buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5])
    >>> [round(x, 1) for x in res]
    [100.0, 75.0, 90.0, 115.0, 125.0]
    >>> [round(x, 2) for x in buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5], start_index=2)]
    [100.0, 100.0, 100.0, 127.78, 138.89]
    """
    # Your code here. Don't change anything above.
    
    n = len(prices)
    b=[None]*n
    number_of_shares_in_the_beginning = starting_money/prices[start_index]
    for i in range(n):
        if (i <=start_index):
            b[i] = starting_money
        else:
            b[i] = prices[i] * number_of_shares_in_the_beginning
    return b

          

def moving_average(prices, n):
    """
    Calculates n-period moving average of a list of floats/integers.

    Parameters:
        prices: list of values (ordered in time),
        n: integer moving-average parameter

    Returns:
        list with None for the first n-1 values in prices and the appropriate moving average for the rest

    Example use:
    >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
    >>> [round(m, 2) if m is not None else None for m in ma]
    [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
    >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
    [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
    """
    # Your code here. Don't change anything above.
    ma = []
    for i in range(len(prices)):
        if i < n - 1:
            ma.append(None) 
        else:
            ma.append(sum(prices[i-(n-1):i+1])/n)
    return ma


def compare_mas(ma1, ma2):
    """
    Compare two moving averages.

    Compares values in ma1 and ma2 pairwise to create a list of indicators such that
    - If ma1 > ma2, indicator = 1
    - Otherwise indicator = 0
    - The moving averages may contain None-values in the beginning. If either value is None, the indicator is None

    Parameters:
        ma1 (list): moving average (list of prices)
        ma2 (list): moving average (list of prices)

    Returns:
        list: binary indicators for which moving average value is greater

    Example use:
    >>> p1 = [1, 2, 4, 5]
    >>> p2 = [0, 2.5, 5, 3]
    >>> compare_mas(p1, p2)
    [1, 0, 0, 1]
    >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    >>> p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
    >>> compare_mas(p1, p2)
    [None, None, 1, 1, 1, 0, 0, 0, 1, 1]
    """
    # Your code here. Don't change anything above.

    c = [] # list storing the indicator values
    if len(ma1)==len(ma2):
        for i in range(1, len(ma2)): #len(ma1)==len(ma2)
            if ma1[i] is not None and ma2[i] is not None:
                if ma1[i] > ma2[i]:
                    indicator = 1
                    c.append(indicator) 
                elif ma2[i] > ma1[i]:
                    indicator = 0
                    c.append(indicator) 
            else:
                c.append(None)
        return c
p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
compare_mas(p1, p2)

def ma_strategy(prices, comparisons, starting_cash=100.0):
    
    """
    Trade based on moving average crossovers
    

    Parameters:
        prices: list if stock prices
        comparisons: list of comparisons from compare_mas
        starting_cash (float, optional): Starting cash position, defaults to 100.0.

    Returns:
        list of values of the current position: either cash position or the market value of stock position
    
    We initially hold cash, and buy when we first get a signal to buy.

    More specifically, a change from value 0 to 1 in comparisons signals there's a crossover in moving averages,
    so we want to buy stock. A move from 1 to 0 signals that we want to sell stock.

    Whenever we trade, we buy with our entire cash position, or sell our entire stock position.
    We will therefore always hold either stock or cash, but never both.
    
    Assume we can hold fractional stock quantities, and there are no transaction fees.

    Example use:
    >>> starting_cash = 1.0
    >>> prices = [2,4,6,5,1]
    >>> cos = [0, 1, 1, 0, 0] # not real indicators, just to illustrate portfolio value when trading
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> values
    [1.0, 1.0, 1.5, 1.25, 1.25]
    >>> starting_cash = 1000.0
    >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    >>> cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
    """
    # Your code here. Don't change anything above.
    
    #import numpy as np
    present_value = []  
    stock_at = 0
    cash = starting_cash
    '''
    time_index = [] # time index stores the first occurence of 1 and 0 (one first and then zero) in the comparisons list 
    buy_index = [1, 0] # buy_index stores the value (1 and 0) in the comparisions list
    one_index = comparisons.index(1)
    #zero_index = comparisons.index(0, one_index) #stores the first occurence of zero after one has occured in the comparisons list
    zero_index = comparisons.index(0)
    time_index.append(one_index)
    time_index.append(zero_index)
    '''
    
    # ma strategy trade based on moving average
    
    
    time_index = []
    buy_index = []
    for i in range(len(prices)):
        if i == 0:
            present_value.append(starting_cash)
        else:
            if comparisons[i] is None:
                present_value.append(present_value[i-1])
            elif comparisons[i] == 1:
                stock_at = cash/prices[i]
                cash = 0
                present_value.append(stock_at*prices[i])
            elif comparisons[i] == 0:
                cash = stock_at*prices[i]
                stock_at = 0
                present_value.append(cash)
    return present_value                    
          


starting_cash = 1000.0
prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
values = ma_strategy(prices, cos, starting_cash)
[round(v, 2) for v in values] 





def gallery(visits, option=2):
    """
    Produce summary statistics of gallery visits.

    Parameters:
        visits: list of visits (see also HTML instructions):
            Each visit is a tuple (room number (str), visitor number (str), time (str)) (all elements are integers in string format)
            Each visitor starts outside any room, and they leave all rooms in the end.
            The visits are not necessarily in order.
        option (int, optional): determines what to return, see below
            
    Returns:
        a list containing tuples for each room (sorted in increasing number by room number (1, 2, 3, ...)):
        - if option = 0, (room number, number of unique visitors)
        - if option = 1, (room number, number of unique visitors, average visit time)
        - if option = 2, (room number, number of unique visitors, average visit time, highest total time spent in the room by a single visitor)
        - the average visit time is rounded to integer value.

    Example use:
    >>> visits = [('0', '0', '20'), ('0', '0', '25'), ('1', '1', '74'), ('1', '1', '2')]
    >>> gallery(visits)
    [('0', 1, 5, 5), ('1', 1, 72, 72)]
    >>> gallery(visits, 0)
    [('0', 1), ('1', 1)]
    >>> gallery(visits, 1)
    [('0', 1, 5), ('1', 1, 72)]
    >>> gallery(visits, 1)[0]
    ('0', 1, 5)
    >>> visits = [('15', '3', '61'), ('15', '3', '45'), ('6', '0', '91'), ('10', '4', '76'), ('6', '0', '86'), ('6', '4', '2'), ('10', '1', '47'), ('6', '3', '17'), ('6', '4', '41'), ('15', '3', '36'), ('6', '2', '97'), ('15', '4', '58'), ('6', '0', '16'), ('10', '2', '21'), ('10', '4', '75'), ('6', '0', '76'), ('15', '4', '50'), ('10', '1', '64'), ('6', '3', '3'), ('15', '3', '35'), ('6', '2', '96'), ('10', '2', '35'), ('10', '2', '77'), ('10', '2', '48')]
    >>> gallery(visits)
    [('6', 4, 24, 65), ('10', 3, 15, 43), ('15', 2, 8, 17)]
    """
    # Your code here. Don't change anything above.
    visits.sort(key = lambda x : int(x[2]))
    # print(arr)
    uniqueVisitors = dict()
    visitRecord = dict()
    allVisitors = defaultdict(set)
    Time = dict()
    entryVisit = dict()
    highVisit = dict()
    roomNumbers = set()
    highVisitorsTime = dict()

    for roomNumber, visitorNumber, time in visits:
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
            visitRecord[roomNumber] = 1 + visitRecord.get(roomNumber, 0)
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
        totalVisits = visitRecord[currRoomNumber]
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
    return (res)


def reverse_engineer(seq):
    """
    Reverse engineer an input sequence
    
    Parameters:
        seq - list of strings
    
    Returns:
        list of values corresponding to each letter present in the sequences (smallest possible values)
        (in alphabetical order)
    
    Example use
    >>> reverse_engineer(["a", "ab", "c", "a", "ab", "ac"])
    [2, 4, 5]
    >>> reverse_engineer(["b", "bc", "ab", "bc", "b", "abc", "b"])
    [3, 1, 2]
    >>> reverse_engineer(["a", "b", "d", "c", "a", "ab"])
    [6, 9, 11, 10]
    >>> reverse_engineer(['c', 'ce', 'd', 'c', 'ce', 'd', 'c', 'a', 'ce', 'cd', 'b', 'ce', 'c', 'd', 'ce', 'c', 'a', 'd', 'ce', 'c', 'cde', 'c', 'b', 'ce', 'd', 'ac', 'ce', 'd', 'c', 'ce', 'cd', 'ce', 'a', 'bc', 'd', 'ce', 'c', 'd', 'ce', 'c', 'cde', 'a', 'c', 'ce', 'df', 'b', 'c', 'ce', 'd', 'c', 'ace', 'cd', 'ce', 'c', 'd', 'ce', 'b', 'c', 'ad', 'ce', 'c'])
    [17, 23, 3, 7, 6, 91]
    """
    # Your code here. Don't change anything above.
    #Let's find the different combinations first

    input = seq
    values = {}
    factors = []
    highest_factor = {}
    #Setup a complete List of factors
    for line in input :
        temp_factors = {}
        for char in line :
            highest_factor[char] = highest_factor.get(char, 0) + 1
            temp_factors[char] = highest_factor[char]
        factors.append(temp_factors)

    i = 0
    highest_val = 0
    #itterate forward as many times as nessessary
    while i < len(factors) :
        if i == 0 :
            for key in factors[i].keys() :
                values[key] = 1
            i += 1
            continue
        # compare previous line to current
        prev_key = list(factors[i - 1])[0]
        cur_key = list(factors[i])[0]
        total_prev = values[prev_key] * factors[i - 1][prev_key]
        total_cur = values.get(cur_key, 0) * factors[i][cur_key]
        highest_val = max(highest_val,total_cur)
        if total_prev >= total_cur :
            # too low, adjust
            values[cur_key] = int(total_prev / factors[i][cur_key] + 1)
            #return to previous instance of key if it exists and retry
            i = 1
            continue

        # check equality on same line
        current_keys = list(factors[i])
        modified = False
        for j,x in enumerate(current_keys[:len(current_keys) - 1]) :
            for y in current_keys[j + 1:len(current_keys)] :
                total_x = values.get(x,0) * factors[i][x]
                total_y = values.get(y,0) * factors[i][y]
                if total_x == total_y :
                    continue
                elif total_x < total_y :
                    values[x] = max(int(total_y / factors[i][x]),values.get(x,0) + 1)
                    highest_val = max(highest_val,values[x] * factors[i][x])
                    modified = True
                else :
                    values[y] = max(int(total_x / factors[i][y]),values.get(y,0) + 1)
                    highest_val = max(highest_val,values[y] * factors[i][y])
                    modified = True
        if modified :
            i = 1
            continue
        else :
            i += 1
    lower = string.ascii_lowercase
    highest_letter_found = False
    for char in lower[::-1] :
        if values.get(char,0) > 0:
            highest_letter_found = True
        elif highest_letter_found :
            values[char] = highest_val + 1
    # print (list(values.items()).sort(key = lambda x : x[0]))
    temp = (sorted(values.items(), key=lambda kv:
                 kv[0]))
    res = []
    for i in temp:
        res.append(i[1])
    return (res)

# Test the function

# print(reverse_engineer(["a", "b", "a", "a", "b", "a"]))

# print(reverse_engineer(["a", "ab", "c", "a", "ab", "ac"]))

# print(reverse_engineer(["b", "bc", "ab", "bc", "b", "abc", "b"]))

# print(gallery([('0', 1, 5, 5), ('1', 1, 72, 72)]))
