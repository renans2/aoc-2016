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
    _id = ''

    for char in _line:
        if char.isdigit():
            _id += char

    return int(_id)

######################### Part 1 #########################

total = 0

for line in lines:
    if is_a_room(line):
        total += get_id(line)

print(total)
