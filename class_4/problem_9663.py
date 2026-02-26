n = int(input())


def dfs(x, visited):
    if x == n:
        return 1

    result = 0
    for i in range(n):
        visited[x] = i
        if is_safe(x, visited):
            result += dfs(x + 1, visited)

    return result


def is_safe(x, visited):
    for i in range(x):
        # 열이 같은지 확인
        if visited[i] == visited[x]:
            return False
        # 대각선인지 확인
        if abs(visited[i] - visited[x]) == abs(i - x):
            return False
    return True


visited = [0] * n
print(dfs(0, visited))
