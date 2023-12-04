import re


def parse(line):
    winning, numbers = re.sub(r"Card \d+: ", "", line).strip().split(" | ")
    winning = [x for x in winning.split(" ") if x.isdigit()]
    numbers = [x for x in numbers.split(" ") if x.isdigit()]
    return winning, numbers


def get_matches(winning, numbers):
    count = 0
    for w in winning:
        if w in numbers:
            count += 1
            continue
    return count


total_part1 = 0
total_part2 = 0
with open("inputs/day4.txt", "r") as f:
    lines = f.readlines()
    copies = [1] * len(lines)
    for i, line in enumerate(lines):
        w, n = parse(line)
        count = get_matches(w, n)
        for y in range(count):
            copies[i+y+1] += copies[i]
        total_part1 += int(2**(count-1))
    total_part2 = sum(copies)

print("Part 1:", total_part1)
print("Part 2:", total_part2)
