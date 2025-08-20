import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip())

while t > 0:
    k = int(input().rstrip())
    max_heap = []
    min_heap = []
    visited = [False] * k

    for i in range(k):
        oper = input().rstrip().split()
        if oper[0] == "I":
            v = int(oper[1])
            heapq.heappush(max_heap, (v * -1, i))
            heapq.heappush(min_heap, (v, i))
            visited[i] = True
        else:
            if oper[1] == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    v = heapq.heappop(max_heap)
                    visited[v[1]] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    v = heapq.heappop(min_heap)
                    visited[v[1]] = False

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not max_heap and not min_heap:
        print("EMPTY")
    else:
        print(f"{max_heap[0][0] * -1} {min_heap[0][0]}")
    t -= 1
