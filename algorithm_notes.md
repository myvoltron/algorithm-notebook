# Algorithm Notes

코딩 테스트에서 자주 만나는 알고리즘 유형과 바로 복사해서 쓸 수 있는 파이썬 템플릿을 한곳에 모은 문서입니다.

## 기본 입출력

BOJ에서는 보통 `sys.stdin.readline`을 사용한다. 여러 줄 출력은 리스트에 모아 `"\n".join(...)`으로 출력하면 빠르다.

```python
import sys

input = sys.stdin.readline


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        pass

    print(arr)


if __name__ == "__main__":
    main()
```

## 그래프

### BFS

- 최단 거리가 간선 수 기준이고 모든 간선 비용이 같을 때 사용한다.
- 격자 최단 거리, 최소 이동 횟수, 레벨 탐색에 잘 맞는다.
- `deque`를 사용하고, 큐에 넣는 순간 방문 처리한다.

```python
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(grid, start_x, start_y):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    return visited


n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

visited = bfs(grid, 0, 0)
print(visited[n - 1][m - 1])
```

### DFS

- 연결 요소 탐색, 사이클 확인, 백트래킹, 트리 순회에 자주 쓴다.
- 재귀 DFS는 `sys.setrecursionlimit`을 확인한다.
- 깊이가 매우 깊으면 반복문 스택 DFS가 더 안전하다.

```python
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        dfs(next_node)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(1)

print(visited)
```

### Dijkstra

- 음수 간선이 없는 그래프의 단일 시작점 최단 경로.
- `heapq`를 쓰고, 이미 더 짧은 거리로 처리된 노드는 건너뛴다.
- 여러 목적지를 비교해야 하면 한 번 구한 `distance` 배열을 재사용한다.

```python
import sys
import heapq

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance


n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

distance = dijkstra(start)

for i in range(1, n + 1):
    print("INF" if distance[i] == INF else distance[i])
```

### Floyd-Warshall

- 모든 정점 쌍 최단 경로.
- `O(n^3)`이라 보통 `n <= 500` 정도에서 고려한다.
- 경유지 `k`를 가장 바깥 반복문에 둔다.

```python
import sys

input = sys.stdin.readline
INF = 10**18

n = int(input())
m = int(input())
distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    distance[a][b] = min(distance[a][b], cost)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if distance[i][j] == INF else distance[i][j], end=" ")
    print()
```

### Bellman-Ford

- 음수 간선 또는 음수 사이클 판별이 필요할 때 사용한다.
- `n - 1`번 완화 후 한 번 더 완화되면 음수 사이클이 있다.
- 시간 복잡도는 `O(VE)`라 입력 크기를 꼭 확인한다.

```python
import sys

input = sys.stdin.readline
INF = 10**18


def bellman_ford(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    for i in range(n):
        for a, b, cost in edges:
            if distance[a] == INF:
                continue
            if distance[b] > distance[a] + cost:
                distance[b] = distance[a] + cost
                if i == n - 1:
                    return None

    return distance


n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))

distance = bellman_ford(1)
print(-1 if distance is None else distance[1:])
```

### Topological Sort

- 방향 비순환 그래프(DAG)의 선후 관계 정렬.
- 선수 과목, 작업 순서, 빌드 순서 문제에 잘 맞는다.
- 진입 차수가 0인 노드를 큐에 넣고 하나씩 제거한다.

```python
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)

    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)

print(*result)
```

### Union-Find

- 집합 연결 여부를 빠르게 확인할 때 사용한다.
- 사이클 판별, MST, 네트워크 연결 문제에 자주 나온다.
- 경로 압축을 반드시 넣는다.

```python
import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

print(parent)
```

### Minimum Spanning Tree

- 모든 노드를 최소 비용으로 연결할 때 사용한다.
- 크루스칼: 간선을 비용순 정렬한 뒤 Union-Find로 사이클을 피한다.
- 프림: 특정 시작점에서 힙으로 가장 싼 간선을 확장한다.

```python
import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
answer = 0

for cost, a, b in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += cost

print(answer)
```

## 탐색과 최적화

### Binary Search

- 정렬된 배열에서 값/위치 찾기.
- 또는 "정답 후보"에 대해 가능/불가능 판정이 단조적일 때 사용한다.
- `can(mid)`가 True일 때 왼쪽/오른쪽 중 어느 방향으로 갈지 먼저 정한다.

```python
import sys

input = sys.stdin.readline


def can(value):
    # value가 조건을 만족하면 True, 아니면 False
    return True


left = 0
right = 10**9
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
```

### Two Pointers

- 정렬 배열의 두 수 합, 연속 부분합, 중복 제거류 문제에 자주 쓴다.
- 왼쪽/오른쪽 포인터가 한 방향으로만 움직이면 `O(n)`이 된다.

```python
import sys

input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
current = 0
answer = 0

for right in range(n):
    current += arr[right]

    while current > target and left <= right:
        current -= arr[left]
        left += 1

    if current == target:
        answer += 1

print(answer)
```

### Sliding Window

- 연속 구간을 유지하며 합, 개수, 빈도 조건을 갱신한다.
- 고정 길이 윈도우는 더하고 빼는 위치가 명확하다.
- 가변 길이 윈도우는 조건을 만족할 때까지 오른쪽 확장, 깨질 때 왼쪽 축소를 반복한다.

```python
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

current = sum(arr[:k])
answer = current

for right in range(k, n):
    current += arr[right]
    current -= arr[right - k]
    answer = max(answer, current)

print(answer)
```

### Backtracking

- 모든 경우를 보되, 불가능한 후보는 일찍 가지치기한다.
- 순열, 조합, N-Queen, 스도쿠 같은 문제에 많이 쓰인다.
- `path`, `visited`, 현재 깊이, 남은 후보를 명확히 둔다.

```python
import sys

input = sys.stdin.readline


def backtrack(depth):
    if depth == m:
        print(*path)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        path.append(i)
        backtrack(depth + 1)
        path.pop()
        visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n + 1)
path = []

backtrack(0)
```

### Bitmask

- 작은 집합의 포함 여부를 정수 하나로 표현할 때 사용한다.
- 부분집합 탐색, 방문 상태 DP, 조합 상태 저장에 자주 쓴다.
- `1 << i`는 i번째 원소를 뜻한다.

```python
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 모든 부분집합 탐색
for mask in range(1 << n):
    subset = []

    for i in range(n):
        if mask & (1 << i):
            subset.append(arr[i])

    print(subset)

# 원소 추가/삭제/확인
mask = 0
i = 2

mask |= 1 << i
mask &= ~(1 << i)
exists = bool(mask & (1 << i))

print(exists)
```

## 동적 계획법

### 1D/2D DP

- 현재 답이 이전 작은 문제의 답으로 표현될 때 사용한다.
- 상태 정의가 제일 중요하다: `dp[i]` 또는 `dp[i][j]`가 정확히 무엇인지 한 문장으로 적어본다.
- 초기값과 점화식의 인덱스 범위를 먼저 확인한다.

```python
import sys

input = sys.stdin.readline

# 1차원 DP
n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1]

print(dp[n])

# 2차원 DP
n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
```

### Knapsack

- 무게/비용 제한 안에서 최대 가치 선택.
- 0/1 배낭은 뒤에서 앞으로 갱신하면 1차원 DP로 줄일 수 있다.
- 같은 물건을 여러 번 쓸 수 있으면 앞에서 뒤로 갱신한다.

```python
import sys

input = sys.stdin.readline

n, capacity = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (capacity + 1)

for weight, value in items:
    for current in range(capacity, weight - 1, -1):
        dp[current] = max(dp[current], dp[current - weight] + value)

print(dp[capacity])
```

### LIS

- 가장 긴 증가하는 부분 수열.
- `O(n^2)` DP 또는 `bisect_left`를 쓰는 `O(n log n)` 방식이 있다.
- 실제 수열 복원이 필요한지, 길이만 필요한지 구분한다.

```python
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = []

for value in arr:
    index = bisect_left(lis, value)
    if index == len(lis):
        lis.append(value)
    else:
        lis[index] = value

print(len(lis))
```

### Prefix Sum

- 구간 합을 여러 번 빠르게 구할 때 사용한다.
- 1차원은 `prefix[right] - prefix[left - 1]`.
- 2차원은 더한 사각형에서 위쪽/왼쪽을 빼고 겹친 영역을 다시 더한다.

```python
import sys

input = sys.stdin.readline

# 1차원 누적합
n, q = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

for _ in range(q):
    left, right = map(int, input().split())
    print(prefix[right] - prefix[left - 1])

# 2차원 누적합
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = (
            prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
            + board[i - 1][j - 1]
        )

x1, y1, x2, y2 = map(int, input().split())
answer = (
    prefix[x2][y2]
    - prefix[x1 - 1][y2]
    - prefix[x2][y1 - 1]
    + prefix[x1 - 1][y1 - 1]
)
print(answer)
```

## 문자열

### Stack String

- 폭발 문자열, 괄호 검사, 인접 중복 제거에 자주 쓴다.
- 오른쪽에 하나씩 넣으면서 끝부분만 검사하면 효율적이다.

```python
import sys

input = sys.stdin.readline

s = input().strip()
target = input().strip()
stack = []
length = len(target)

for ch in s:
    stack.append(ch)

    if len(stack) >= length and "".join(stack[-length:]) == target:
        for _ in range(length):
            stack.pop()

print("".join(stack) if stack else "FRULA")
```

### KMP

- 긴 문자열에서 패턴을 빠르게 찾는다.
- 실패 함수(prefix table)를 만들고, 불일치 시 비교 위치를 되돌리지 않는다.
- 보통 문자열 길이가 매우 클 때 고려한다.

```python
import sys

input = sys.stdin.readline


def build_table(pattern):
    table = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def kmp(text, pattern):
    table = build_table(pattern)
    result = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 1)
                j = table[j]
            else:
                j += 1

    return result


text = input().strip()
pattern = input().strip()
print(kmp(text, pattern))
```

### Trie

- 문자열 집합의 접두사 검색.
- 전화번호 목록, 자동완성, 사전 문제에 나온다.
- 노드마다 다음 문자 딕셔너리와 종료 표시를 둔다.

```python
import sys

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


trie = Trie()
n = int(input())

for _ in range(n):
    trie.insert(input().strip())

print(trie.starts_with(input().strip()))
```

## 수학

### GCD/LCM

- 최대공약수는 `math.gcd`.
- 최소공배수는 `a * b // gcd(a, b)`.

```python
import math

a, b = map(int, input().split())
gcd = math.gcd(a, b)
lcm = a * b // gcd

print(gcd, lcm)
```

### Prime/Sieve

- 소수 판별은 `sqrt(n)`까지만 나눠본다.
- 여러 수의 소수 여부가 필요하면 에라토스테네스의 체를 쓴다.

```python
import sys

input = sys.stdin.readline

n = int(input())
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * i, n + 1, i):
        is_prime[j] = False

print([i for i in range(2, n + 1) if is_prime[i]])
```

### Modular Arithmetic

- 나눗셈이 필요한 모듈러 연산은 모듈러 역원을 확인한다.
- 모듈러가 소수면 `pow(a, mod - 2, mod)`를 사용할 수 있다.
- 큰 거듭제곱은 `pow(a, b, mod)`를 사용한다.

```python
MOD = 1_000_000_007

a, b = map(int, input().split())
power = pow(a, b, MOD)
inverse = pow(a, MOD - 2, MOD)

print(power, inverse)
```

## 실전 체크리스트

- 입력 크기를 보고 `O(n)`, `O(n log n)`, `O(n^2)`, `O(n^3)` 중 가능한 범위를 먼저 가늠한다.
- 그래프가 방향인지 무방향인지 확인한다.
- 노드 번호가 0부터인지 1부터인지 확인한다.
- 최단 경로 문제에서 간선 가중치가 음수인지 확인한다.
- 정답이 커질 수 있으면 모듈러 또는 큰 정수 처리가 필요한지 확인한다.
- 여러 테스트 케이스에서는 전역 배열 초기화를 빼먹지 않는다.
