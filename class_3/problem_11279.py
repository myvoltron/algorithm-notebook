import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

q = []
while n > 0:
    oper = int(input().rstrip())
    if oper == 0:
        if q:
            v = heapq.heappop(q)
            print(v * -1)
        else:
            print(0)
    else:
        heapq.heappush(q, oper * -1)

    n -= 1
