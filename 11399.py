# 2024-03-21
# 그리디 알고리즘
# [11399] ATM

import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
times = [0]

people.sort()

for i in range(1, n+1):
    times.append(times[i-1] + people[i-1])

print(sum(times))
