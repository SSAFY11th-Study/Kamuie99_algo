def max_sum(idx, total):
    global result
    # 마지막 가로줄 까지 왔을 때
    if idx == N:
        # total이 result 보다 크다면
        if total > result:
            result = total  # 이제부턴 니가 최대값!
            return
        else:
            return  # 아니라면 다시 돌아가자

    for i in range(N):
        if i not in visited and field[idx][i] > 0:  # 방문하지 않았고, 음수가 아닐 때
            visited.append(i)   # 방문하고
            max_sum(idx+1, total + field[idx][i])   # 다음 줄 보러 가기
            visited.pop()   # 최대값이 아니었다면 백트래킹

# 테스트 케이스 수를 입력 받는다.
T = int(input())
for test_case in range(1, T+1): # 다음 줄부터 각 단계별로
    # 표적의 가로, 세로 개수 N이 주어진다.
    N = int(input())
    # 이차원 배열에 표적 정보를 저장한다.
    field = [list(map(int, input().split())) for i in range(N)]
    # 초기 최대값은 -50으로 한다, 음수 하나 나왔는데 -50이면 어캄
    result = -50
    # 방문 정보를 나타낼 빈 배열 초기화
    visited = []
    max_sum(0, 0)   # 함수 실행
    print(f'#{test_case} {result}')   # 결과 값 출력