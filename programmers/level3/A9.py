def solution(n, edge):
    answer = []
    count = []
    checked = 1
    edge.sort()
    for i, e in enumerate(edge):
        if e[0] == 1:
            answer.append(e[1])
            count.append(i)
        elif e[1] == 1:
            answer.append(e[0])
            count.append(i)
    checked += len(answer)
    count.sort(reverse=True)
    for c in count:
        edge.pop(c)
    while checked < n:
        count = []
        temp = []
        for j, e1 in enumerate(edge):
            if e1[0] in answer:
                if e1[1] not in temp and e1[1] not in answer:
                    temp.append(e1[1])
                    checked += 1
                if j not in count:
                    count.append(j)
            elif e1[1] in answer:
                if e1[0] not in temp:
                    temp.append(e1[0])
                    checked += 1
                if j not in count:
                    count.append(j)
        count.sort(reverse=True)
        for c1 in count:
            edge.pop(c1)
        answer = temp
    return len(answer)