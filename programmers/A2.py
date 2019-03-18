def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0, 0, 0]
    for i in range(len(answers)):
        if(a1[i%5] == answers[i]):
            count[0]+=1
        if(a2[i%8] == answers[i]):
            count[1]+=1
        if(a3[i%10] == answers[i]):
            count[2]+=1
    if(count[0] > count[1] and count[0] > count[2]):
        answer = [1]
    elif(count[1] > count[0] and count[1] > count[2]):
        answer = [2]
    elif(count[2] > count[0] and count[2] > count[1]):
        answer = [3]
    elif(count[0] > count[2] and count[1] == count[0]):
        answer = [1, 2]
    elif(count[0] > count[1] and count[2] == count[0]):
        answer = [1, 3]
    elif(count[1] > count[0] and count[1] == count[2]):
        answer = [2, 3]
    else:
        answer = [1, 2, 3]
    return answer