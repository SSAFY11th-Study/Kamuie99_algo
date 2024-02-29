import sys
sys.stdin = open('input.txt')


# A B C D E F
# 0 1 2 3 4 5
# 0-5. 1-3, 2-4
def what_is_up(bottom_idx):
    if bottom_idx == 0:
        up = dice[5]
    elif bottom_idx == 5:
        up = dice[0]
    elif bottom_idx == 1:
        up = dice[3]
    elif bottom_idx == 3:
        up = dice[1]
    elif bottom_idx == 2:
        up = dice[4]
    elif bottom_idx == 4:
        up = dice[2]
    
    return up


N = int(input())
field = [list(map(int, input().split())) for i in range(N)]
result = []
for j in range(6):
    total = []
    for i in range(N):
        hi = [1, 2, 3, 4, 5, 6]
        dice = field[i]
        if i == 0:
            bottom_idx = j
        else:
            bottom_idx = dice.index(up)
        up = what_is_up(bottom_idx)
        hi.remove(dice[bottom_idx])
        hi.remove(up)
        total.append(max(hi))
    result.append(sum(total))

print(max(result))


# dice = list(map(int, input().split()))
# bottom_idx = 0
# up = what_is_up(bottom_idx)
# dice.remove(dice[bottom_idx])
# dice.remove(up)
# total.append(max(dice))

# dice = list(map(int, input().split()))
# bottom_idx = dice.index(up)
# up = what_is_up(bottom_idx)
# dice.remove(dice[bottom_idx])
# dice.remove(up)
# total.append(max(dice))

# dice = list(map(int, input().split()))
# bottom_idx = dice.index(up) 
# up = what_is_up(bottom_idx)
# dice.remove(dice[bottom_idx])
# dice.remove(up)
# total.append(max(dice))

# dice = list(map(int, input().split()))
# bottom_idx = dice.index(up) 
# up = what_is_up(bottom_idx)
# dice.remove(dice[bottom_idx])
# dice.remove(up)
# total.append(max(dice))

# dice = list(map(int, input().split()))
# bottom_idx = dice.index(up) 
# up = what_is_up(bottom_idx)
# dice.remove(dice[bottom_idx])
# dice.remove(up)
# total.append(max(dice))
