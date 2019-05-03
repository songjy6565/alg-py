def solution(weight):
    weight.sort()
    answer = weight.pop(0)
    if answer != 1:
        return 1
    while(len(weight) > 0):
        cur = weight.pop(0)
        if cur-1 <= answer:
            answer += cur
        else:
            return answer+1
    return answer+1