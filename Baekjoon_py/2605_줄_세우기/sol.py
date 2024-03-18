N = int(input())

cards = list(map(int, input().split()))

field = [1]

temp = []
for i in range(1, len(cards)):
    for j in range(cards[i]):
        t = field.pop()
        temp.append(t)
    field.append(i+1)
    while temp:
        l = temp.pop()
        field.append(l)

print(*field)