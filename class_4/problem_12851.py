from collections import deque

n, k = map(int, input().split())


def bfs(start, end, visited, count):
    q = deque([(start, 0)])
    visited[start] = 0
    count[start] = 1

    while q:
        v, step = q.popleft()
        next_step = step + 1

        if v == end:
            continue

        for i in [v - 1, v + 1, v * 2]:
            if i > 100000 or i < 0:
                continue

            if visited[i] < next_step:
                continue
            elif visited[i] == next_step:
                count[i] += 1
            else:
                visited[i] = next_step
                count[i] = 1

            q.append((i, next_step))

    return (visited[end], count[end])


result = bfs(n, k, [float("inf")] * 100001, [0] * 100001)

print(result[0])
print(result[1])


# def bfs2(start, end, visited):
#     q = deque([(start, 0)])
#     result = 0
#
#     while q:
#         point, count = q.popleft()
#
#         if count >= path_count:
#             continue
#
#         for i in [point - 1, point + 1, point * 2]:
#             if i > 100000 or i < 0:
#                 continue
#             if visited[i] > count + 1:
#                 continue
#
#             if count + 1 == path_count:
#                 if i == end:
#                     result += 1
#                     break
#                 else:
#                     continue
#
#             visited[i] = count + 1
#             q.append((i, count + 1))
#     return result
#
#
# if n >= k:
#     print(n - k)
#     print(1)
# else:
#     path_count = bfs(n, k, [False] * 100001)
#     same_count = bfs2(n, k, [0] * 100001)
#
#     print(path_count)
#     print(same_count)
#

# INF = float("inf")
# dp = [INF] * (k + 2)
# count = [0] * (k + 2)
#
# result = (0, 0)
# if n <= k:
#     for i in range(k + 2):
#         if i <= n:
#             dp[i] = n - i
#             count[i] = 1
#             continue
#
#         if i % 2 == 0:
#             minimum = min(dp[i], dp[i // 2] + 1, dp[i - 1] + 1)
#             current = 0
#             for i in [dp[i], dp[i // 2] + 1, dp[i - 1] + 1]:
#                 if minimum == i:
#                     current +=
#                     count[i] += 1
#             dp[i] = minimum
#             dp[i] =
#         else:
#             dp[i] = min(
#                 dp[i], dp[(i + 1) // 2] + 2, dp[(i - 1) // 2] + 2, dp[i - 1] + 1
#             )
#         result = (dp[k], 1)
#
# else:
#     result = (n - k, 1)
#
# print(result[0])
# print(result[1])
