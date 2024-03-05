import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr_1 = [list(map(int, input().split())) for _ in range(N)]
arr_2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(arr_1[i][j] + arr_2[i][j], end =' ')
    print()