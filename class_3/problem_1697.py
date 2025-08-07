n, m = map(int, input().split())

INF = int(1e9)

dp = [INF] * (m + 2)

result = 0
if n <= m:
    for i in range(m + 2):
        if i <= n:
            dp[i] = n - i
            continue

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = min(
                dp[i], dp[(i + 1) // 2] + 2, dp[(i - 1) // 2] + 2, dp[i - 1] + 1
            )
    result = dp[m]
else:
    result = n - m

print(result)

