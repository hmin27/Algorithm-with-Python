# 2024-03-21
# 그리디 알고리즘
# [1541] 잃어버린 괄호

# 최소가 되려면 - 값이 커야함
# - 뒤에 다른 -가 나오기 전까지 괄호
# 0으로 시작하는 숫자 처리

temp=[]

expression = list(input())
num_str = ''
expression_str = ''

for i in range(len(expression)):
    if expression[i] == '-':
        expression.insert(i+1, '(')

        for j in range(i+2, len(expression)):
            if expression[j] == '-':
                expression.insert(j, ')')
                break
            if j+1 == len(expression):
                expression.append(')')
        
for i in range(len(expression)):
    if expression[i] != '-' and expression[i] != '+' and expression[i] != '(' and expression[i] != ')':
        num_str += expression[i]
        if i == len(expression) -1:
            num_int = int(num_str)
            expression_str += str(num_int)
    else:
        if num_str != '':
            num_int = int(num_str)
            expression_str += str(num_int)
        expression_str += expression[i]

        num_str = ''


# print(expression_str)
print(eval(expression_str))
            
        