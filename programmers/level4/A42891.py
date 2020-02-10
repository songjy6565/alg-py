def solution(food_times, k):
    answer = 0
    N = len(food_times)
    n = N
    k += 1
    while True:
        if n == 0:
            return -1
        times = k // n
        if times == 0:
            for i in range(N):
                case = food_times[i]
                if case == 0:
                    continue
                else:
                    if k == 1:
                        answer = i+1
                        return answer
                    else:
                        k -= 1
        else:
            for i in range(N):
                case = food_times[i]
                if case == 0:
                    continue
                elif case <= times:
                    k -= case
                    n -= 1
                    food_times[i] = 0
                    if k == 0:
                        answer = i+1
                        return answer
                else:
                    k -= times
                    food_times[i] -= times
                    if k == 0:
                        answer = i+1
                        return answer
            
    return answer