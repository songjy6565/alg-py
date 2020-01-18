def solution(n, cores):
    N = len(cores)
    if n <= N:
        return n
    answer = 0
    mi = 0
    ma = 250000000
    n -= N
    while True:
        mid = (mi+ma)//2
        if mi+1 == ma:
            for j in cores:
                n -= mi//j
            for k in range(N):
                if ma % cores[k] == 0:
                    n -= 1
                    if n == 0:
                        return k+1
        sub = 0
        c = 0
        for i in cores:
            sub += mid//i
            if sub >= n:
                c = 1
                ma = mid
                break
        if c == 0:
            mi = mid
    return answer