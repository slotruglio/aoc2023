import re

def calc_ways(t, d):
    return len([x for x in range(1, t+1) if x * (t-x) >= d])

times = []
distances = []
for line in open("inputs/day6.txt", "r").readlines():
    # for line in demo:
    if len(times) == 0:
        times.extend([int(x) for x in re.findall(r"\d+", line)])
        continue
    distances.extend([int(x) for x in re.findall(r"\d+", line)])

part_1 = 1
for i, time in enumerate(times):
    part_1 *= calc_ways(time, distances[i])

print("Part 1:", part_1)

new_time = ''.join([str(x) for x in times])
new_distance = ''.join([str(x) for x in distances])
part_2 = calc_ways(int(new_time), int(new_distance))
print("Part 2:", part_2)
