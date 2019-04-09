import heapq

def solution(jobs):
    before = -1
    current = 0
    wait = []
    n = len(jobs)
    answer = 0
    count = 0
    while count < n:
        for a in jobs:
            if before < a[0] <= current:
                answer += (current - a[0])
                heapq.heappush(wait, a[1])
        if len(wait) > 0:
            answer += len(wait)*wait[0]
            before = current
            current += heapq.heappop(wait)
            count += 1
        else:
            current += 1
    return answer//n