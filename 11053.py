# 2024-02-18
# 동적 계획법
# [11053] 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int, input().split()))

dp = [ 1 for _ in range(n) ]

for i in range(n):
    temp = 0
    for j in range(0, i):
        if arr[j] < arr[i]: 
            temp = dp[j] + 1
        if temp > dp[i]: 
            dp[i] = temp

print(max(dp))
    