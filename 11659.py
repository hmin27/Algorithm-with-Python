# 2024-03-10
# 누적 합
# [11659] 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]

for i in range(1, n+1):
    prefix_sum.append(arr[i-1] + prefix_sum[i-1])

# print(prefix_sum)

for _ in range(m):
    start, end = map(int, input().split())
    
    ans = prefix_sum[end] - prefix_sum[start-1]
    print(ans)