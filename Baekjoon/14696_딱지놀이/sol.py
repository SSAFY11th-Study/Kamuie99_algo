N = int(input())

def gyaesan(arr):
    count_4 = 0
    count_3 = 0
    count_2 = 0
    count_1 = 0
    
    for i in range(1, len(arr)):
        if arr[i] == 4:
            count_4 += 1
        elif arr[i] == 3:
            count_3 += 1
        elif arr[i] == 2:
            count_2 += 1
        else:
            count_1 += 1
    
    return count_4 * 1010101 + count_3 * 10101 + count_2 * 101 + count_1


for _ in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result_a = gyaesan(a)
    result_b = gyaesan(b)
    
    if result_a > result_b:
        print('A')
    elif result_a < result_b:
        print('B')
    else:
        print('D')