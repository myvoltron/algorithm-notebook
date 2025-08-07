n = int(input())

original = list(map(int, input().split()))
copied = original.copy()
copied = list(set(copied))
copied.sort()
d = dict()
for i in range(len(copied)):
    d[copied[i]] = i

for i in original:
    print(d[i], end=" ")
