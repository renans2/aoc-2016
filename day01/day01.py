with open('input.txt', 'r') as file:
    line = file.readline().split(", ")

############### Part 1 ####################

# the 'facing' variable represents the
# direction it's currently facing

# 0 -> facing north
# 1 -> facing east
# 2 -> facing south
# 3 -> facing west

# R increments 'facing'
# L decrements 'facing'

facing = 0
xOffset = 0
yOffset = 0

for instruction in line:
    facing = (facing + (1 if instruction[0] == "R" else -1)) % 4
    blocks = int(instruction[1:])

    if facing % 2 == 0: # facing north or south
        yOffset += blocks if facing == 0 else -blocks
    else:               # facing east or west
        xOffset += blocks if facing == 1 else -blocks

print(abs(xOffset) + abs(yOffset))

############### Part 2 ####################

facing = 0
xOffset = 0
yOffset = 0
visited_locations = set()
visited_locations.add((xOffset, yOffset))
visited_twice = ()

for instruction in line:
    facing = (facing + (1 if instruction[0] == "R" else -1)) % 4
    blocks = int(instruction[1:])
    incrementer = ()

    if facing == 0:
        incrementer = (0, 1)
    elif facing == 1:
        incrementer = (1, 0)
    elif facing == 2:
        incrementer = (0, -1)
    else:
        incrementer = (-1, 0)

    for _ in range(blocks):
        xOffset += incrementer[0]
        yOffset += incrementer[1]
        coords = (xOffset, yOffset)

        if coords in visited_locations:
            visited_twice = coords
            break
        else:
            visited_locations.add(coords)

    if visited_twice:
        break

print(abs(visited_twice[0]) + abs(visited_twice[1]))
