# 2024-03-14
# 누적 합
# [10986] 나머지 합

import sys
import math
input = sys.stdin.readline

n, div = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [ 0 ]  # 0~n
remain = [ 0 for _ in range(div) ] # 0~div-1
remain[0] = 1
count = 0
total = 0

for i in range(n):
    add = prefix_sum[i] + arr[i]
    prefix_sum.append(add)
    remain[add % div] += 1


for i in range(div):
    total += math.comb(remain[i], 2)

print(total)
