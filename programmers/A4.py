def solution(n, lost, reserve):
    answer = 0
    matched = []
    for i in range(len(lost)):
        target = lost[i]
        if target in reserve:
            answer += 1
            matched.append(target)
        elif target-1 in reserve and target-1 not in matched and target-1 not in lost:
            answer += 1
            matched.append(target-1)
        elif target+1 in reserve and target+1 not in matched and target+1 not in lost:
            answer += 1
            matched.append(target+1)
    answer += (n - len(lost))
    return answer