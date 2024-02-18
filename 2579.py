# 2024-02-18
# 동적 계획법
# [2579] 계단 오르기

n = int(input())
stairs = [0]

for i in range(n):
    stairs.append(int(input()))

dp = [ 0 for _ in range(n+1) ]
dp[1] = stairs[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-3]+stairs[i]+stairs[i-1], dp[i-2]+stairs[i])

print(dp[n])
