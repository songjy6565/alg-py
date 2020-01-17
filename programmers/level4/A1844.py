def solution(maps):
    answer = 0
    N=len(maps)
    M=len(maps[0])
    queue = [(0,0)]
    while len(queue) > 0:
        a,b = queue.pop(0)
        answer = maps[a][b]
        if a == N-1 and b == M-1:
            return answer
        if a-1 >= 0 and maps[a-1][b] == 1:
            queue.append((a-1,b))
            maps[a-1][b] = answer + 1 
        if b-1 >= 0 and maps[a][b-1] == 1:
            queue.append((a,b-1))
            maps[a][b-1] = answer + 1
        if a+1 <= N-1 and maps[a+1][b] == 1:
            queue.append((a+1,b))
            maps[a+1][b] = answer + 1
        if b+1 <= M-1 and maps[a][b+1] == 1:
            queue.append((a,b+1))
            maps[a][b+1] = answer + 1
    return -1