import sys
sys.stdin = open('input.txt')

hex_to_bin = {hex(i)[2:].upper() : f'{i:04b}' for i in range(16)}


T = int(input())
for test_case in range(1, T+1):
  N, N16 = input().split()
  print(f'#{test_case}', end = ' ')
  for char in N16:
    print(f'{hex_to_bin[char]}', end = '')
  print()