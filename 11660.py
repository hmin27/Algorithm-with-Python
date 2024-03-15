# 2024-03-15
# 누적 합
# [11660] 구간 합 구하기 5

import sys
input = sys.stdin.readline

n, repeat = map(int, input().split())
arr = []
prefix_sum = [ [0] * (n+1) for _ in range(n+1) ]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = arr[i-1][j-1] + prefix_sum[i][j-1]

for _ in range(repeat):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    
    for j in range(x1, x2+1):
        result += (prefix_sum[j][y2] - prefix_sum[j][y1-1])
    
    print(result)