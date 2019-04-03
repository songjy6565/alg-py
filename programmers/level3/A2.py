def partialsum(n, i):
    result = 1
    for j in range(1,i):
        result *= (n+j)/j
        result %= 1000000007
    return result

def solution(n):
    answer = 0
    index = 1
    while(n >= 0):
        answer += partialsum(n,index)
        answer %= 1000000007
        n -= 2
        index += 1
    return answer