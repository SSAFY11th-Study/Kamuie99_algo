N = int(input())

field = [[0] * 1001 for i in range(1001)]


for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x1+x2):
        for k in range(y1, y1+y2):
            field[j][k] = i


for i in range(1, N+1):
    result = 0
    for f in field:
        result += f.count(i)
    print(result)