def solution(strings, n):
    answer = strings
    answer.sort()
    return sorted(answer, key = lambda x:x[n:n+1])