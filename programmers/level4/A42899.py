def solution(K, travel):
    timetable = []
    for i in range(len(travel)+1):
        sub = []
        for j in range(K+1):
            sub.append(0)
        timetable.append(sub)
    index = 0
    while len(travel) > 0:
        cur = travel.pop(0)
        for i in range(K+1):
            if i >= cur[0] and timetable[index][i-cur[0]] !=-1:
                a = timetable[index][i-cur[0]]+cur[1]
            else:
                a = -1
            if i >= cur[2] and timetable[index][i-cur[2]] !=-1:
                b = timetable[index][i-cur[2]]+cur[3]
            else:
                b = -1
            timetable[index+1][i] = max(a,b)
        index += 1
    return  timetable[-1][K]