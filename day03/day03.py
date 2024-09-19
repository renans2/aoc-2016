with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]

#################### Part 1 ########################

n_possible = 0

for line in lines:
    sides = line.split()
    is_possible = True

    for i in range(3):
        if int(sides[i]) + int(sides[(i + 1) % 3]) <= int(sides[(i + 2) % 3]):
            is_possible = False
            break

    if is_possible:
        n_possible += 1

print(n_possible)