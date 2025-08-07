import sys

input = sys.stdin.readline

t = int(input())

while t > 0:
    n = int(input())
    d = dict()
    while n > 0:
        cloth, kinds = input().split()
        if kinds not in d:
            d[kinds] = 1
        else:
            d[kinds] += 1
        n -= 1
    values = d.values()
    result = 1
    for i in values:
        result *= i + 1
    result -= 1
    print(result)
    t -= 1
