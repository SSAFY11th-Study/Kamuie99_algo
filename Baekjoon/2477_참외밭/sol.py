import sys
sys.stdin = open('input.txt')

K = int(input())
            #1  2  3  4
field = [[], [],[],[],[]]


for _ in range(6):
    D, N = map(int, input().split())
    field[D].append(N)
    
big_temp = []
small_temp = []
for f in field:
    if len(f) == 1:
        big_temp.append(f[0])
    elif len(f) == 2:
        small_temp.append(min(f))

result_1 = big_temp[0]*big_temp[1]

result_2 = small_temp[0]*small_temp[1]

print((result_1 - result_2) * K)