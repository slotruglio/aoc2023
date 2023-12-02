def get_id_games(line):
    number, extractions = line.split(":")
    number = int(number.split(" ")[-1])
    extractions = extractions.split(";")
    return number, extractions

def count_cubes(extraction):
    totals = {"red":0, "green":0, "blue":0}
    sets = extraction.split(",")
    for s in sets:
        s = s.strip()
        number, color = s.split(" ")
        totals[color] += int(number)
    return totals

# part 1
maximum = {"red":12, "green":13, "blue":14}
total_part1 = 0
for line in open("inputs/day2.txt", "r").readlines():
    number, extractions = get_id_games(line)
    valid = True
    for extraction in extractions:
        totals = count_cubes(extraction)
        if any([totals[color] > maximum[color] for color in totals]):
            valid = False
            break
    if valid: total_part1 += number

print("Part 1:", total_part1)

# part 2
total_part2 = 0
for line in open("inputs/day2.txt", "r").readlines():
    _, extractions = get_id_games(line)
    minimum = {"red":0, "green":0, "blue":0}
    for extraction in extractions:
        totals = count_cubes(extraction)
        for color in totals:
            minimum[color] = max(minimum[color], totals[color])
    value = 1  
    for color in minimum:
        value *= minimum[color]
    total_part2 += value

print("Part 2:", total_part2)


