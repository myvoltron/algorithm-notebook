# import sys
# from bisect import bisect_left
#
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# tree = []
# while True:
#     line = input().strip()
#     if not line:
#         break
#     tree.append(int(line))
#
#
# def postorder(tree):
#     if len(tree) == 1:
#         print(tree[0])
#         return
#
#     index = bisect_left(tree[1:], tree[0])
#     # right가 없는 경우
#     if index >= len(tree) - 1:
#         postorder(tree[1:])
#     # left가 없는 경우
#     elif index == 0:
#         postorder(tree[1:])
#     else:
#         postorder(tree[1 : index + 1])
#         postorder(tree[index + 1 :])
#     print(tree[0])
#
#
# postorder(tree)

import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []
while True:
    line = input().strip()
    if not line:
        break
    tree.append(int(line))


def postorder(start, end):
    if start > end:
        return

    root = tree[start]

    mid = bisect_right(tree, root, start + 1, end + 1)

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(root)


postorder(0, len(tree) - 1)
