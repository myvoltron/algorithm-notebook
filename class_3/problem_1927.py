import sys
import heapq

input = sys.stdin.readline

n = int(input())
hq = []
while n > 0:
    oper = int(input())
    if oper == 0:
        if not hq:
            print(0)
        else:
            v = heapq.heappop(hq)
            print(v)
    else:
        heapq.heappush(hq, oper)
    n -= 1
