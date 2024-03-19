# 2024-03-19
# 그리디 알고리즘
# [11047] 동전 0

import sys
input = sys.stdin.readline 

coins = []
total = 0

n, k = map(int, input().split())
for _ in range(n):
    coins.append(int(input()))

for i in range(len(coins)-1, -1, -1):
    if k // coins[i] > 0:
        num = k // coins[i] 
        k -= coins[i] * num 
        # print(f"{coins[i]} * {num}, left: {k}")
    
        total += num 
    else: 
        continue 

print(total)

