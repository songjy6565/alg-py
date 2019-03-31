def solution(s):
    answer = ''
    mid = len(s)//2
    if len(s)%2 :
        answer = s[mid:mid+1]
    else:
        answer = s[mid-1:mid+1]
    return answer