import sys
sys.stdin = open('input.txt')


# N은 돌의 개수, 앞에 추가한 0때문에 인덱스 범위 작업 시 N번재 인덱스도 포함해야함
def work(field, i, j, w, N):

    if w == 1:  # 1번 작업
        for k in range(i, i+j):
            if 1 <= k <= N: # 인덱스 범위를 벗어나지 않았다면
                field[k] = 1 - field[k] # 0이었다면 1이되고 1이었다면 0이 됨
        return field    # 반복문이 끝났다면 작업 종료, 리턴

    if w == 2:  # 2번 작업
        color = field[i]    # 현재 인덱스의 색상을 저장해 놓는다.
        for k in range(i, i+j):  # i번째부터 j개의 돌에 대해
            if 1 <= k <= N: # 인덱스를 초과하지 않았다면
                field[k] = color    # 색상을 바꾸어 준다.
        return field    # 반복문이 끝났다면 작업 종료, 리턴

    if w == 3:  # 3번 작업
        for k in range(1, j+1):   # 마주보는 돌 j개에 대해서 -> 1부터
            if 1 <= i - k and i + k <= N:   # 인덱스를 벗어나지 않았고
                if field[i-k] == field[i+k]:    # 두개의 색상이 같다면
                    field[i-k] = 1 - field[i-k] # 색상을 변경해준다
                    field[i+k] = 1 - field[i+k] # 색상을 변경해준다.
            else: # 인덱스를 벗어났다면
                break   # 끝
        return field


T = int(input())    # 테스트케이스 수 입력받기
result = []     # 결과를 저장할 빈 배열 초기화
for test_case in range(1, T+1):
    # 첫줄에 돌의 개수 N과 뒤집기 작업의 총 횟수 M
    N, M = map(int, input().split())
    # 다음 줄에 흰색 0, 검은색 1로 표시된 N개 돌의 초기 상태
    field = list(map(int, input().split()))
    # i번째 부터 돌을 뒤집는다 할때, 첫번째는 0번 인덱스이므로, 편의를 위해 앞에 0 추가
    field = [0] + field
    for _ in range(M):  # 이어 M개의 줄에
        # 기준 위치 i, 작업할 돌의 개수 j, 작업 번호 w가 주어진다.
        i, j, w = map(int, input().split())
        # 함수를 실행한 결과값을 저장한다.
        result = work(field, i, j, w, N)
    # 저장된 최종 결과를 확인한다.
    print(f'#{test_case}', *result[1:])