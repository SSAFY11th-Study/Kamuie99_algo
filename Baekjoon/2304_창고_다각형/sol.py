import sys
sys.stdin = open('input.txt')

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

field.sort(key=lambda x:x[0]) 

prev = 0
result = 0

stack = []
small = []
for f in field:
    if f != field[-1]:
        if stack:
            if f[1] > stack[-1][1]:
                temp = stack.pop()
                result += temp[1] * (f[0] - temp[0])
                stack.append(f)
            else:
                small.append(f[1])
        else:
            stack.append(f)
    if f == field[-1]:
        if f[1] > stack[-1][1]:
                temp = stack.pop()
                result += temp[1] * (f[0] - temp[0])
        elif f[1] < stack[-1][1]:
            temp = stack.pop()
            small.append(f[1])
            result += temp[1] 
            result += (f[0] - temp[0]) * max(small)
            
print(result)