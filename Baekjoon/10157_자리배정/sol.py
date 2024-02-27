import sys
sys.stdin = open('input.txt')


x, y = map(int, input().split())

p = int(input())

if p > x*y:
    print(0)
    exit()

field = [[0] * (y+1) for _ in range(x+1)]
r = c = 1
d = 0
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                # 7*6+1 = 43
for i in range(1, x*y+1):
    if i == p:
        print(r, c)
        break
    else:
        field[r][c] = i
        
        r += drc[d][0]
        c += drc[d][1]
        
        if r < 1 or c < 1 or r > x or c > y or field[r][c]:
            r -= drc[d][0]
            c -= drc[d][1]
            
            d = (d+1)%4
            r += drc[d][0]
            c += drc[d][1]