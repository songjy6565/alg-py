def solution(a, b):
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    diff = 0
    for i in range(a-1):
        diff += months[i]
    diff += (b - 1)
    answer = days[diff % 7]
    return answer