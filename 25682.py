# 2024-03-18
# 누적 합
# [25682] 체스판 다시 칠하기 2

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(input())[:-1])

# Black first
prefix_b_fst = [ [0] * (m+1) for _ in range(n+1) ]
# White first
prefix_w_fst = [ [0] * (m+1) for _ in range(n+1)]

for i in range(n):
    for idx, color in enumerate(board[i]):
        b_fst, w_fst = 0, 0
        
        if (i+idx) % 2 == 0:    # 0, 2, 4...
            if color == 'B':
                w_fst = 1
            else: 
                b_fst = 1
        else: 
            if color == 'B':
                b_fst = 1
            else: 
                w_fst = 1
        
        prefix_b_fst[i+1][idx+1] = b_fst + prefix_b_fst[i][idx+1] + prefix_b_fst[i+1][idx] - prefix_b_fst[i][idx]
        prefix_w_fst[i+1][idx+1] = w_fst + prefix_w_fst[i][idx+1] + prefix_w_fst[i+1][idx] - prefix_w_fst[i][idx]


minimum = sys.maxsize

for i in range(k, n+1):
    for j in range(k, m+1):
        result = min(prefix_b_fst[i][j] - prefix_b_fst[i-k][j] - prefix_b_fst[i][j-k] + prefix_b_fst[i-k][j-k],
                     prefix_w_fst[i][j] - prefix_w_fst[i-k][j] - prefix_w_fst[i][j-k] + prefix_w_fst[i-k][j-k])

        if minimum > result: 
            minimum = result

print(minimum)