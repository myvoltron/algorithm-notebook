S1, S2 = input(), input()

# [0, 0]은 비워둠
dp = [[0] * (len(S2) + 1) for _ in range(len(S1) + 1)]

for i, c1 in enumerate(S1, 1):
    for j, c2 in enumerate(S2, 1):
        if c1 == c2:
            # 왼쪽 위, 즉 이전까지의 최적해에 1을 더한 값으로 갱신
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            # 왼쪽 혹은 위의 결과 중 큰 것으로 갱신
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
