# 2024-02-18
# 동적 계획법
# [2565] 전깃줄

n = int(input())
arr = []

for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

arr.sort()

dp = [ 1 for _ in range(n) ]

for i in range(n):
    temp = 0
    for j in range(0, i):
        if arr[j][1] < arr[i][1]: 
            temp = dp[j] + 1
        if temp > dp[i]: 
            dp[i] = temp

print(n - max(dp))