str_input = list(map(str, input()))

dial = [[], [],  ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
        ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

time = 0

for str in str_input:
    for i in range(len(dial)):
        if str in dial[i]:
            temp = i + 1
            time += temp

print(time)

