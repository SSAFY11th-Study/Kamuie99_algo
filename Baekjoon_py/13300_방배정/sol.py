# import sys
# sys.stdin = open('input.txt')

N, K = map(int, input().split())

#학년   1  2  3  4  5  6
F = [0, 0, 0, 0, 0, 0, 0]
M = [0, 0, 0, 0, 0, 0, 0]


for i in range(N):
    S, Y = map(int, input().split())
    # 여학생
    if S == 0:
        F[Y] += 1
    # 남학생
    elif S == 1:
        M[Y] += 1
    
FM = F + M

count = 0
for fm in FM:
    if fm !=0 and fm<=K:
        count += 1
    elif fm > K:
        if fm % K == 0:
            count += (fm // K)
        else:
            count += (fm // K+1)

print(count)
