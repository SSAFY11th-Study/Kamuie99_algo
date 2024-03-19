def dfs(product):
    global total, min_sum

    if product == N:
        if total > min_sum:
            total = min_sum
        return

    if total <= min_sum:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            min_sum += lst[product][i]
            dfs(product + 1)
            visited[i] = 0
            min_sum -= lst[product][i]


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = 0
    total = 987654321

    dfs(0)
    print(f'#{test_case} {total}')