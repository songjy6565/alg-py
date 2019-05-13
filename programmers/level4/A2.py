def solution(distance, rocks, n):
    mi = 1
    ma = distance
    rocks.sort()
    while ma > mi+1:
        mid = (ma+mi)//2
        cur = 0
        count = 0
        for e in rocks:
            if e-cur < mid:
                count += 1
            else:
                cur = e
                continue
            if count > n:
                ma = mid
                break
        if distance-cur < mid:
            count += 1
        if count <= n:
            mi = mid
        else:
            ma = mid
    return mi