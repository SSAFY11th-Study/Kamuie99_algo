import sys
sys.stdin = open('input.txt')

field = [list(map(int, input().split())) for _ in range(9)]

numbers = []

for raw in field:
    numbers.append(max(raw))

max_number = max(numbers)
max_idx1 = numbers.index(max_number)
max_idx2 = field[max_idx1].index(max_number)

print(max_number)
print(max_idx1+1, max_idx2+1)