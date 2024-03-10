# 2024-03-10
# 동적 계획법
# [12865] 평범한 배낭

import sys

n, k = map(int, input().split())
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# dp = [[ 0 for _ in range(k+1) ] for _ in range(n)]
dp = [ 0 for _ in range(k+1) ]

for item in items:
    w, v = item 
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w]+v)

print(dp[-1])


        
    
