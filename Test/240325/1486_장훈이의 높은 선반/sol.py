import sys
sys.stdin = open('input.txt')

def check(height, idx):
  global tmp, B
  if height >= B: # 만약 현재까지 계산한 높이가 탑 높이보다 크거나 같다면
    tmp = min(tmp, height)  # tmp 값과 height 중 작은 값을 tmp에 새로 저장
    return  # 백트래킹
  for i in range(idx, N):
    check(height+field[i], i+1)

T = int(input())
for test_case in range(1, T+1):
  N, B = map(int, input().split())
  field = list(map(int, input().split()))
  tmp = 200001  # 점원 최대 20명, 인당 최대 키 10,000 20 * 10,000 + 1 = 200,001
  check(0, 0)
  print(f'#{test_case} {tmp - B}')  # 출력 해야 되는 값은 만든 키 높이 - 탑 높이