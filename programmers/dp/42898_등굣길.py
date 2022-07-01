def solution(m, n, puddles):
    d = [[0] * (m) for _ in range(n)]  
    d[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            if [j+1,i+1] in puddles or [i, j] == [0, 0]:
                continue
            else:
                d[i][j] = d[i-1][j] + d[i][j-1]
    return (d[-1][-1] % 1000000007)