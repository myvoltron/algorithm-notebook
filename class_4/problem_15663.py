n, m = map(int, input().split())


def perm(arr, r):
    s = set([])
    visited = [False] * len(arr)

    def backtrack(path):
        if len(path) == r:
            s.add(tuple(path))
            return
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                backtrack(path + [arr[i]])
                visited[i] = False

    backtrack([])
    return sorted(list(s))


result = perm(sorted(list(map(int, input().split()))), m)
for i in result:
    for j in i:
        print(j, end=" ")
    print()
