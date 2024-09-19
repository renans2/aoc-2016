with open('input.txt', 'r') as file:
    instructions = [line.rstrip() for line in file.readlines()]

################### Part 1 ###################

# the numpad is going to be a matrix
# and each number is going to have
# an i index (for the row) and
# a j index (for the column)

# the starting position is
# i = 1 and j = 1 (for the number 5)

numpad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

i = 1
j = 1
code = []

def process_line(line, __i, __j):
    _i = __i
    _j = __j

    for move in line:
        if move == 'U' and _i > 0:
            _i -= 1
        elif move == 'D' and _i < len(numpad) - 1:
            _i += 1
        elif move == 'L' and _j > 0:
            _j -= 1
        elif move == 'R' and _j < len(numpad) - 1:
            _j += 1

    return _i, _j

for line in instructions:
    new_numpad_position = process_line(line, i, j)
    i = new_numpad_position[0]
    j = new_numpad_position[1]
    code.append(numpad[i][j])

print(code)

################### Part 2 ###################

numpad = [[0, 0,  1,  0, 0],
          [0, 2,  3,  4, 0],
          [5, 6,  7,  8, 9],
          [0,'A','B','C',0],
          [0, 0, 'D', 0, 0]]

i = 2
j = 0
code = []

def process_line2(line, __i, __j):
    _i = __i
    _j = __j

    for move in line:
        if move == 'U' and _i > 0                 and numpad[_i - 1][_j] != 0:
            _i -= 1
        elif move == 'D' and _i < len(numpad) - 1 and numpad[_i + 1][_j] != 0:
            _i += 1
        elif move == 'L' and _j > 0               and numpad[_i][_j - 1] != 0:
            _j -= 1
        elif move == 'R' and _j < len(numpad) - 1 and numpad[_i][_j + 1] != 0:
            _j += 1

    return _i, _j

for line in instructions:
    new_numpad_position = process_line2(line, i, j)
    i = new_numpad_position[0]
    j = new_numpad_position[1]
    code.append(numpad[i][j])

print(code)
