import sys
sys.stdin = open('input.txt')

def check(height, idx):
  global tmp, B
  if height >= B:
    tmp = min(tmp, height)
    return
  for i in range(idx, N):
    check(height + field[i], i + 1)

T = int(input())
for test_case in range(1, T+1):
  N, B = map(int ,input().split())
  field = list(map(int ,input().split()))
  tmp = 20 * 10000 + 1
  check(0, 0)
  print(f'#{test_case} {tmp - B}')