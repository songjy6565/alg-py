def solution(N, number):
    answer = 0
    partial = [[],[N],[],[],[],[],[],[],[]]
    for i in range(1,9):
        for a in partial[i]:
            if a == number:
                answer = i
                break
        if(answer != 0 or i == 8):
            break
        for j in range(1,i+1):
            for k in range(1,i+1):
                if j+k == i+1 and j >= k:
                    for c in partial[j]:
                        for d in partial[k]:
                            if c+d not in partial[i+1]:
                                partial[i+1].append(c+d)
                            if c-d not in partial[i+1]:
                                partial[i+1].append(c-d)
                            if c*d not in partial[i+1]:
                                partial[i+1].append(c*d)
                            if c!= 0:
                                if d//c not in partial[i+1]:
                                    partial[i+1].append(d//c)
                            if d-c not in partial[i+1]:
                                partial[i+1].append(d-c)
                            if d != 0:
                                if c//d not in partial[i+1]:
                                    partial[i+1].append(c//d)
        sum = N
        for j in range(i):
            sum *= 10
            sum += N
        if sum not in partial[i+1]:
            partial[i+1].append(sum)
        
    if answer == 0:
        answer = -1
    return answer