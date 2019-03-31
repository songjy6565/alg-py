def solution(s, n):
    answer = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if lower.find(i) != -1:
            answer += lower[(lower.find(i)+n)%26]
        elif upper.find(i) != -1:
            answer += upper[(upper.find(i)+n)%26]
        else:
            answer += " "
    return answer