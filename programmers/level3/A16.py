check = []

def search(direction, node):
    global check
    result = 0
    for e in direction[node-1]:
        if e not in check:
            check.append(e)
            result += search(direction, e) + 1
    return result

def solution(n, results):
    global check
    right = []
    reverse = []
    answer = 0
    for i in range(n):
        right.append([])
        reverse.append([])
    for e in results:
        right[e[0]-1].append(e[1])
        reverse[e[1]-1].append(e[0])
    for j in range(1,n+1):
        total = 0
        check = []
        total += (search(right,j) + search(reverse,j))
        #print(right[j-1],reverse[j-1],total, check)
        if total == n-1:
            answer += 1
    return answer