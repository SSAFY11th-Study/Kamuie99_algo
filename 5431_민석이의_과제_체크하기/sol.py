import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    field = list(map(int, input().split()))
    students = []
    for i in range(1, N+1):
        students.append(i)
    result = []
    for s in students:
        if s not in field:
            result.append(s)
    print(f'#{test_case}', *result)