import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    global result
    # 언제까지 분할 해 나갈 것이냐.
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left_list = merge_sort(arr[:middle])    # [2]
    right_list = merge_sort(arr[middle:])   # [2]
    merged = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[j])
            j += 1
    # 범위 내 조사를 마쳤는데...
    merged.extend(left_list[i:])
    merged.extend(right_list[j:])

    if left_list[-1] > right_list[-1]:
        result += 1

    return merged



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0  # 병합 과정에서 왼쪽 끝 요소가 오른쪽 끝 요소보다 큰 경우
    merged_list = merge_sort(nums)
    print(f'#{tc} {merged_list[N//2]} {result}')