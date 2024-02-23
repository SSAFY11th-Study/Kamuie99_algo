N = int(input())

field = [[0] * 101 for i in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            field[x+i][y+j] = 1

result = 0
for f in field:
    result += sum(f)

print(result)