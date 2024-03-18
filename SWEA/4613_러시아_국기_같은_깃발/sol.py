import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    field = []
    for i in range(N):
        temp = input()
        field.append(temp)     
    print(field)
    
    field[0] = field[0].replace('R', 'W').replace('B', 'W')

    field[-1] = field[-1].replace('W', 'R').replace('B', 'R')
    
    color = 1
    for i in range(1, len(field)-1):
        count_W = field[i].count('W')
        count_B = field[i].count('B')
        count_R = field[i].count('R')
        # 만약 밑에 두줄 이상 남아있다면, 현재 칠해진 색이 1개라면, 흰색이 더 많이 칠해져 있다면
        if i < len(field)-2 and color == 1 and count_W > count_B:
            field[i] = field[i].replace('R', 'W').replace('B', 'W')
        # 만약 밑에 한줄 이상, 현재 칠해진 색 1개, 파란색이 더 많이 칠해져 있다
        elif color == 1 and count_W < count_B:
            field[i] = field[i].replace('R', 'B').replace('W', 'B')
            color += 1
        # 현재 칠해진 색 2개, 파란색이 더 많이 칠해져 있다면
        elif color == 2 and count_B >= count_R:
            field[i] = field[i].replace('R', 'B').replace('W', 'B')
        # 현재 칠해진 색 3개 거나, 2개인데 빨간색이 더 많이 칠해져 있다면
        else:
            field[-1] = field[-1].replace('W', 'R').replace('B', 'R')
    print(field)