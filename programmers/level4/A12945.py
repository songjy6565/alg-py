def sol(i, j,visit,mat,Max):
    if i == j:
        return 0
    if str(i)+str(j) in visit:
        return visit[str(i)+str(j)]
    result = Max
    for a in range(i, j):
        result = min(result, sol(i,a,visit,mat,Max)+sol(a+1,j,visit,mat,Max)+mat[i][0]*mat[a][1]*mat[j][1])
    visit[str(i)+str(j)] = result
    return result

def solution(matrix_sizes):
    mat = matrix_sizes
    answer = 0
    visit = {}
    N = len(matrix_sizes)
    answer = sol(0,N-1,visit,matrix_sizes,200*200*200*N)
    return answer