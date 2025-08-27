import sys

input = sys.stdin.readline

n, k = map(int, input().split())

weights = []
values = []
for i in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = weights[i - 1], values[i - 1]
    for k in range(k + 1):
        dp[i][k] = dp[i - 1][k]
        if k >= w:
            dp[i][k] = max(dp[i][k], dp[i - 1][k - w] + v)

print(dp[n][k])
