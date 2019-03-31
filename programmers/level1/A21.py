def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if d[i] > budget:
            return i
        budget -= d[i]
    return len(d)