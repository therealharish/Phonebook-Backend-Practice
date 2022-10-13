def check(starting_cash, prices, cos):
    res = []
    firstZeroPos = -1
    newarr = []
    # for i, j, z in zip(prices, cos, temparr):
    #     newarr.append((i, j, z))
    # print(newarr)
    
    # print(cos)

    lastBuy = False
    temp = starting_cash
    res = []
    for i in range(len(cos)-1):
        prevCost = cos[i-1]
        currCost = cos[i]
        nextCost = cos[i+1]
        if(lastBuy == False):
            res.append(starting_cash)
        else:
            res.append(temp)
        temp = 0
        # print(res, cos[i], prices[i])
        if lastBuy == False and currCost == 1 and prevCost==0:
            temp = starting_cash / prices[i]
            lastBuy = True
            if currCost == 1 and nextCost == 1:
                temp+= temp * prices[i]
        elif lastBuy and currCost == 1 and prevCost==0:
            temp = res[i] / prices[i]
            if lastBuy and currCost == 1 and nextCost == 1:
                temp+= temp * prices[i]
            
        if lastBuy and currCost == 1 and prevCost == 1:
            temp+= res[-1] / prices[i] * prices[i]
            
        if(lastBuy and currCost == 0 and prevCost == 1):
            temp =  res[i]
    res.append(res[-1]/prices[-2]*prices[-1])
    res = [round(v, 2) for v in res]
    print(res) 

starting_cash = 1000.0
prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
temparr = [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
# check(starting_cash, prices, cos)

starting_cash = 1.0
prices = [2,4,6,5,1]
cos = [0, 1, 1, 0, 0] # not real indicators, just to illustrate portfolio value when trading
ans = [1.0, 1.0, 1.5, 1.25, 1.25]
check(starting_cash, prices, cos)