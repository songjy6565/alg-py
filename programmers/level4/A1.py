def solution(n):
    answer = 0
    prev = 3
    cur = 11
    if n == 2:
        return prev
    elif n == 4:
        return cur
    else:
        i = 6
        while i <= n:
            answer = 3*cur + (cur-prev)
            prev = cur
            cur = answer
            i += 2
    return answer % 1000000007