def palin(mid, s, case):
    if case == 0:
        result = 1
        ma = mid+1
    else:
        result = 2
        ma = mid+2
    mi = mid-1
    while True:
        if mi < 0 or ma > len(s)-1:
            return result
        if s[mi] != s[ma]:
            return result
        else:
            mi -= 1
            ma += 1
            result += 2
        
def solution(s):
    answer = 1
    for i in range(len(s)-1):
        answer = max(answer, palin(i,s,0))
        if s[i] == s[i+1]:
            answer = max(answer, palin(i,s,1))
    return answer