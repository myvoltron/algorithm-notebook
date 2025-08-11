n = int(input())

fruit = list(map(int, input().split()))


def count_kinds(dp):
    result = 0
    for i in dp:
        if i == 0:
            continue
        result += 1
    return result


start = 0
end = 0
result = -1

dp = [0] * 10
dp[fruit[0]] += 1

while start <= end and end < len(fruit):
    kinds_count = count_kinds(dp)

    if kinds_count <= 2:
        if sum(dp) > result:
            result = sum(dp)

        end += 1
        if end >= len(fruit):
            break
        dp[fruit[end]] += 1
    else:
        start += 1
        dp[fruit[start - 1]] -= 1

print(result)
