import sys
sys.stdin = open('input.txt')

# 연결 요소
def dfs(v):
    visited[v] = 1          # 방문 표시

    for nxt in graph[v]:    # 정점에서 연결된 정점들 순회
        if visited[nxt]:    # 방문하지 않는 정점들을 선택
            continue
        dfs(nxt)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    input_arr = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]  # 1번부터 n번까지

    for i in range(M):     # 무방향 그래프 연결 상태
        v1 = input_arr[i * 2]
        v2 = input_arr[i * 2 + 1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0 for _ in range(N + 1)]
    count = 0

    for i in range(1, N + 1):
        if visited[i]:  # 방문 확인
            continue
        dfs(i)      # 연결 요소를 다 방문 표시
        count += 1    # 연결 요소의 개수 + 1

    print(f'#{test_case} {count}')