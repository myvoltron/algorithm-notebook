import sys
import heapq

input = sys.stdin.readline

n = int(input())

q = []
while n > 0:
    oper = int(input())

    if oper == 0:
        if q:
            v = heapq.heappop(q)
            if v[1] == 0:
                print(v[0] * -1)
            else:
                print(v[0])
        else:
            print(0)
    else:
        if oper < 0:
            heapq.heappush(q, (oper * -1, 0))
        else:
            heapq.heappush(q, (oper, 1))
    n -= 1
