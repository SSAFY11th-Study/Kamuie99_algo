import sys
sys.stdin = open('input.txt')


scores = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,
        'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}

total_score = 0
result = 0
for i in range(20):
    name, score, grade = map(str, input().split())
    score = float(score)
    if grade != 'P':
        tmp = scores[grade]
        total_score += score
        result += tmp * score

result /= total_score
print(result)