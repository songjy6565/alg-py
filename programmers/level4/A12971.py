def solution(sticker):
    answer = 0
    N = len(sticker)
    if N == 1:
        return sticker[0]
    elif N == 2:
        return max(sticker[0],sticker[1])
    elif N == 3:
        return max(sticker[0],sticker[1],sticker[2])
    prev = sticker[N-1]
    cur = max(sticker[N-1],sticker[0])
    prev1 = sticker[0]
    cur1 = max(sticker[0],sticker[1])
    prev2 = sticker[1]
    cur2 = max(sticker[1],sticker[2])
    
    temp = 0
    for i in range(2,N-1):
        temp = max(prev+sticker[i-1],cur)
        prev = cur
        cur = temp
        
        temp = max(prev1+sticker[i],cur1)
        prev1 = cur1
        cur1 = temp
        
        temp = max(prev2+sticker[i+1],cur2)
        prev2 = cur2
        cur2 = temp

    return max(cur, cur1, cur2)