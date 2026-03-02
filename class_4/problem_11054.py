# n = int(input())
# seq = list(map(int, input().split()))
#
# result = -1
#
#
# # 올랐다가 내렸다가
# # 오름차순
# # 내림차순
# def is_bitonic(sequence):
#     if len(sequence) < 3:
#         return True
#
#     is_increasing = False
#     is_turned = False
#     if sequence[0] < sequence[1]:
#         is_increasing = True
#     elif sequence[0] > sequence[1]:
#         is_increasing = False
#     else:
#         return False
#
#     for i in range(2, len(sequence)):
#         if sequence[i - 1] < sequence[i]:
#             if is_increasing:
#                 continue
#             else:
#                 if is_turned:
#                     return False
#                 else:
#                     is_turned = True
#                     is_increasing = True
#         elif sequence[i - 1] > sequence[i]:
#             if is_increasing:
#                 if is_turned:
#                     return False
#                 else:
#                     is_turned = True
#                     is_increasing = False
#             else:
#                 continue
#         else:
#             return False
#     return True
#
#
# def dfs(depth, m):
#     global result
#
#     if is_bitonic(path):
#         result = max(result, depth)
#     else:
#         return
#
#     if depth == m:
#         return
#
#     start = 0 if depth == 0 else index_path[-1] + 1
#     for i in range(start, len(seq)):
#         index_path.append(i)
#         path.append(seq[i])
#         dfs(depth + 1, m)
#         path.pop()
#         index_path.pop()
#
#
# def dfs2(depth, is_increasing, is_turned):
#     global result
#
#     result = max(result, depth)
#     if depth == n:
#         return
#
#     start = 0 if depth == 0 else index_path[-1] + 1
#     for i in range(start, n):
#         current_is_increasing = is_increasing
#         current_is_turned = is_turned
#
#         if depth == 1:
#             if seq[index_path[-1]] < seq[i]:
#                 current_is_increasing = True
#                 current_is_turned = False
#             elif seq[index_path[-1]] > seq[i]:
#                 current_is_increasing = False
#                 current_is_turned = False
#             else:
#                 continue
#         elif depth >= 2:
#             if seq[index_path[-1]] < seq[i]:
#                 if not is_increasing:
#                     if is_turned:
#                         continue
#                     else:
#                         current_is_increasing = True
#                         current_is_turned = True
#             elif seq[index_path[-1]] > seq[i]:
#                 if is_increasing:
#                     if is_turned:
#                         continue
#                     else:
#                         current_is_increasing = False
#                         current_is_turned = True
#             else:
#                 continue
#         index_path.append(i)
#         dfs2(depth + 1, current_is_increasing, current_is_turned)
#         index_path.pop()
#
#
# index_path = []
# path = []
# # dfs(0, n)
# dfs2(0, False, False)
# print(result)
#
# # print(is_bitonic([1, 5, 2, 1, 4, 3, 4, 5, 2, 1]))
#

n = int(input())
seq = list(map(int, input().split()))

dp = [0] * 1001
inc_dp = [0] * 1001
dec_dp = [0] * 1001


for start_index in range(n):
    tmp = []
    for i in range(start_index):
        if seq[start_index] > seq[i]:
            tmp.append(inc_dp[i])
    if not tmp:
        inc_dp[start_index] = 1
    else:
        inc_dp[start_index] = max(tmp) + 1

for start_index in range(n - 1, -1, -1):
    tmp = []
    for i in range(start_index + 1, n):
        if seq[start_index] > seq[i]:
            tmp.append(dec_dp[i])
    if not tmp:
        dec_dp[start_index] = 1
    else:
        dec_dp[start_index] = max(tmp) + 1

for start_index in range(n):
    dp[start_index] = inc_dp[start_index] + dec_dp[start_index] - 1

print(max(dp))
