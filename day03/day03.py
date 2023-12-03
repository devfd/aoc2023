from collections import defaultdict


def symbol_adjacent(x_min, x_max, y_min, y_max):
    for r in range(y_min, y_max):
        for c in range(x_min, x_max):
            if lines[r][c] not in ".0123456789":
                return r, c
    return None


with open("input.txt", "r") as file:
    lines = [line.strip() + "." for line in file]

    p1 = 0
    p2 = defaultdict(list)

    for row, line in enumerate(lines):
        num_str = ""
        for col, char in enumerate(line):
            if char.isdigit():
                num_str += char
            elif num_str:
                rc = symbol_adjacent(
                    max(0, col - len(num_str) - 1),
                    min(len(line) - 1, col + 1),
                    max(0, row - 1),
                    min(len(lines), row + 2),
                )

                if rc:
                    p1 += int(num_str)
                    r, c = rc
                    if lines[r][c] == "*":
                        p2[r, c].append(int(num_str))
                num_str = ""

    print("Part 1:", p1)
    print("Part 2:", sum(arr[0] * arr[1] for arr in p2.values() if len(arr) == 2))
