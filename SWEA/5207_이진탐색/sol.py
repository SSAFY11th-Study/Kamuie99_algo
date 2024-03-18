def binary_search(x):
    s, e = 0, n - 1 # s는 시작, e는 끝 n - 1
    check = 0
    while s <= e:   # s가 e보다 작거나 같은 동안
        mid = (s + e) // 2  # 중간 값은 두개 합의 나누기 2
        if a[mid] == x:     # 찾는 값이면 바로 종료
            return True     # True 값 반환
        elif a[mid] > x:    # 만약 x 보다 크다면
            if check == 1:  # check가 1이면 종료
                break       
            check = 1       # 그렇지 않으면 check를 1
            e = mid - 1     # 그 다음 왼쪽 탐색을 위해 e값 변경
        else:
            if check == 2: 
                break   
            check = 2       # 그렇지 않으면 check를 2
            s = mid + 1     # 그 다음 오른쪽 탐색을 위해 s값 변경
    return False

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binary_search(num)
    print(f'#{test_case} {total}')