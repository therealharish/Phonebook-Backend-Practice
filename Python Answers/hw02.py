"""

Homework 2

"""

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
    time_index = []
    buy_index = []
    for t in range(1, len(comparisons)): 
            if comparisons[t] != None and comparisons[t-1]!= None:
                if comparisons[t]!= comparisons[t-1]:
                    time_index.append(t)
                    buy_index.append(comparisons[t])
            elif comparisons[t]!= None and comparisons[t-1]==None:
                time_index.append(t)
                buy_index.append(comparisons[t])
    
    for i in range(0,len(prices)):
        if i==0: # we have no buy or sell at i = 0
            new_value = prices[i] 
            present_value.append(cash)  
            continue

        new_value = (prices[i] - prices[i-1])/prices[i-1]
        if (i == time_index): # crossover point (buy or sell)     #isko sahi krna hai
            #p= np.where(time_index == i)
            #if (buy_index[j for j in range(len(buy_index)) if time_index[i] ==i]) == 1: # buy
            p = [(j) for j in range(len(buy_index)) if time_index[i] ==i]
            if buy_index[p] == 1:
                stock_at = cash
                cash = 0 
                present_value.append(stock_at)                                                           
            else: # sell
                if stock_at == 0: # didn't buy at the past
                    cash = present_value[i-1] # i-1 because it didn't change
                    present_value.append(present_value[i-1])
                else: # buy at the past
                    cash = present_value[i-1] + present_value[i-1]*new_value
                    stock_at = 0
                    present_value.append(cash)
        else:
            if cash == 0: # a buy has occured in the past but not now (not sell because cash=0)          
                stock_at = present_value[i-1] + present_value[i-1]*new_value
                present_value.append(stock_at)
            else:
                present_value.append(cash) # a buy or sell has never occured                     
          
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
    pass
    # produce summary statistic of gallery visits 
    
    


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

    def combinations(iterable, r):

        # take the iterable as tuple
        lst_of_comb = tuple(iterable)
        # n= length of the tuple
        n = len(lst_of_comb)
        # if r > n return
        if r > n:
            return
        # save list(range(r) in inds
        inds = list(range(r)) # indices
        # intially save inds in lst_of_comb
        yield tuple(lst_of_comb[i] for i in inds)
        # find a combination in one iteration and   
        # append these combination tuples to lst_of_comb
        # finally return(using yield) lst_of_comb
        while True:
            for i in reversed(range(r)):
                if inds[i] != i + n - r:
                    break
            else:
                return
            inds[i] = inds[i]+1
            for j in range(i+1, r):
                inds[j] = inds[j-1] + 1
            yield tuple(lst_of_comb[i] for i in inds)
        # Find the permutations of the given list lst
                
    def permutation(p_lst): 
        # If p_lst is empty return empty list
        if len(p_lst) == 0:
            return []
        # If there is only one element in lst then,
        #return p_lst in list
        if len(p_lst) == 1:
            return [p_lst]
        # otherwise, find the permutations
        lst = [] # to store current permutation
        # Iterate the input(p_lst) and compute the permutation
        for i in range(len(p_lst)):
            m = p_lst[i]
            remLst = p_lst[:i] + p_lst[i+1:]
        for p in permutation(remLst):
            lst.append([m] + p)
        return lst
    
    def reverse_engineer(seq):
        letters_lst=[] # to store the different letter exist in the output
        # loop throgh input(seq) and append each letter if it is already
        # does not exist in alp_lst
        for strg in seq:
            for letter in strg:
                if letter not in letters_lst:
                    letters_lst.append(letter)
        letters_lst.sort()
        alphabets="abcdefghijklmnopqrstuvwxyz"
        # find if there are any missing letters between any two letters
        # and add them to alp_lst
        temp_lst=alphabets[:alphabets.find(letters_lst[-1])+1]
        for ltr in temp_lst:
            if ltr not in letters_lst:
                letters_lst.append(ltr)
        # sort the letters list
        letters_lst.sort()
        data = list(range(20))[1:] # in place of 20 you can replace any number, even upto four digit number
        cmb_lst=combinations(data,len(letters_lst))
        per_lst=[] # to store permutations of each combination
        for cmb in list(cmb_lst):
            temp=permutation(list(cmb))
            for x in temp:
                per_lst.append(x)
        per_lst.sort()
        gen_lst=[]
        solution=()
        # for each permutation(tuple), find a sequence and check whether it is equal to input(seq) or not
        for tup in per_lst:
            strg=""
            for i in range(20):# in place of 20 you can replace any number, even upto four digit number
                if i!=0:
                    for t in tup:
                        if i%t==0 :
                            strg=strg+letters_lst[tup.index(t)]
                    if strg!="":
                        gen_lst.append(strg)
                    strg=""
                    # if current list is equal to input(seq) , exit the loop
                    if gen_lst==seq:
                        break
        # if current list is equal to input(seq) , set current tuple as solution
        # and exit
            if gen_lst==seq:
                solution=tup
                break
        # if current list is not equal to seq, make gen_list empty
            gen_lst=[]
        # return the solution
        return list(solution)
# Test the function

print(reverse_engineer(["a", "b", "a", "a", "b", "a"]))

print(reverse_engineer(["a", "ab", "c", "a", "ab", "ac"]))

print(reverse_engineer(["b", "bc", "ab", "bc", "b", "abc", "b"]))

print(reverse_engineer(["a", "b", "d", "c", "a", "ab"]))
