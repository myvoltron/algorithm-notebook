# Python Cheatsheet

코딩 테스트에서 자주 쓰는 파이썬 문법과 표준 라이브러리 정리입니다.

## 빠른 입력

```python
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
arr = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
chars = [list(input().strip()) for _ in range(n)]
```

## 출력

```python
print(answer)
print(*arr)
print("\n".join(map(str, arr)))
```

## 정렬

```python
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x: (x[0], -x[1]))

sorted_arr = sorted(arr)
```

## Counter, defaultdict

```python
from collections import Counter, defaultdict

counter = Counter(arr)
print(counter[3])

graph = defaultdict(list)
graph[a].append(b)
```

## deque

```python
from collections import deque

q = deque()
q.append(1)
q.appendleft(0)
q.popleft()
q.pop()
```

## heapq

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
smallest = heapq.heappop(heap)

# 최대 힙
heapq.heappush(heap, -value)
value = -heapq.heappop(heap)
```

## bisect

```python
from bisect import bisect_left, bisect_right

left = bisect_left(arr, x)
right = bisect_right(arr, x)
count = right - left
```

## itertools

```python
from itertools import combinations, permutations, product

for case in combinations(arr, 2):
    pass

for case in permutations(arr, 3):
    pass

for case in product([0, 1], repeat=3):
    pass
```

## math

```python
import math

math.gcd(a, b)
math.lcm(a, b)
math.ceil(a / b)
math.isqrt(n)
```

## 큰 수와 무한대

```python
INF = 10**18
INF_FLOAT = float("inf")
```

정수 비교만 필요하면 `10**18`처럼 충분히 큰 정수를 쓰는 편이 안정적이다.

## 문자열

```python
s = input().strip()
reversed_s = s[::-1]

parts = s.split()
joined = "".join(parts)

if s.startswith("abc"):
    pass

if s.endswith("xyz"):
    pass
```

## 리스트 초기화

```python
arr = [0] * n
grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
```

2차원 배열은 `[[0] * m] * n`으로 만들면 같은 리스트를 공유하므로 피한다.

## 인덱스와 순회

```python
for i, value in enumerate(arr):
    pass

for i in range(n - 1, -1, -1):
    pass

for a, b in zip(arr, arr[1:]):
    pass
```

## 비트 연산

```python
mask = 0
mask |= 1 << i
mask &= ~(1 << i)
exists = mask & (1 << i)

for i in range(n):
    if mask & (1 << i):
        pass
```

## 재귀

```python
import sys

sys.setrecursionlimit(10**6)
```

재귀 깊이가 입력 크기만큼 커질 수 있으면 제한을 올리거나 반복문으로 바꾼다.

## 자주 하는 실수

- `input()`으로 받은 문자열 끝의 개행을 제거하지 않아 비교가 틀리는 경우.
- 2차원 리스트를 곱셈으로 초기화해서 모든 행이 같이 바뀌는 경우.
- `heapq`는 최소 힙이라는 점을 잊고 최대 힙을 그대로 구현하는 경우.
- 정렬 기준에서 오름차순/내림차순이 섞이는 경우.
- 여러 테스트 케이스에서 `visited`, `graph`, `dp`를 재사용하는 경우.
