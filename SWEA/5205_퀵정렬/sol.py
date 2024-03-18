def partition(left, right):
    if left >= right: # 왼쪽이 오른쪽보다 크거나 같으면 바로 리턴
        return

    pivot = left  # left 값을 pivot에 저장
    i = left+1    # left + 1 을 i
    j = right-1   # right - 1 을 j
    while i <= j:
        while i <= j and A[pivot] >= A[i]: 
          i += 1  # 인덱스를 벗어나지 않고 값이 작거나 같은 동안 계속 +1

        while i <= j and A[pivot] <= A[j]: 
          j -= 1 # 인덱스를 벗어나지 않고 값이 크거나 같은 동안 계속 -1

        if i <= j:  # j가 i와 크거나 같다면 둘이 자리 바꾸기
            A[i], A[j] = A[j], A[i]
    # pivot 과 j 자리 교체
    A[pivot], A[j] = A[j], A[pivot]

    partition(left, j)  # 반띵해서 계속 수행
    partition(j+1, right) # 반띵해서 계속 수행

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    left = 0
    right = len(A)
    partition(left, right)

    print(f'#{test_case} {A[N//2]}')