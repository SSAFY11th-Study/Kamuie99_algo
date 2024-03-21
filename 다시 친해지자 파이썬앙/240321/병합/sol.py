import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
  global count
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left_list = merge_sort(arr[:mid])
  right_list = merge_sort(arr[mid:])
  
  merged = []
  i, j = 0, 0
  
  while i < len(left_list) and j < len(right_list):
    if left_list[i] <= right_list[j]:
      merged.append(left_list[i])
      i += 1
    else:
      merged.append(right_list[j])
      j += 1
      
  merged.extend(left_list[i:])
  merged.extend(right_list[j:])
  
  if left_list[-1] > right_list[-1]:
    count += 1
    
  return merged
    


T = int(input())
for test_case in range(1, T+1):
  N = int(input())
  field = list(map(int, input().split()))
  count = 0
  result = merge_sort(field)
  print(result[N//2], count)