import re

with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

def has_abba(string):
    found = False
    i = 0

    while not found and i < len(string) - 3:
        if string[i] != string[i + 1] and string[i] == string[i + 3] and string[i + 1] == string[i + 2]:
            found = True
        else:
            i += 1

    return found

def supports_tls(_line):
    outside_brackets = re.split(r'\[.*?]', _line)
    inside_brackets = re.findall(r'\[(.*?)]', _line)

    supports = False

    for string in outside_brackets:
        if has_abba(string):
            supports = True
            break

    if not supports:
        return False

    for string in inside_brackets:
        if has_abba(string):
            supports = False
            break

    return supports

counter = 0
for line in lines:
    if supports_tls(line):
        counter += 1

print(counter)