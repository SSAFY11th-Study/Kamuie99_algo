import sys
sys.stdin = open('input.txt')

def boom(raw, col, N, M, field):
    n = field[raw][col]
    temp = n
    for i in range(1, n+1):
        dxy = [(-i, 0), (i, 0), (0, -i), (0, i)]
        for dx, dy in dxy:
            if 0 <= raw + dx < N and 0 <= col + dy < M:
                temp += field[raw+dx][col+dy]
    return temp


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for i in range(N)]
    
    results = []
    
    for i in range(N):
        for j in range(M):
            temp = boom(i, j, N, M, field)
            results.append(temp)
            
    print(f'#{test_case} {max(results)}')