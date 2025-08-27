n, m = map(int, input().split())


def comb(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path)
            return
        for i in range(start, len(arr)):
            backtrack(i, path + [arr[i]])

    backtrack(0, [])
    return result


result = comb(sorted(list(set(list(map(int, input().split()))))), m)
for i in result:
    for j in i:
        print(j, end=" ")
    print()
