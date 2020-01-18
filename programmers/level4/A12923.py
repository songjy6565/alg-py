import math
def IsPrime(n,prime):
    for i in range(len(prime)):
        if n%prime[i] == 0:
            return n / prime[i]
        if prime[i] > math.sqrt(n):
            return 1
    return 1

def solution(begin, end):
    answer = []
    prime = []
    index = begin
    for i in range(2,index+1):
        if IsPrime(i, prime) == 1:
            prime.append(i)
            
    while True:
        if index == end + 1:
            break
        if index == 1:
            answer.append(0)
            index += 1
            continue
        if index % 2 == 0:
            answer.append(index/2)
            index += 1
        else:
            sub = IsPrime(index, prime)
            if sub == 1:
                prime.append(index)
            answer.append(sub)
            index += 1
        
    return answer