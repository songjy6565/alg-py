def dupcheck(a, b):
    if max(a[0],b[0]) <= min(a[1],b[1]):
        return True
    return False

def solution(routes):
    routes.sort()
    answer = 1
    candi = routes.pop(0)
    for a in routes:
        if dupcheck(a,candi):
            candi = [max(a[0],candi[0]),min(a[1],candi[1])]
        else:
            candi = a
            answer += 1
    return answer