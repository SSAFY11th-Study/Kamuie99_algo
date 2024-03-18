w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

go_p = 1
go_q = 1

for i in range(t):
    if p == w or 0 == p:
        go_p *= -1
    if q == h or 0 == q:
        go_q *= -1
    p, q = p + go_p, q + go_q
print(p, q)