# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right


def is_exist(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


n, x = map(int, input().split())

# 오름차순으로 정렬된 수열
sequence = list(map(int, input().split()))

if not is_exist(sequence, x):
    print(-1)
else:
    left_index = bisect_left(sequence, x)
    right_index = bisect_right(sequence, x)
    print(right_index - left_index)
