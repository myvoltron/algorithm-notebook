import sys

input = sys.stdin.readline

t = int(input().rstrip())

while t > 0:
    n = int(input().rstrip())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    result = max(dp[0][0], dp[1][0])
    for i in range(1, n):
        for j in range(2):
            cond = []
            if j == 0:
                cond.append(dp[1][i - 1])
            else:
                cond.append(dp[0][i - 1])

            if i >= 2:
                cond.append(dp[0][i - 2])
                cond.append(dp[1][i - 2])

            dp[j][i] = max(cond) + sticker[j][i]
            result = max(dp[j][i], result)

    print(result)
    t -= 1
