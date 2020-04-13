import sys
sys.setrecursionlimit(1500)

def find(a, b):
    if a not in b:
        b[a] = a+1
        return a
    c = find(b[a], b)
    b[a] = c+1
    return c

def solution(k, room_number):
    b = dict()
    answer = []
    for e in room_number:
        answer.append(find(e,b))
    return answer
'''
def solution(k, room_number):
    answer = []
    dic = {}
    for e in room_number:
        if e not in dic:
            answer.append(e)
            dic[e] = e+1
            continue
        index = dic[e]
        while True:
            if index not in dic:
                answer.append(index)
                dic[index] = index+1
                dic[e] = index+1
                break
            index = dic[index]
    return answer

def solution(k, room_number):
    answer = []
    room = []
    for i in range(1,k+1):
        room.append(i)
    for e in room_number:
        index = e-1
        while True:
            if room[index] == index+1:
                answer.append(room[index])
                room[index] += 1
                room[e-1] = room[index]
                break
            index = room[index]-1
    return answer

def solution(k, room_number):
    answer = []
    room = []
    for i in range(1,k+1):
        room.append(i)
    for e in room_number:
        index = 0
        while True:
            if room[e-1+index] != 0:
                answer.append(room[e-1+index])
                room[e-1+index] = 0
                break
            index += 1
    return answer
    
def solution(k, room_number):
    answer = []
    room = []
    for i in range(1,k+1):
        room.append(i)
    for e in room_number:
        Min = e-1
        Max = len(room)-1
        while True:
            mid = (Min + Max) // 2
            if Min+1 == Max:
                if room[Min] != 0:
                    answer.append(room[Min])
                    room[Min] = 0
                    break
                if room[Max] != 0:
                    answer.append(room[Max])
                    room[Max] = 0
                    break
            if room[mid] == 0:
                Min = mid
                continue
            if room[mid] != 0:
                Max = mid
                continue
    print(room)
    return answer
  
def assign(index):
    global room
    ascend = index+1
    descend = index-1
    value = room[index]
    room[index] += 1
    while True:
        if ascend < len(room) and room[ascend] == value:
            room[ascend] += 1
            ascend += 1
        else:
            break
    while True:
        if descend >= 0 and room[descend] == value:
            room[descend] += 1
            descend -= 1
        else:
            break
def solution(k, room_number):
    answer = []
    global room
    for i in range(1,k+1):
        room.append(i)
    for e in room_number:
        answer.append(room[e-1])
        assign(e-1)
    print(room)
    return answer

def solution(k, room_number):
    answer = []
    room = []
    for i in range(1,k+1):
        room.append(i)
    for e in room_number:
        Min = 0
        Max = len(room)-1
        while True:
            mid = (Min + Max) // 2
            if room[mid] == e or Min == Max:
                answer.append(room[mid])
                room.pop(mid)
                break
            if room[mid] > e:
                Max = mid
                continue
            if room[mid] < e:
                Min = mid
                continue
    return answer
'''