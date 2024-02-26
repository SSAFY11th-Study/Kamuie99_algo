# 총을 쐈을 때를 나타내는 함수
def boom(i, j, field, N):
    # tmp는 현재 맞힌 칸의 점수를 저장한 변수
    tmp = field[i][j]
    # 상하좌우로 두칸씩 총 8칸을 나타내는 델타 탐색
    for k in range(1, 3):
        # dxy는 상하좌우 한칸, k가 2가 되면 상하좌우 두칸이 된다.
        dxy = [(-k, 0), (k, 0), (0, -k), (0, k)]
        # 해당 dxy 값들을 사용하여
        for dx, dy in dxy:
            # 만약 인덱스를 벗어나지 않는다면
            if 0 <= i + dx < N and 0 <= j + dy < N:
                # tmp에 해당 좌표의 값도 추가한다.
                tmp += field[i+dx][j+dy]
    return tmp  # tmp 값을 리턴한다.


# 첫줄에 테스트케이스 개수 T가 주어진다. (1 <= T <= 10)
T = int(input())
# 이어 각 테스트 케이스별로
for test_case in range(1, T+1):
    # 첫줄에 N
    N = int(input())
    # 이어 N개의 줄에 칸 칸의 점수 Aij가 N개씩 주어진다. 그것을 2차원 배열로 저장한다.
    field = [list(map(int, input().split())) for i in range(N)]
    # 결과 값을 담을 result 변수를 초기화 해주고
    result = 0
    # 2차원 배열을 순회하면서
    for i in range(N):
        for j in range(N):
            # boom 함수를 실행한 결과값을 temp 변수에 저장하여
            temp = boom(i, j, field, N)
            # temp가 result 보다 크다면
            if temp > result:
                # temp가 새로운 최대값이 된다.
                result = temp
    # 결과값을 테스트 케이스 번호와 함께 출력한다.
    print(f'#{test_case} {result}')