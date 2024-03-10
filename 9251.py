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


dp = [[ 0 for _ in range(len(max_seq)) ] for _ in range(len(min_seq)+1) ]  # (min_seq + 1) x max_seq

# 작은 시퀀스를 기준으로 겹치는 부분 수열 파악
# 작은 시퀀스를 0부터 끝까지 하나씩 가면서 겹치는 문자 있는지 확인
# 겹치는 문자가 있을 때 해당 문자 왼쪽으로 max에 +1해서 저장

for i, letter in enumerate(min_seq):

    for j in range(len(max_seq)):
        if letter == max_seq[j]:
            if j != 0:
                temp = max(dp[i][:j])
                dp[i+1][j] = max(temp+1, 1)
            else: 
                dp[i+1][j] = 1
        else: 
            dp[i+1][j] = dp[i][j]

print(max(dp[-1]))
            
        




