# 2024-03-10
# 동적 계획법
# [9251] LCS

seq_a = list(input())
seq_b = list(input())

# 두 시퀀스의 길이 비교
min_seq = seq_a
max_seq = seq_b

if len(seq_a) > len(seq_b):
    min_seq = seq_b
    max_seq = seq_a


dp = [[ 0 for _ in range(len(max_seq)+1) ] for _ in range(len(min_seq)+1) ]  # (min_seq + 1) x (max_seq + 1)

for i, letter in enumerate(min_seq, start=1):

    for j in range(1, len(max_seq)+1):
        if letter == max_seq[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp)
print(dp[-1][-1])
            