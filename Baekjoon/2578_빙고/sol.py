import sys
sys.stdin = open('input.txt')

def find_change_0(arr, n):
    if n in arr:
        idx = arr.index(n)
        arr[idx] = 0

# 내가 갖고 있는 빙고판
my_field = [list(map(int, input().split())) for i in range(5)]
daegak_1 = []
daegak_2 = []
for i in range(5):
    daegak_1.append(my_field[i][i])
for i in range(5):
    daegak_2.append(my_field[i][4-i])
###################################################################
# 너(사회자)꺼
your_field = [list(map(int, input().split())) for i in range(5)]
# 몇번 불렀는지 확인해줄 count 변수 초기화
count = 0
for your in your_field:
    for y in your:
        # 대각 줄에서 찾아서 0
        find_change_0(daegak_1, y)
        find_change_0(daegak_2, y)
        # 가로줄, 세로줄에서 찾아서 0
        for my in my_field:
            find_change_0(my, y)
        # 한번 불렀으니까 += 1
        count += 1
        # 빙고 됐는지 확인
        bingo = 0
        # 가로줄 전체 합이 0이면 빙고 한줄 추가
        for my in my_field:
            if sum(my) == 0:
                bingo += 1
        # 대각의 전체 합이 0이면 빙고 한줄 추가
        if sum(daegak_1) == 0:
            bingo+= 1
        if sum(daegak_2) == 0:
            bingo+= 1
        # 세로줄 전체 합이 0이면 빙고 한줄 추가
        for i in range(5):
            result = 0
            for j in range(5):
                result += my_field[j][i]
            if result == 0:
                bingo+= 1
        # 현재 빙고가 3줄 이상 나왔다면 종료, 여태까지 카운트 출력
        if bingo >= 3:
            print(count)
            exit()
