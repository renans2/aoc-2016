with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

def get_five_most_common(_line):
    _dictionary = {}

    for char in _line:
        if char.isdigit():
            break
        elif char == '-':
            continue
        else:
            _dictionary[char] = _dictionary.get(char, 0) + 1

    _dictionary = dict(sorted(_dictionary.items(), key=lambda item: (-item[1], item[0])))
    most_common = [item[0] for item in list(_dictionary)[0:5]]

    return most_common

def get_checksum(_line):
    return [char for char in _line[-6:-1]]

def is_a_room(_line):
    return get_five_most_common(_line) == get_checksum(_line)

def get_id(_line):
    _id = []

    for char in _line:
        if char.isdigit():
            _id.append(char)

    return int(''.join(_id))

######################### Part 1 #########################

total = 0

for line in lines:
    if is_a_room(line):
        total += get_id(line)

print(total)

######################### Part 2 #########################
room_name = "northpole object storage"

def shifted(_line):
    shifted_room_name = []
    sector_id = get_id(_line)

    for char in _line:
        if char == '-':
            shifted_room_name.append(' ')
        elif char.isdigit():
            break
        else:
            shifted_room_name.append(chr((ord(char) - ord('a') + sector_id) % 26 + ord('a')))

    return ''.join(shifted_room_name).rstrip()

def get_north_pole_id(_lines):
    for line in lines:
        if shifted(line) == room_name:
            return get_id(line)

    return -1

print(get_north_pole_id(lines))
