def solution(N, number):
    dp = [set() for _ in range(9)]
    for count in range(1, 9):
        dp[count].add(int(str(N) * count))
        for i in range(1, count):
            for a in dp[i]:
                for b in dp[count - i]:
                    dp[count].add(a + b)
                    dp[count].add(a - b)
                    dp[count].add(a * b)

                    if b != 0:
                        dp[count].add(a // b)

        if number in dp[count]:
            return count
    return -1


result = solution(5, 12)
print(result)
