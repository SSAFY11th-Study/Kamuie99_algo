# 최대값을 찾아주고 누적합에 더해주는 함수
def find_max(x, y, N, M, field):
    # 누적합을 전역 변수로 설정
    global total_sum
    # 현재 최대값은 0으로 초기화
    max_num = 0
    # 현재 좌표 값(최좌상단)이 최대값인 상태이므로 저장
    max_x = x
    max_y = y
    # 해당 M 크기 만큼의 행렬을 순회하며
    for i in range(x, x+M):
        for j in range(y, y+M):
            # 인덱스 범위를 벗어나지 않았다면
            if 0 <= i < N and 0 <= j < N :
                # temp로 저장하여
                temp = field[i][j]
                # 만일 temp가 현재까지의 최대값 보다 크다면
                if temp > max_num:
                    # 최대값을 temp로 하고, temp의 좌표를 max 좌표로 수정
                    max_num = temp
                    max_x = i
                    max_y = j
    # 다 끝난 뒤에 현재의 최대값을 누적합에 합산
    total_sum += max_num
    # 만약 현재의 최대값 좌표가 직전 받았던 좌표와 동일하다면
    if x == max_x and y == max_y:
        # 그리고 혹시 0, 0이 최대값이라 초기에 종료됐다면
        if x == 0 and y == 0:
            # 0,0 좌표의 값을 total_sum에 더한 채로 반환해주고 종료
            return total_sum
        else:
            # 그렇지 않다면 마지막 값은 누적합에 반영하지 않고 종료
            total_sum -= max_num
            return total_sum
    else:
        # 직전 최대값 좌표와 동일하지 않다면 계속 재귀적으로 함수 실행
        find_max(max_x, max_y, N, M, field)

# 첫줄에 테스트 케이스 개수 T가 주어진다.
T = int(input())
# 각 테스트 케이스
for test_case in range(1, T+1):
    # 첫 줄에는 N, M이 주어진다.
    N, M = map(int, input().split())
    # 다음 N줄에 각 N개의 정수 띄워쓰기로 구분되어 주어진다.
    field = [list(map(int, input().split())) for i in range(N)]
    # 누적합을 저장할 변수 초기화
    total_sum = 0
    # 함수 실행
    find_max(0, 0, N, M, field)
    # 테스트케이스 번호와 함께 출력
    print(f'#{test_case} {total_sum}')