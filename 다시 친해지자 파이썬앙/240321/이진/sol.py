import sys
sys.stdin = open('input.txt')

def binary_search(L, R, T, direction):
  global cnt
  
  mid = (L + R) // 2
  
  if T == A[mid]:
    cnt += 1
    return

  elif T > A[mid]:
    if direction == 'RIGHT':
      return
    binary_search(mid+1, R, T, 'RIGHT')
  
  elif T < A[mid]:
    if direction == 'LEFT':
      return
    binary_search(L, mid-1, T, 'LEFT')

T = int(input())
for test_case in range(1, T+1):
  N, M = map(int, input().split())
  A = sorted(list(map(int, input().split())))
  B = list(map(int, input().split()))

  cnt = 0   # 최종 결과
  
  for b in B:
    binary_search(0, N-1, b, 'START')
    
  print(test_case, cnt)