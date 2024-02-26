import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수 입력 받기
T = int(input())
# 테스트 케이스 횟수 만큼 반복하여 계산
for test_case in range(1, T+1):
    # N, M을 입력 받아 저장
    N, M = map(int, input().split())
    # 2차원 배열에 N 줄에 걸쳐 저장
    field = [list(map(int, input().split())) for i in range(N)]
    # N 크기의 가로줄과 세로줄이 있을 때, M 크기의 사각형은 N-M+1 개 들어갈 수 있다.
    A = N - M + 1
    # 각각의 네모의 합을 저장할 배열을 초기화
    results = []
    # 해당 2차원 배열을 순회하면서
    for i in range(A):
        for j in range(A):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += field[k+i][l+j]
            results.append(temp)
    # 해당 합들 중 최대값을 테스트 케이스 번호와 함께 출력
    print(f'#{test_case} {max(results)}')