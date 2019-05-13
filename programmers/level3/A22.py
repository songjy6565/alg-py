def solution(n, s):
    answer = []
    div = s // n
    if div < 1:
        return [-1]
    rest = s % n
    for i in range(n-rest):
        answer.append(div)
    for j in range(rest):
        answer.append(div+1)
    return answer