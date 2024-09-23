with open('input.txt', 'r') as file:
    lines = [line.rstrip().split() for line in file]

def n_lit_pixels(_lines):
    wide = 50
    tall = 6
    matrix = []
    for i in range(tall):
        matrix.append([])
        for j in range(wide):
            matrix[i].append(False)

    def shift_row(_row, _amount):
        copy = [row[:] for row in matrix]
        for idx in range(wide):
            val = matrix[_row][idx]
            new_idx = (idx + _amount) % wide
            copy[_row][new_idx] = val
        for r in range(tall):
            matrix[r] = copy[r]

    def shift_col(_col, _amount):
        copy = [row[:] for row in matrix]
        for idx in range(tall):
            val = matrix[idx][_col]
            new_idx = (idx + _amount) % tall
            copy[new_idx][_col] = val
        for r in range(tall):
            matrix[r] = copy[r]

    def update_matrix(_line):
        if _line[0] == "rect":
            dimensions = _line[1].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            for x in range(height):
                for y in range(width):
                    matrix[x][y] = True
        else:
            place = int(_line[2][2:])
            amount = int(_line[4])

            if _line[1] == "row":
                shift_row(place, amount)
            else:
                shift_col(place, amount)


    for line in _lines:
        update_matrix(line)

    counter = 0
    for i in range(tall):
        for j in range(wide):
            if matrix[i][j]:
                counter += 1

    return counter


print(n_lit_pixels(lines))
