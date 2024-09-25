with open('input.txt', 'r') as file:
    lines = [line.rstrip().split() for line in file]

class Display:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        for i in range(rows):
            self.matrix.append([])
            for j in range(cols):
                self.matrix[i].append(False)

    def get_copy(self):
        copy = [row[:] for row in self.matrix]
        return copy

    def shift_row(self, _row, _amount, copy):
        for idx in range(self.cols):
            val = self.matrix[_row][idx]
            new_idx = (idx + _amount) % self.cols
            copy[_row][new_idx] = val
        for r in range(self.rows):
            self.matrix[r] = copy[r]

    def shift_col(self, _col, _amount, copy):
        for idx in range(self.rows):
            val = self.matrix[idx][_col]
            new_idx = (idx + _amount) % self.rows
            copy[new_idx][_col] = val
        for r in range(self.rows):
            self.matrix[r] = copy[r]

    def update_matrix(self, _line):
        if _line[0] == "rect":
            dimensions = _line[1].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            for x in range(height):
                for y in range(width):
                    self.matrix[x][y] = True
        else:
            place = int(_line[2][2:])
            amount = int(_line[4])

            copy = self.get_copy()
            if _line[1] == "row":
                self.shift_row(place, amount, copy)
            else:
                self.shift_col(place, amount, copy)

    def get_lit_pixels(self):
        lit = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j]:
                    lit += 1

        return lit


########################### Part 1 ###########################

width = 50
height = 6
display = Display(height, width)

for line in lines:
    display.update_matrix(line)

print(display.get_lit_pixels())
