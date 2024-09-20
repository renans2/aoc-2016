with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

def get_most_frequent_char_in_column(_lines, _col):
    dictionary = {}

    for line in _lines:
        char = line[_col]
        dictionary[char] = dictionary.get(char, 0) + 1

    dictionary = sorted(dictionary.items(), key=lambda x: -x[1])

    return dictionary[0][0]

num_cols = len(lines[0])
message = []

for col in range(num_cols):
    message.append(get_most_frequent_char_in_column(lines, col))

message = ''.join(message)
print(message)