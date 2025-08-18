import math

dp = [0] * 50001
for i in range(1, 224):
    dp[i**2] = 1

for i in range(1, 50001):
    if dp[i] == 1:
        continue

    dp[i] = 4
    for j in range(1, int(math.sqrt(i)) + 1):
        e = dp[i - j**2] + 1
        dp[i] = min(dp[i], dp[i - j**2] + 1)
        if dp[i] == 2:
            break

n = int(input())
print(dp[n])
