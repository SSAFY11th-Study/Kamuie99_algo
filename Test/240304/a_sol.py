import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    field = []

    for i in range(N):
        field.append(list(map(int, input().split())))


    # 한 개

    charge_x = None
    charge_y = None

    l = len(field)

    xys = []

    for x in range(-15, 16):
        for y in range(-15, 16):
            xys.append((x, y))

    results = []
    for x, y in xys:
        count = l
        for xh, yh, d in field:
            if abs(xh - x) + abs(yh - y) <= d:
                count -= 1
        result = 0
        if count == 0:
            for xh, yh, d in field:
                result += abs(xh - x) + abs(yh - y)
            results.append(result)

    if results:
        print(f'#{test_case} {min(results)}')
