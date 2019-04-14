def solution(n, costs):
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