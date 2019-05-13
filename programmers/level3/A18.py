def solution(n):
    answer = 0
    first = 1
    second = 2
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        for i in range(n-2):
            answer = first + second
            first = second
            second = answer
    return answer %1234567