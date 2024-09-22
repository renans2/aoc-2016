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
    outside_brackets = " ".join(re.split(r'\[.*?]', _line))
    inside_brackets = " ".join(re.findall(r'\[(.*?)]', _line))

    return has_abba(outside_brackets) and not has_abba(inside_brackets)



def is_aba(s):
    return s[0] != s[1] and s[0] == s[2]

def has_corresponding_bab(s, target):
    i = 0
    found = False

    while not found and i < len(s) - 2:
        if s[i] != s[i + 1] and s[i] == s[i + 2] and s[i] == target[1] and s[i + 1] == target[0]:
            found = True
        else:
            i += 1

    return found

def supports_ssl(_line):
    # o_b == outside_brackets
    o_b = "".join(re.split(r'\[.*?]', _line))
    # i_b == inside_brackets
    i_b = "".join(re.findall(r'\[(.*?)]', _line))

    found = False
    i = 0
    while not found and i < len(o_b) - 2:
        portion = o_b[i:i+3]
        if is_aba(portion) and has_corresponding_bab(i_b, portion):
            found = True
        else:
            i += 1

    return found


###################### Part 1 ######################

counter1 = 0
for line in lines:
    if supports_tls(line):
        counter1 += 1

print(counter1)

###################### Part 2 ######################

counter2 = 0
for line in lines:
    if supports_ssl(line):
        counter2 += 1

print(counter2)