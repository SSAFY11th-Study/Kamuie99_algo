import sys
sys.stdin = open('input.txt')

result = []

N, K = map(int, input().split())

field = list(map(int, input().split()))

for i in range(N-K+1):
    result.append(sum(field[i:i+K]))
        
print(max(result))