import sys
input = sys.stdin.readline

col, raw = map(int, input().split())

raw_arr = [0, raw]

col_arr = [0, col]

N = int(input())

for i in range(N):
    garo_sero, where = map(int, input().split())
    # 가로로 자르는 점선
    if garo_sero == 0:
        raw_arr.append(where)
    # 세로로 자르는 점선
    elif garo_sero == 1:
        col_arr.append(where)

raw_arr.sort()
col_arr.sort()

max_raw = 0
for i in range(len(raw_arr)-1):
    temp = raw_arr[i+1] - raw_arr[i]
    if max_raw < temp:
        max_raw = temp

max_col = 0
for j in range(len(col_arr)-1):
    temp = col_arr[j+1] - col_arr[j]
    if max_col < temp:
        max_col = temp

print(max_raw * max_col)