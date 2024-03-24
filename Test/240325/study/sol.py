# 장훈이의 높은 선반
# def check(height, idx):
#   global tmp, B
#   if height >= B:
#     tmp = min(height, tmp)
#     return
#   for i in range(idx, N):
#     check(height + field[i], i+1)

# T = int(input())
# for test_case in range(1, T+1):
#   N, B = map(int ,input().split())
#   field = list(map(int ,input().split()))
#   tmp = 10 * 20000 + 1
#   check(0, 0)
#   print(f'#{test_case} {tmp-B}')
  
# 이진수

# hex_to_bin = {hex(i)[2:].upper() : f'{i:04b}' for i in range(16)}

# T = int(input())

# for test_case in range(1, T+1):
#   N, N16 = input().split()
#   print(f'#{test_case}', end=' ')
#   for char in N16:
#     print(f'{hex_to_bin[char]}', end='')
#   print()

# 장훈이의 높은 선반

# def check(height, idx):
#   global tmp, B
#   if height >= B:
#     tmp = min(height, tmp)
#     return
#   for i in range(idx, N):
#     check(height + field[i], i+1)


# T = int(input())
# for test_case in range(1, T+1):
#   N, B = map(int ,input().split())
#   field = list(map(int ,input().split()))
#   tmp = 10 * 20000 + 1
#   check(0, 0)
#   print(f'#{test_case} {tmp - B}')

# 이진수

hex_to_binary = {hex(i)[2:].upper() : f'{i:04b}' for i in range(16)}
