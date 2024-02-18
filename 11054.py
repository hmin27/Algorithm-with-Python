# 2024-02-18
# 동적 계획법
# [11054] 가장 긴 바이토닉 부분 수열

n = int(input())
arr = list(map(int, input().split()))

dp = [ [ 1 for _ in range(n) ] for _ in range(3) ]

for i in range(1, n):
    temp = 0
    for j in range(0, i):
        if arr[j] < arr[i]: 
            temp = dp[0][j] + 1
        if temp > dp[0][i]: 
            dp[0][i] = temp
    
for i in range(n-1, -1, -1):
    temp = 0
    for j in range(n-1, i, -1):
        if arr[j] < arr[i]:
            temp = dp[1][j] + 1
        if temp > dp[1][i]:
            dp[1][i] = temp 

for i in range(n):
    dp[2][i] = dp[0][i] + dp[1][i] - 1

print(max(dp[2]))
    