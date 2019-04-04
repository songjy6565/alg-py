def solution(n, computers):
    answer = 0
    connect = []
    current = 0
    next = 0
    for i in range(n):
        if i not in connect:
            connect.append(i)
            answer += 1
            next += 1
        while (next > current):
            for j, v in enumerate(computers[connect[current]]):
                if v == 1 and j not in connect:
                    connect.append(j)
                    next += 1
            current += 1
    return answer