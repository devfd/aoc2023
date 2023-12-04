import re


def parse_line(line):
    match = re.match(r"Card.* (\d+): (.+) \| (.+)", line)
    card_id = int(match.group(1))
    winning = [int(n) for n in match.group(2).split()]
    draws = [int(n) for n in match.group(3).split()]
    return card_id, winning, draws


with open("input.txt", "r") as file:
    total = 0
    card_counters = {}

    for line in file:
        card_id, winning, draws = parse_line(line)
        match_count = sum(d in winning for d in draws)

        card_counters[card_id] = card_counters.get(card_id, 0) + 1

        if match_count > 0:
            total += 2 ** (match_count - 1)
            for i in range(match_count):
                next_card_id = card_id + i + 1
                card_counters[next_card_id] = (
                    card_counters.get(next_card_id, 0) + card_counters[card_id]
                )

    print("Part 1:", total)
    print("Part 2:", sum(card_counters.values()))
