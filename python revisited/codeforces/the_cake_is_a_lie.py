test_cases = int(input())

while test_cases:

    inputs = list(map(int,input().split()))
    horizontal_moves = 0
    vertical_moves = 0
    if (inputs[0] != 1):
        horizontal_moves = (inputs[0] - 1) * inputs[1]
    if (inputs[1] != 1):
        vertical_moves = (inputs[1] - 1)

    if horizontal_moves + vertical_moves == inputs[2]:
        print('YES')
    else:
        print('NO')
    test_cases-=1