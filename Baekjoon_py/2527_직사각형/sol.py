import sys
sys.stdin = open('input.txt')

T = 4
for test_case in range(1, T+1):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # 초기 값은 직사각형으로 설정
    result = 'a'
    # 안겹칠 때
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        result = 'd'
    # 점으로 겹칠 때
    elif (p1 == x2 and (q1 == y2 or y1 == q2)) or (p2 == x1 and (q2 == y1 or q1 == y2)):
        result = 'c'
    # 선으로 겹칠때
    elif p1 == x2 or p2 == x1 or q1 == y2 or y1 == q2:
        result = 'b'
    # 결과값
    print(result)