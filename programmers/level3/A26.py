def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    i = 0
    j = 0
    while j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
    return answer