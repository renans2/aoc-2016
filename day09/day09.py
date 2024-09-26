with open('input.txt', 'r') as file:
    line = file.readline()

decompressed = []

i = 0
while i < len(line):
    if line[i] == '(':
        marker, j = "", i+1
        while line[j] != ")":
            marker += line[j]
            j += 1
        j += 1
        marker = "".join(marker).split("x")
        n_chars, n_repeats = int(marker[0]), int(marker[1])
        i = j + n_chars
        decompressed.extend(line[j:i] * n_repeats)
    else:
        decompressed.append(line[i])
        i += 1

decompressed = "".join(decompressed)
print(len(decompressed))