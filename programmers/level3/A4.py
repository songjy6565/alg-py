def solution(N):
    answer = 4
    pprev = 0
    prev = 1
    current = 1
    for i in range(1,N):
        answer += (current*2)
        pprev = prev
        prev = current
        current = pprev + prev
    return answer