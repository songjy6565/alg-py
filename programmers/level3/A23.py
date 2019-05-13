def solution(n):
    answer = [[1,3]]
    for i in range(1,n):
        cur = []
        for e in answer:
            temp = [e[0],e[1]]
            if temp[0] == 2:
                temp[0] = 3
            elif temp[0] == 3:
                temp[0] = 2
            if temp[1] == 2:
                temp[1] = 3
            elif temp[1] == 3:
                temp[1] = 2
            cur.append(temp)
        cur.append([1,3])
        for e in answer:
            temp = [e[0],e[1]]
            if temp[0] == 1:
                temp[0] = 2
            elif temp[0] == 2:
                temp[0] = 1
            if temp[1] == 1:
                temp[1] = 2
            elif temp[1] == 2:
                temp[1] = 1
            cur.append(temp)
        answer = cur
    return answer