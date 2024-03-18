import sys
sys.stdin = open('input.txt')

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

field.sort(key=lambda x:x[0]) 

max_num = 0
max_idx = 0
for i in range(len(field)):
    if field[i][1] > max_num:
        max_num = field[i][1]
        max_idx = i

result = 0
stack = []
for i in range(max_idx+1):
    if stack:
        if field[i][1] > stack[-1][1]:
            temp = stack.pop()
            result += temp[1] * (field[i][0] - temp[0])
            stack.append(field[i])
    else:
        stack.append(field[i])


stack = []
for j in range(len(field)-1, max_idx, -1):
    if stack:
        if field[j][1] > stack[-1][1]:
            temp = stack.pop()
            result += temp[1] * (temp[0] - field[j][0])
            stack.append(field[j])
    else:
        stack.append(field[j])

if stack:
    result += (stack[0][0] - field[max_idx][0]) * stack[0][1]



result += field[max_idx][1]

print(result)