import sys
sys.stdin = open('input.txt')

# que 사용을 위해 deque import
from collections import deque

def under_100(x):         # 100만 이하인지를 판단하는 함수
    return 0 < x <= 1000000

def bfs(n, c):
  que = deque([(n, c)])   # que에 n과 c=0 을 넣고
  visited = set()         # 이미 앞에 나왔던 수는 또 나올 필요 x 방문처리를 위해 집합 생성
  visited.add(n)          # n을 방문했다고 처리하고 while문 진입
  
  while que:
    n, c = que.popleft()  # n과 c(카운트) 값을 뽑아서

    if n == M:            # 만약 n이 만들고 싶은 자연수 M이 되었다면
      return c            # c(카운트) 값 출력
    
    yunsan = {n*2, n+1, n-1, n-10}
    
    for y in yunsan:
      if y not in visited and under_100(y):   # 만약 n에 2를 곱한 수가 방문하지 않은 수이고 100만 이하라면
        que.append((y, c+1))                    # 연산하고, 결과값과 연산 회수를 다시 que에 추가
        visited.add(y)                          # 해당 결과 값도 방문처리

T = int(input())
for test_case in range(1, T+1):
  N, M = map(int, input().split())
  print(f'#{test_case} {bfs(N, 0)}')  # 함수에 N 값과 카운트에 쓸 c에 0 전달