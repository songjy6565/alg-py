def solution(cookie):
    answer = 0
    summ = 0
    s = []
    for e in cookie:
        summ += e
        s.append(summ)
        
    N = len(cookie)
    for m in range(N):
        l = m
        r = m+1
        while True:
            if l < 0 or r >= N:
                break
            if l == 0:
                lsum = s[m]
            else:
                lsum = s[m]-s[l-1]
            rsum = s[r]-s[m]
            if lsum == rsum:
                answer = max(lsum,answer)
                l -= 1
                r += 1
                continue
            if lsum < rsum:
                l -= 1
            else:
                r += 1
    return answer