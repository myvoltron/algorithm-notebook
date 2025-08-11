dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

t = int(input())
while t > 0:
    print(dp[int(input())])
    t -= 1
