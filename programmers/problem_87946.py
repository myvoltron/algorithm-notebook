def solution(k, dungeons):
    visited = [False] * len(dungeons)

    def backtrack(current):
        max_count = 0
        for i in range(len(dungeons)):
            if visited[i]:
                continue

            dungeon = dungeons[i]
            if dungeon[0] > current:
                continue

            # 방문하지 않았고 최소 필요 피로도를 충족함
            visited[i] = True

            count = 1 + backtrack(current - dungeon[1])
            max_count = max(max_count, count)

            visited[i] = False
        return max_count

    return backtrack(k)


result = solution(80, [[80, 20], [50, 40], [30, 10]])  # 3
print(result)
