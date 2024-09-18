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
visited_locations.add((xOffset, yOffset))  # Adicionar o ponto inicial
visited_twice = ()

for instruction in line:
    facing = (facing + (1 if instruction[0] == "R" else -1)) % 4

    blocks = int(instruction[1:])

    if facing == 0:
        for i in range(blocks):
            yOffset += 1
            coords = (yOffset, xOffset)
            if coords not in visited_locations:
                visited_locations.add(coords)
            else:
                visited_twice = coords
                break
    elif facing == 1:
        for i in range(blocks):
            xOffset += 1
            coords = (yOffset, xOffset)
            if coords not in visited_locations:
                visited_locations.add(coords)
            else:
                visited_twice = coords
                break
    elif facing == 2:
        for i in range(blocks):
            yOffset -= 1
            coords = (yOffset, xOffset)
            if coords not in visited_locations:
                visited_locations.add(coords)
            else:
                visited_twice = coords
                break
    else:
        for i in range(blocks):
            xOffset -= 1
            coords = (yOffset, xOffset)
            if coords not in visited_locations:
                visited_locations.add(coords)
            else:
                visited_twice = coords
                break

    if visited_twice:
        break

print(abs(visited_twice[0]) + abs(visited_twice[1]))
