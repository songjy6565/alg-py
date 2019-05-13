def solution(n, works):
    answer = 0
    if sum(works) < n:
        return answer
    works.sort(reverse=True)
    ma = works[0]
    mi = 0
    while True:
        mid = (ma+mi)//2
        Sum = 0
        for e in works:
            if e < mid:
                ma = mid
                break
            else:
                Sum += (e-mid)
                if Sum > n:
                    mi = mid
                    break
        if ma != mid and mi != mid:
            ma = mid
        if ma <= mi+1:
            break
    for i in range(len(works)):
        if works[i] <= ma:
            break
        else:
            n -= works[i]-ma
            works[i] = ma
    for j in range(n):
        works[j] -= 1
    for k in range(len(works)):
        answer += works[k]**2
    return answer