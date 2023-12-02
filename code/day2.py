# part 1
demo = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

maximum = {"red":12, "green":13, "blue":14}
valid_games = []
for line in open("inputs/day2.txt", "r").readlines():
    name, extractions = line.split(":")
    name = int(name.split(" ")[-1])
    extractions = extractions.split(";")
    valid = True
    for extraction in extractions:
        totals = {"red":0, "green":0, "blue":0}
        sets = extraction.split(",")
        for s in sets:
            s = s.strip()
            number, color = s.split(" ")
            totals[color] += int(number)
        if any([totals[color] > maximum[color] for color in totals]):
            valid = False
    if valid: valid_games.append(name)

print("Part 1:", sum(valid_games))

# part 2
powers = []
for line in open("inputs/day2.txt", "r").readlines():
    name, extractions = line.split(":")
    name = int(name.split(" ")[-1])
    extractions = extractions.split(";")
    minimum = {"red":0, "green":0, "blue":0}
    for extraction in extractions:
        totals = {"red":0, "green":0, "blue":0}
        sets = extraction.split(",")
        for s in sets:
            s = s.strip()
            number, color = s.split(" ")
            totals[color] += int(number)
        for color in totals:
            if totals[color] > minimum[color]:
                minimum[color] = totals[color]
    value = 1  
    for color in minimum:
        value *= minimum[color]
    powers.append(value)

print("Part 2:", sum(powers))


