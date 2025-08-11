import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip())

while t > 0:
    k = int(input().rstrip())
    pq = []
    while k > 0:
        oper = input().rstrip().split()
        if oper[0] == "I":
            heapq.heappush(pq, int(oper[1]))
        else:
            if not pq:
                k -= 1
                continue

            if oper[1] == "1":
                pq.sort()
                pq.pop()
            else:
                heapq.heappop(pq)
        k -= 1

    if not pq:
        print("EMPTY")
    else:
        print(f"{pq[-1]} {pq[0]}")

    t -= 1
