# 2024-03-13
# 누적 합
# [16139] 인간-컴퓨터 상호작용

import sys
input = sys.stdin.readline

string = list(input())
string = string[:-1]

alphabets = [ [0]*26 for _ in range(len(string)+1) ]

for i, char in enumerate(string):
    alphabets[i+1] = alphabets[i][:]
    alphabets[i+1][ord(char) - 97] += 1

    
# print(alphabets)
    

repeat = int(input())

for i in range(repeat):
    target, start, end = input().split()
    start, end = int(start), int(end)
    # print(alphabets)

    result = alphabets[end+1][ord(target) - 97] - alphabets[start][ord(target) - 97]

    print(result)
