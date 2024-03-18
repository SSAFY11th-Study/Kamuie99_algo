import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

field = list(map(int, input().split()))

result = []
result.append(sum(field[:K]))

for i in range(N - K):
    result.append(result[i] - field[i] + field[K+i])
        
print(max(result))