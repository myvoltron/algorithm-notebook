from collections import deque

a, b = map(int, input().split())


def bfs(start, target):
    # node, count, path
    q = deque([(start, 0, [start])])

    while q:
        v = q.popleft()

        for i in [v[0] * 2, v[0] * 10 + 1]:
            if i == target:
                return v[1] + 2
            if i > target:
                continue
            if i in v[2]:
                continue

            q.append((i, v[1] + 1, v[2] + [i]))
    return -1


print(bfs(a, b))
