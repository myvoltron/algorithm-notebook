n, k = map(int, input().split())

dp = [0] * 100001

stack = [(n, 0)]
result = [0, 0]
while stack:
    v = stack.pop()

    if v[0] + 1
