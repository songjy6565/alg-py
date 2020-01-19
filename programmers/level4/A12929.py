def fac(n):
    if n <= 1:
        return 1
    return n*fac(n-1)
def sol(n):
    if n == 1:
        return 1 
    return fac(2*n)/(fac(n)*fac(n+1))
def solution(n):
    answer = 0
    answer = sol(n)
    return answer