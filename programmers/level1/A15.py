import math

def IsPrime(n,prime):
    for i in range(len(prime)):
        if n%prime[i] == 0:
            return False
        if prime[i] > math.sqrt(n):
            return True
    return True

def solution(n):
    prime = []
    for i in range(2,n+1):
        if IsPrime(i, prime):
            prime.append(i)
    return len(prime)