def solution(board):
    answer = 0
    N = len(board)
    able = []
    visit = []
    for i in range(N):
        able.append(1)
    
    for m in range(N):
        candi = []
        for n in range(N):
            if board[m][n] == 0:
                continue
            else:
                num = board[m][n]
                if num in visit:
                    continue
                elif n < N-1 and num == board[m][n+1]:
                    able[n] = 0
                    able[n+1] = 0
                    visit.append(num)
                    if n < N-2 and num == board[m][n+2]:
                        able[n+2] = 0
                elif n > 0 and m < N-2 and num == board[m+1][n-1] and num == board[m+2][n]:
                    able[n-1] = 0
                    able[n] = 0
                    visit.append(num)
                elif n < N-1 and m < N-2 and num == board[m+1][n+1] and num == board[m+2][n]:
                    able[n] = 0
                    able[n+1] = 0
                    visit.append(num)
                elif n < N-2 and board[m+1][n+1] == num and board[m+1][n+2] == num:
                    if board[m][n+1] == 0 and board[m][n+2] == 0 and able[n+1] == 1 and able[n+2] == 1:
                        answer += 1
                        board[m][n] = 0
                        board[m+1][n] = 0
                        board[m+1][n+1] = 0
                        board[m+1][n+2] = 0
                    else:
                        able[n] = 0
                        able[n+1] = 0
                        able[n+2] = 0
                        visit.append(num)
                elif n > 1 and board[m+1][n-1] == num and board[m+1][n-2] == num:
                    if board[m][n-1] == 0 and board[m][n-2] == 0 and able[n-1] == 1 and able[n-2] == 1:
                        answer += 1
                        board[m][n] = 0
                        board[m+1][n] = 0
                        board[m+1][n-1] = 0
                        board[m+1][n-2] = 0
                    else:
                        able[n] = 0
                        able[n-1] = 0
                        able[n-2] = 0
                        visit.append(num)
                elif n > 0 and n < N-1 and board[m+1][n-1] == num and board[m+1][n+1] == num:
                    if board[m][n-1] == 0 and board[m][n+1] == 0 and able[n-1] == 1 and able[n+1] == 1:
                        answer += 1
                        board[m][n] = 0
                        board[m+1][n] = 0
                        board[m+1][n-1] = 0
                        board[m+1][n+1] = 0
                    else:
                        able[n] = 0
                        able[n-1] = 0
                        able[n+1] = 0
                        visit.append(num)
                else:
                    candi.append(n)
        while len(candi) > 0:
            j = candi.pop(0)
            number = board[m][j]
            if j < N-1 and board[m+2][j+1] == number:
                if able[j+1] == 1 and board[m][j+1] == 0 and board[m+1][j+1] == 0:
                    answer += 1
                    board[m][j] = 0
                    board[m+1][j] = 0
                    board[m+2][j] = 0
                    board[m+2][j+1] = 0
                else:
                    able[j] = 0
                    able[j+1] = 0
                    visit.append(number)
            if j > 0 and board[m+2][j-1] == number:
                if able[j-1] == 1 and board[m][j-1] == 0 and board[m+1][j-1] == 0:
                    answer += 1
                    board[m][j] = 0
                    board[m+1][j] = 0
                    board[m+2][j] = 0
                    board[m+2][j-1] = 0
                else:
                    able[j] = 0
                    able[j-1] = 0
                    visit.append(number)
    return answer