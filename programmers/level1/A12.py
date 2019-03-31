def solution(s):
    answer = ''
    arr = sorted(s, reverse=True)
    for e in arr:
        answer += e
    return answer