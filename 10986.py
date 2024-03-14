# 2024-03-14
# 누적 합
# [10986] 나머지 합

import sys
input = sys.stdin.readline

n, div = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [ 0 ]
count = 0

for i in range(n):
    prefix_sum.append( prefix_sum[i] + arr[i] )

for i in range(1, n):
    for j in range(i, n+1):
        result = prefix_sum[j] - prefix_sum[i-1]

        if(result % div == 0):
            count += 1
        

print(count)