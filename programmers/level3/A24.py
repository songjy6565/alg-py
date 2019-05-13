def solution(N, road, K):
    answer = 1
    graph = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        graph.append(temp)
    for e in road:
        if graph[e[0]-1][e[1]-1] == 0 or e[2] < graph[e[0]-1][e[1]-1]:
            graph[e[0]-1][e[1]-1] = e[2]
            graph[e[1]-1][e[0]-1] = e[2]
    queue = [0]
    d = [0]
    for k in range(N-1):
        d.append(500001)
    while len(queue) > 0:
        cur = queue.pop(0)
        for i,e in enumerate(graph[cur]):
            if e > 0:
                if d[cur]+e < d[i]:
                    d[i] = d[cur]+e
                    queue.append(i)
    for i in range(1,N):
        if d[i] <= K:
            answer += 1
    return answer