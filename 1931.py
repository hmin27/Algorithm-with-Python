# 2024-03-20
# 그리디 알고리즘
# [1931] 회의실 배정

import sys
input = sys.stdin.readline
schedules = []
total = 0
flag = True

n = int(input())
for _ in range(n):
    schedule = tuple(map(int, input().split()))
    schedules.append(schedule)

schedules.sort(key=lambda x: (x[1], x[0]))  # 빨리 끝나는 순으로, 같이 끝나면 일찍 시작하는 순으로 정렬
earliest = schedules[0]
total += 1

idx = 0
# 빠르고 짧은 회의만 택
for i in range(1, n):

    if schedules[i][0] >= earliest[1]:
        total += 1
        earliest = schedules[i]

print(total)

    




