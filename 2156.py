# 2024-02-17
# 동적 계획법
# [2156] 포도주 시식

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

case_a, case_b, case_c = 0, 0, 0

for i in range(n):
    if i%3 == 0:
        case_a += arr[i]
        case_b += arr[i]
    if i%3 == 1:
        case_a += arr[i]
        case_c += arr[i]
    if i%3 == 2:
        case_b += arr[i]
        case_c += arr[i]

print(max(case_a, case_b, case_c))
