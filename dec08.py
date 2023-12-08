# dec08.py
# Part 1 sample 1:
# 2
# Part 1 sample 2:
# 6
# Part 1 full:
# 12737
# Part 2 sample 3:
# 6
# Part 2 full:
# 9064949303801
# 

from math import lcm

def part1(data):
    rules = {}
    turns = []
    steps1 = 0
    for n, l in enumerate(data):
        if not n:
            turns = [0 if c == 'L' else 1 for c in list(l.strip())]
        elif l.strip() != "":
            rules[l[:3]] = [l[7:10],l[12:15]]
    node = 'AAA'
    while node != 'ZZZ':
        node = rules[node][turns[steps1%len(turns)]]
        steps1 += 1
    return steps1            

def part2(data):
    rules = {}
    turns = []
    steps2 = 0
    for n, l in enumerate(data):
        if not n:
            turns = [0 if c == 'L' else 1 for c in list(l.strip())]
        elif l.strip() != "":
            rules[l[:3]] = [l[7:10],l[12:15]]
    # list of starting nodes
    snodes = list(filter(lambda x: x[2] == 'A', rules))
    paths = len(snodes)
    pds = {}  # periodicity tracker
    while len(list(filter(lambda x: x[2] == 'Z', snodes))) != paths:
        snodes = [rules[n][turns[steps2%len(turns)]] for n in snodes]
        steps2+= 1
        for s, n in enumerate(snodes):
            if n[2] == 'Z' and s not in pds:
                pds[s] = steps2
        if len(pds) == paths:  # have we seen a full cycle of each path?
            return lcm(*pds.values())
    return steps2           

if __name__ in ['__main__']:
    for fnam in ['dec08s1.txt', 'dec08s2.txt', 'dec08.txt']:
        with open(fnam) as file:
            print(part1(file.readlines()))
    for fnam in ['dec08s3.txt', 'dec08.txt']:
        with open(fnam) as file:
            print(part2(file.readlines()))