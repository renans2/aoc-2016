lines = []

with open('input.txt', 'r') as file:
    for line in file:
        formatted = list(map(int, line.strip().split()))
        lines.append(formatted)

def triangle_is_possible(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

#################### Part 1 ########################

possible_triangles1 = 0

for x, y, z in lines:
    if triangle_is_possible(x, y, z):
        possible_triangles1 += 1

print(possible_triangles1)


#################### Part 2 ########################

n_possible2 = 0

for col in range(3):
    for row in range(0, len(lines), 3):
        if triangle_is_possible(lines[row][col],
                                lines[row+1][col],
                                lines[row+2][col]):
            n_possible2 += 1

print(n_possible2)
