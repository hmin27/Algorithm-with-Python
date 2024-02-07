# 2024-02-08
# 동적 계획법
# [1932] 정수 삼각형

import sys

total = []
arr = []

# 마지막 행부터 최댓값 저장
def calculate_cost(row):
    global total

    for i in range(row-2, -1, -1):  # n-2~0행
        temp = [ 0 for _ in range(i+1) ]
        for j in range(i+1):
            maximum = max(arr[i][j]+total[j], arr[i][j]+total[j+1])
            temp[j] = maximum

        total = temp


if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    total = arr[n-1]
    
    calculate_cost(n)
    print(total[0])
    