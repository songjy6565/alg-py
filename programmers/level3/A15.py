def solution(m, n, puddles):
    answer = []
    for i in range(m):
        answer.append([])
        for j in range(n):
            answer[i].append(1)
    for e in puddles:
        answer[e[0]-1][e[1]-1] = 0
    for k in range(1,m):
        if answer[k][0] != 0:
            answer[k][0] = answer[k-1][0]
    for l in range(1,n):
        if answer[0][l] != 0:
            answer[0][l] = answer[0][l-1]
    for i in range(1,n):
        for j in range(1,m):
            if answer[j][i] != 0:
                answer[j][i] = answer[j-1][i] + answer[j][i-1]
    return answer[m-1][n-1] % 1000000007