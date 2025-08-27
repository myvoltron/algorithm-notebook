n, m = map(int, input().split())


def perm(arr, r):
    result = []
    visited = [False] * len(arr)

    def backtrack(path):
        if len(path) == r:
            result.append(path)
            return
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                backtrack(path + [arr[i]])
                visited[i] = False

    backtrack([])
    return result


result = perm(sorted(list(map(int, input().split()))), m)
for i in result:
    for j in i:
        print(j, end=" ")
    print()
