def solution(money):
    pprev = money[0]
    prev = pprev
    pprev2 = money[1]
    prev2 = money[2]
    pprev3 = money[-1]
    prev3 = pprev3
    answer = pprev
    answer2 = max(pprev2, prev2)
    answer3 = pprev3
    for i in range(2,len(money)-1):
        answer = max(pprev+money[i], prev)
        answer2 = max(pprev2+money[i+1], prev2)
        answer3 = max(pprev3+money[i-1], prev3)
        pprev = prev
        prev = answer
        pprev2 = prev2
        prev2 = answer2
        pprev3 = prev3
        prev3 = answer3
    return max(answer,answer2,answer3)