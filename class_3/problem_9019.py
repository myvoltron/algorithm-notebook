import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


# 123 -> 1230
# 1000 -> 1
def rotate_left(v):
    n1 = v // 1000
    n2 = (v % 1000) // 100
    n3 = ((v % 1000) % 100) // 10
    n4 = (((v % 1000) % 100) % 10) // 1

    return ((n2 * 10 + n3) * 10 + n4) * 10 + n1


def rotate_right(v):
    n1 = v // 1000
    n2 = (v % 1000) // 100
    n3 = ((v % 1000) % 100) // 10
    n4 = (((v % 1000) % 100) % 10) // 1

    return ((n4 * 10 + n1) * 10 + n2) * 10 + n3


def bfs(start, end, visited):
    q = deque([(start, "")])
    visited[start] = True

    while q:
        v = q.popleft()

        for i in [
            (v[0] * 2 % 10000, "D"),
            (9999 if v[0] == 0 else v[0] - 1, "S"),
            (rotate_left(v[0]), "L"),
            (rotate_right(v[0]), "R"),
        ]:
            if i[0] == end:
                return v[1] + i[1]
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append((i[0], v[1] + i[1]))


while n > 0:
    a, b = map(int, input().split())
    visited = [False] * 10000
    print(bfs(a, b, visited))
    n -= 1
