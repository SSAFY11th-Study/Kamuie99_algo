import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M1, M2 = map(int, input().split())
    field = list(map(int, input().split()))

    field.sort(reverse=True)

    A1 = []
    A2 = []

    for i in range(N):
        if len(A1) < M1 and len(A2) < M2:
            if i % 2 == 0:
                A1.append(field[i])
            else:
                A2.append(field[i])
        elif len(A1) >= M1:
            A2.append(field[i])
        elif len(A2) >= M2:
            A1.append(field[i])

    A1_result = 0
    A2_result = 0

    count = 1
    for a in A1:
        A1_result += a * count
        count += 1

    count = 1
    for a in A2:
        A2_result += a * count
        count += 1

    print(f'#{test_case} {A1_result+A2_result}')