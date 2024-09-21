with open('input.txt', 'r') as file:
    lines = [line.rstrip() for line in file]

def get_x_frequent_chars_in_column(_lines, _col):
    dictionary = {}

    for line in _lines:
        char = line[_col]
        dictionary[char] = dictionary.get(char, 0) + 1

    most_frequent_char  = sorted(dictionary.items(), key=lambda x: -x[1])[0][0]
    least_frequent_char = sorted(dictionary.items(), key=lambda x:  x[1])[0][0]

    return most_frequent_char, least_frequent_char

num_cols = len(lines[0])
message1 = []
message2 = []

for col in range(num_cols):
    chars = get_x_frequent_chars_in_column(lines, col)
    message1.append(chars[0])
    message2.append(chars[1])

message1 = ''.join(message1)
message2 = ''.join(message2)
print(message1)
print(message2)