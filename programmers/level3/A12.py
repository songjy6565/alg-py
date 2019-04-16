def solution(n, times):
    Min = 0
    Max = n * max(times)
    while Max > Min+1:
        mid = (Min + Max)//2 + (Min + Max) % 2
        possible = 0
        for e in times:
            possible += mid // e
        if possible == n and Max == Min+1:
            return mid
        elif possible >= n:
            Max = mid
        else:
            Min = mid
    return Max