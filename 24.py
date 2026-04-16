import string
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    width = (size * 4) - 3
    lines = []
    for i in range(size):
        s = "-".join(alphabets[i:size])
        full_line = s[::-1] + s[1:]
        lines.append(full_line.center(width, "-"))
    print('\n'.join(lines[::-1] + lines[1:]))



