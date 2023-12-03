import re


def word_to_digit(word):
    return {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }.get(word, None)


def extract_numbers(line):
    matches = re.findall(r"(one|two|three|four|five|six|seven|eight|nine|\d)", line)
    return [word_to_digit(m) if m.isalpha() else int(m) for m in matches]


with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    total = 0

    for line in lines:
        numbers = extract_numbers(line)
        if numbers:
            first_digit, last_digit = numbers[0], numbers[-1]
            total += first_digit * 10 + last_digit

    print(total)
