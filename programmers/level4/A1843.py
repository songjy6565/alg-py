dp = []
def sol(begin,end,ismax):
    global dp
    result = 0
    if ismax:
        if begin == end:
            return abs(dp[begin][end])
        if dp[begin][end] != 102000:
            return dp[begin][end]
        for i in range(begin,end+1):
            if i == begin and dp[i][i] < 0:
                result += -dp[i][i]
            else:
                result += dp[i][i]
        for i in range(begin,end):
            if dp[i+1][i+1] < 0:
                result = max(result, sol(begin,i,True) - sol(i+1,end,False))
            else:
                result = max(result, sol(begin,i,True) + sol(i+1,end,True))
        dp[begin][end] = result
    else:
        if begin == end:
            return abs(dp[begin][end])
        if dp[end][begin] != 102000:
            return dp[end][begin]
        for i in range(begin,end+1):
            if i == begin and dp[i][i] < 0:
                result += -dp[i][i]
            else:
                result += dp[i][i]
        for i in range(begin,end):
            if dp[i+1][i+1] < 0:
                result = min(result, sol(begin,i,False) - sol(i+1,end,True))
            else:
                result = min(result, sol(begin,i,False) + sol(i+1,end,False))
        dp[end][begin] = result
    return result

def solution(arr):
    global dp
    n = (len(arr)//2)+1
    for i in range(n):
        sub = []
        for j in range(n):
            sub.append(102000)
        dp.append(sub)
    dp[0][0] = int(arr[0])
    index = 1
    for i in range(1,len(arr),2):
        if arr[i] == "+":
            dp[index][index] = int(arr[i+1])
        else:
            dp[index][index] = -int(arr[i+1])
        index += 1
    answer = sol(0,n-1,True)
    return answer