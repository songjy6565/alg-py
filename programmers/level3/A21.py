def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def solution(n, k):
    answer = []
    order = []
    for i in range(1,n+1):
        order.append(i)
    for j in range(1,n+1):
        fac = factorial(n-j)
        index = k//fac
        k = k % fac
        if k == 0:
            answer.append(order.pop(index-1))
            order.sort(reverse=True)
            answer = answer + order
            break
        elif k == 1:
            answer.append(order.pop(index))
            answer = answer + order
            break
        else:
            answer.append(order.pop(index))
    return answer