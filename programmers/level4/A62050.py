def Mst(n, costs):
    answer = 0
    costs = sorted(costs, key = lambda x:x[2])
    connect = [[costs[0][0],costs[0][1]]]
    answer += costs[0][2]
    costs.pop(0)
    count = 1
    for e in costs:
        if count == n-1:
            break
        c = 0
        for i, a in enumerate(connect):
            if e[0] in a and e[1] in a:
                answer -= e[2]
                count -= 1
                c = 1
                break
            elif e[0] in a:
                case = 0
                for j in range(i+1,len(connect)):
                    if e[1] in connect[j]:
                        connect.append(connect[i]+connect[j])
                        connect.pop(j)
                        connect.pop(i)
                        case = 1
                        break
                if case == 0:
                    connect[i].append(e[1])
                c = 1
                break
            elif e[1] in a:
                case = 0
                for k in range(i+1,len(connect)):
                    if e[0] in connect[k]:
                        connect.append(connect[i]+connect[k])
                        connect.pop(k)
                        connect.pop(i)
                        case = 1
                        break
                if case == 0:
                    connect[i].append(e[0])
                c = 1
                break
        if c == 0:
            connect.append([e[0],e[1]])
        count += 1
        answer += e[2]
    return answer

def solution(land, height):
    group = []
    N = len(land)
    for i in range(N):
        sub = []
        for j in range(N):
            sub.append(-1)
        group.append(sub)
    index = 0
    queue = []
    for m in range(N):
        for n in range(N):
            if group[m][n] == -1:
                group[m][n] = index
                if m-1 >= 0 and abs(land[m][n]-land[m-1][n]) <= height:
                    queue.append((m-1,n))
                    group[m-1][n] = index
                if n-1 >= 0 and abs(land[m][n]-land[m][n-1]) <= height:
                    queue.append((m,n-1))
                    group[m][n-1] = index
                if m+1 <= N-1 and abs(land[m][n]-land[m+1][n]) <= height:
                    queue.append((m+1,n))
                    group[m+1][n] = index
                if n+1 <= N-1 and abs(land[m][n]-land[m][n+1]) <= height:
                    queue.append((m,n+1))
                    group[m][n+1] = index
                while len(queue) > 0:
                    a,b = queue.pop(0)
                    if a-1 >= 0 and abs(land[a][b]-land[a-1][b]) <= height and group[a-1][b] == -1:
                        queue.append((a-1,b))
                        group[a-1][b] = index
                    if b-1 >= 0 and abs(land[a][b]-land[a][b-1]) <= height and group[a][b-1] == -1:
                        queue.append((a,b-1))
                        group[a][b-1] = index
                    if a+1 <= N-1 and abs(land[a][b]-land[a+1][b]) <= height and group[a+1][b] == -1:
                        queue.append((a+1,b))
                        group[a+1][b] = index
                    if b+1 <= N-1 and abs(land[a][b]-land[a][b+1]) <= height and group[a][b+1] == -1:
                        queue.append((a,b+1))
                        group[a][b+1] = index
                index = index + 1
            
    kruskal = []
    for m in range(N):
        for n in range(N):
            cur = group[m][n]
            node = 0
            if m+1 <= N-1:
                node = group[m+1][n]
                if node != cur:
                    ele = []
                    ele.append(cur)
                    ele.append(node)
                    ele.append(abs(land[m][n]-land[m+1][n]))
                    kruskal.append(ele)
            if n+1 <= N-1:
                node = group[m][n+1]
                if node != cur:
                    ele = []
                    ele.append(cur)
                    ele.append(node)
                    ele.append(abs(land[m][n]-land[m][n+1]))
                    kruskal.append(ele)
    '''
    graph = []
    for i1 in range(index):
        sub1 = []
        for j1 in range(index):
            sub1.append(10001)
        graph.append(sub1)
    
    for m in range(N):
        for n in range(N):
            cur = group[m][n]
            node = 0
            if m+1 <= N-1:
                node = group[m+1][n];
                if node != cur and abs(land[m][n]-land[m+1][n]) < graph[cur][node]:
                    graph[cur][node] = abs(land[m][n]-land[m+1][n])
                    graph[node][cur] = graph[cur][node]
            if n+1 <= N-1:
                node = group[m][n+1];
                if node != cur and abs(land[m][n]-land[m][n+1]) < graph[cur][node]:
                    graph[cur][node] = abs(land[m][n]-land[m][n+1])
                    graph[node][cur] = graph[cur][node]
    kruskal = []
    for m1 in range(index):
        for n1 in range(index):
            if n1 > m1 and graph[m1][n1] != 10001:
                element = []
                element.append(m1)
                element.append(n1)
                element.append(graph[m1][n1])
                kruskal.append(element)
    '''
    answer = Mst(index,kruskal)
    return answer