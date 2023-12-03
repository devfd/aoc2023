import re


def parse_subset(subset):
    color_counts = re.findall(r"(\d+) (red|green|blue)", subset)
    return {color: int(count) for count, color in color_counts}


def parse_line(line):
    match = re.match(r"Game (\d+): (.+)", line)
    game_id = int(match.group(1))
    sets = [parse_subset(s) for s in match.group(2).split("; ")]
    return (game_id, sets)


with open("input.txt", "r") as file:
    total = 0

    for line in file:
        game_id, sets = parse_line(line)
        max_red = max(s.get("red", 0) for s in sets)
        max_green = max(s.get("green", 0) for s in sets)
        max_blue = max(s.get("blue", 0) for s in sets)

        total += max_red * max_green * max_blue

    print(total)
