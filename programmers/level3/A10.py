def solution(triangle):
    answer = [triangle[0][0]]
    triangle.pop(0)
    for a in triangle:
        temp = []
        temp.append(answer[0] + a[0])
        for i in range(1,len(answer)):
            temp.append(max(answer[i-1]+a[i], answer[i]+a[i]))
        temp.append(answer[-1]+a[-1])
        answer = temp
    return max(answer)