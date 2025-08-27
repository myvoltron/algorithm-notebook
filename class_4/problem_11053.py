n = int(input())
arr = list(map(int, input().split()))


dp = [0] * 1001


def recurv(arr):
    result = -1
    for start_index in range(len(arr)):
        tmp = []
        for i in range(start_index):
            if arr[start_index] > arr[i]:
                tmp.append(dp[i])
        if not tmp:
            dp[start_index] = 1
        else:
            dp[start_index] = max(tmp) + 1
        result = max(result, dp[start_index])
    return result


print(recurv(arr))

# 3 4 1 5 6 -> 3 4 5 6
# 10 30 20 30 40 50 -> 10 20 30 40 50 -> 5
# 10 20 10 30 20 50 -> 10 20 30 50 -> 4
# 50 40 1 2 3 4 -> 1 2 3 4 -> 4
