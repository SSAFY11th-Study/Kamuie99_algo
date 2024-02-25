# import sys
# sys.stdin = open('input.txt')
#                                 # 9
def change(W, on_off):
    if on_off[W] == 1:
        on_off[W] = 0
    else:
        on_off[W] = 1
    return on_off

def switch_on_off(S, W, on_off, N):
    if S == 1:
        for i in range(W, N, W):
            change(i, on_off)
    elif S == 2:
        change(W, on_off)
        
        change_list = []
        
        for i in range(1, W+1):
            if 0 < W-i and W+i < N and on_off[W-i] == on_off[W+i]:
                change_list.append(W-i)
                change_list.append(W+i)
            else:
                break
        
        for c in change_list:
            change(c, on_off)
    
    return on_off

N = int(input())

on_off = list(map(int, input().split()))

on_off = [0] + on_off

student_num = int(input())

for i in range(student_num):
    S, W = map(int, input().split())
    on_off = switch_on_off(S, W, on_off, N+1)

count = 0
for i in range(1, N+1):
    print(on_off[i], end = ' ')
    count += 1
    if count == 20:
        print()
        count = 0