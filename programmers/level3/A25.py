def solution(n, stations, w):
    answer = 0
    cover = 0
    width = 2*w+1
    for e in stations:
        if e-w > cover+1:
            answer += (e-w-1-cover)//width
            if (e-w-1-cover) % width > 0:
                answer += 1
        cover = e+w
    if cover < n:
        answer += (n-cover)//width
        if (n-cover) % width > 0:
            answer += 1
    return answer