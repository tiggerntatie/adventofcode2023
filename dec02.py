# Part 1,2 sample:
# 8
# 2286
# Part 1,2 full:
# 2006
# 84911
# 

reds = 12
greens = 13
blues = 14

def part1and2(data):
    totes1 = 0
    totes2 = 0
    for gamen, l in enumerate(data): # gamen zero based
        g = [[y.split(" ") for y in x.split(", ")] for x in l.strip().split(": ")[1].split("; ")]
        counts = {'red':0, 'green':0, 'blue':0}
        for r in g:
            for c in r:
                if counts[c[1]] < int(c[0]):
                    counts[c[1]] = int(c[0])
        if counts['red'] <= reds and counts['green'] <= greens and counts['blue'] <= blues:
            totes1 += gamen + 1
        totes2 += counts['red'] * counts['green'] * counts['blue']
    return totes1, totes2

import string
if __name__ in ['exec','__main__']: # supports bugged runpython.org
    for fnam in ['dec02s.txt', 'dec02.txt']:
        with open(fnam) as file:
            result = part1and2(file.readlines())
            print(result[0])
            print(result[1])