import sys

input = sys.stdin.readline

n = int(input())

house = []
for _ in range(n):
    # red 0, green 1, blue 2
    house.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * n for _ in range(n)]
dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]
for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2])
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2])
        else:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1])
        dp[i][j] += house[i][j]


result = INF
for i in range(3):
    result = min(result, dp[n - 1][i])
print(result)
