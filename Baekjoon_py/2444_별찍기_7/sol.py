N = int(input())

for i in range(N-1, -1, -1):
    print(' ' * i, end = '')
    print('*' * (N-i), end = '')
    print('*' * (N-i-1))

for i in range(1, N):
    print(' ' * i, end = '')
    print('*' * (N-i), end = '')
    print('*' * (N-i-1))