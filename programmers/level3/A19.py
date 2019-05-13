def solution(dirs):
    answer = 0
    horiz = []
    verti = []
    for i in range(11):
        horiz.append([0,0,0,0,0,0,0,0,0,0])
        verti.append([0,0,0,0,0,0,0,0,0,0])
    cur = [5,5]

    for e in dirs:
        if e == 'U':
            if cur[1] == 10:
                continue
            elif verti[cur[0]][cur[1]] != 1:
                answer += 1
                verti[cur[0]][cur[1]] = 1
            cur[1] += 1
        elif e == 'D':
            if cur[1] == 0:
                continue
            elif verti[cur[0]][cur[1]-1] != 1:
                answer += 1
                verti[cur[0]][cur[1]-1] = 1
            cur[1] -= 1
        elif e == 'R':
            if cur[0] == 10:
                continue
            elif horiz[cur[1]][cur[0]] != 1:
                answer += 1
                horiz[cur[1]][cur[0]] = 1
            cur[0] += 1
        elif e == 'L':
            if cur[0] == 0:
                continue
            elif horiz[cur[1]][cur[0]-1] != 1:
                answer += 1
                horiz[cur[1]][cur[0]-1] = 1
            cur[0] -= 1   
    return answer