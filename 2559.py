# 2024-03-12
# 누적 합
# [2559] 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

prefix_sum = [0]

for i in range(1, 1+n):
    prefix_sum.append(temperature[i-1] + prefix_sum[i-1])

max = -10000000

for i in range(0, n-k+1):
    temp = prefix_sum[k+i] - prefix_sum[i]

    if temp > max:
        max = temp 

print(max)