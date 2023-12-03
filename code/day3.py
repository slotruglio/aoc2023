import re

matches = dict()
pattern = r"[^\w\s\.]"
with open("inputs/day3.txt", "r") as f:
    lines = f.readlines()

for x, line in enumerate(lines):
    number, neighbors = [], set()
    for y, c in enumerate(line):
        if c.isdigit():
            number.append(c)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    if x+dx < 0 or y+dy < 0 or x+dx >= len(lines) or y+dy >= len(line):
                        continue
                    if re.match(pattern, lines[x+dx][y+dy]):
                        neighbors.add(((x+dx, y+dy), lines[x+dx][y+dy]))
        if len(number) > 0 and (not c.isdigit() or y == len(line)-1):
            for n in neighbors:
                matches.setdefault(n, []).append(int("".join(number)))
            number, neighbors = [], set()

total_part1 = sum([sum(matches[key]) for key in matches])
total_part2 = sum([matches[key][0]*matches[key][1]
                  for key in matches if key[1] == "*" and len(matches[key]) == 2])
print("Part 1:", total_part1)
print("Part 2:", total_part2)
