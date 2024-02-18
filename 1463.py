# 2024-02-18
# 동적 계획법
# [1463] 1로 만들기

n = int(input())
dp = [ 0 for _ in range(n+1) ]
dp[0] = 1000000

if n > 1:
    dp[2] = 1
if n > 2:
    dp[3] = 1

for i in range(4, n+1):
    div3, div2 = 0, 0
    if i%3 == 0:
        div3 = i // 3
    if i%2 == 0:
        div2 = i // 2
    
    dp[i] = min(dp[div3]+1, dp[div2]+1, dp[i-1]+1)

print(dp[n])