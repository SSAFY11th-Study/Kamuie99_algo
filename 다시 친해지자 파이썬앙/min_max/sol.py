import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  field = list(map(int, input().split()))
  print(f'#{test_case} {max(field)-min(field)}')