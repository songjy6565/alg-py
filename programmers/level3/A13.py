def solution(budgets, M):
    Min = 0
    if sum(budgets) < M:
        return max(budgets)
    Max = max(budgets)
    while Max > Min:
        if Max == Min + 1:
            return Min
        Sum = 0
        mid = (Max + Min) // 2
        for e in budgets:
            if Sum > M:
                break
            if e > mid:
                Sum += mid
            else:
                Sum += e
        if Sum > M:
            Max = mid
        else:
            Min = mid
    return Min