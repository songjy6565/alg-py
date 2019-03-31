def solution(arr):
    answer = []
    target = -1
    for i in range(len(arr)):
        if target != arr[i]:
            answer.append(arr[i])
            target = arr[i]
    
    return answer