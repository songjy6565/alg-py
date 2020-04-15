def solution(strs, t):
    dic = {}
    N = len(t)
    for i in range(1, N+1):
        for e in strs:
            if (i-len(e)) < 0:
                continue
            if t[:i] == e:
                dic[i-1] = 1
                break
            if i-len(e)-1 in dic:
                if t[i-len(e):i] == e:
                    if i-1 not in dic:
                        dic[i-1] = dic[i-len(e)-1]+1
                    else:
                        dic[i-1] = min(dic[i-1],dic[i-len(e)-1]+1)
    if N-1 not in dic:
        return -1
    return dic[N-1]
'''
def solution(strs, t):
    if t in strs:
        return 1
    dp = []
    N = len(t)
    for i in range(N):
        dp.append(0)
    for i in range(1, N+1):
        for e in strs:
            if (i-len(e)) < 0:
                continue
            if t[:i] == e:
                dp[i-1] = 1
                continue
            if dp[i-len(e)-1] != 0:
                if t[i-len(e):i] == e:
                    if dp[i-1] == 0:
                        dp[i-1] = dp[i-len(e)-1]+1
                    else:
                        dp[i-1] = min(dp[i-1],dp[i-len(e)-1]+1)
    if dp[N-1] == 0:
        return -1
    return dp[N-1]

def solution(strs, t):
    if t in strs:
        return 1
    dp = []
    N = len(t)
    for i in range(N):
        dp.append(0)
    if t[0] in strs:
        dp[0] = 1
    for i in range(1, N):
        if t[:i+1] in strs:
            dp[i] = 1
            continue
        for j in range(i):
            if dp[j] == 0:
                continue
            if dp[i] == 0 or dp[j]+1 < dp[i]:
                if t[j+1:i+1] in strs:
                    dp[i] = dp[j]+1
    print(dp)
    if dp[N-1] == 0:
        return -1
    return dp[N-1]

def sol(strs, t, N):
    if t in strs:
        return 1
    answer = N
    for e in strs:
        if len(t) < len(e):
            continue
        if t[:len(e)] == e:
            answer = min(answer, sol(strs, t[len(e):], N)+1)
    return answer

def solution(strs, t):
    answer = sol(strs, t, len(t)+1)
    if answer == len(t)+1:
        return -1
    return answer
'''