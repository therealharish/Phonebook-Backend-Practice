

def solve(n, m, totalCost):
    MAXN = 55;
    MAXM = 105;
    MAXCOST = 55;
    MOD = 1e9 + 7;
    
    finalOutput = []
    for ar in range(len(n)):
        cum = [[[0 for k in range(MAXCOST)] for j in range(MAXM)] for i in range(MAXN)]
        dp = [[[0 for k in range(MAXCOST)] for j in range(MAXM)] for i in range(MAXN)]
        for j in range(1, m[ar]+1):
            dp[1][j][0] = 1
            cum[1][j][0] = j
        nValue = n[ar]
        mValue = m[ar]
        costValue = totalCost[ar]
        
        for i in range(2, nValue+1):
            for j in range(1, mValue+1):
                for k in range(0, costValue+1):
                    dp[i][j][k] = (j * dp[i - 1][j][k]) % MOD
                    if k != 0:
                        dp[i][j][k] += cum[i - 1][j - 1][k-1]
                        dp[i][j][k] %= MOD
                    cum[i][j][k] = (cum[i][j - 1][k] + dp[i][j][k]) % MOD
        finalOutput.append(cum[nValue][mValue][costValue])
    return finalOutput


n = [2, 3, 4]
m = [3, 3, 3]
totalCost = [1, 2, 2]
finalOutput = solve(n, m, totalCost)
for i in range(len(finalOutput)):
    print(int(finalOutput[i]))
