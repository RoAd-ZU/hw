def change_line(line):
    """docstring"""
    return line.upper()

def change_line_title(line):
    """docstring"""
    return line.title()


line_u = input()
print(change_line(line_u))
print(change_line_title(line_u))