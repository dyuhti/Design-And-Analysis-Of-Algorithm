def path(m,n,N,i,j):

    MOD = 10 **9+7
    dp=[[[0 for _ in range(n)]for _ in range(m)] for _ in range(N+1)]
    dp[0][i][j]=1
    directions =[(1,0),(-1,0),(0,1),(0,-1)]
    result = 0

    for k in range(1,N+1):
        new_dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N + 1)]
        for x in range(m):
            for y in range(n):
                for d in directions:
                    nx,ny = x+d[0],y+d[1]
                    if 0 <= nx < m and 0 <= ny < n:
                        new_dp[k][x][y] = (new_dp[k][x][y] + dp[k - 1][nx][ny]) % MOD
                    else:
                        result = (result + dp[k - 1][x][y]) % MOD

        dp = new_dp

    return result

print(path(2, 2, 2, 0, 0))
print(path(1, 3, 3, 0, 1))