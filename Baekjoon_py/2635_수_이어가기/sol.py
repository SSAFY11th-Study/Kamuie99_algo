N = int(input())    # 첫번째 수를 입력받는다.
max_len = 0     # 최대 개수의 수들을 셀 변수 초기화
results = []    # 결과들을 담을 배열 초기화
# N-1부터 1까지의 수들을 두번째 수로 차례로 설정하여
for i in range(N-1, -1, -1):
    field = [N, N-i]    # 두번째 수가 i일 때 초기 상황
    # 큰 수를 반복값으로 설정한 뒤, 특정 조건 만족하면 종료
    for j in range(100000):
        next = field[j] - field[j+1]    # 0번째 수 - 1번째 수 = 다음 수
        if next < 0:    # 음수이면 끝
            break
        else:           # 양수이면 append
            field.append(next)
    # 만약 이번 계산의 배열 길이가 최대배열 길이보다 크면
    if len(field) > max_len:
        max_len = len(field)    # 해당 배열 길이를 최대 배열 길이로 설정
        results = field   # 해당 배열을 결과들을 담을 배열에 추가

print(len(results))
print(*results)