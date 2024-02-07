# 2024-02-07
# 동적 계획법
# [1149] RGB거리

import sys

total = [ 0 for _ in range(3) ]
arr = []

# 마지막 행부터 최소값 저장
def calculate_cost(row):
    global total
    total = arr[row-1]

    for i in range(row-2, -1, -1):  # n-2~0행
        temp = [ 0 for _ in range(3) ]
        for j in range(3):
            if j == 0:
                minimum = min(arr[i][j]+total[1], arr[i][j]+total[2])
            elif j == 1:
                minimum = min(arr[i][j]+total[0], arr[i][j]+total[2])
            else: 
                minimum = min(arr[i][j]+total[0], arr[i][j]+total[1])

            temp[j] = minimum

        total = temp


if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    calculate_cost(n)
    result = min(total)
    print(result)
    
    