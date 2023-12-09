# dec09.py
# Part 1,2 sample:
# 114
# 2
# Part 1,2 full:
# 1762065988
# 1066


def part1and2(data):
    ext = 0
    prev = 0
    for l in data:
        nlist = [int(x) for x in l.split()]
        diffs = nlist[::]
        lastdiffs = []
        firstdiffs = []
        newdiffs = []
        while diffs.count(0) != len(diffs):
            for i in range(1, len(diffs)):
                newdiffs.append(diffs[i]-diffs[i-1])
            lastdiffs.append(newdiffs[-1])
            firstdiffs.append(newdiffs[0])
            diffs = newdiffs
            newdiffs = []
        ext += sum(lastdiffs) + nlist[-1]
        while len(firstdiffs) > 1:
            firstdiffs[-2] = firstdiffs[-2]-firstdiffs[-1]
            firstdiffs.pop()
        prev += nlist[0] - firstdiffs[0]
    return ext, prev


if __name__ in ['__main__']:
    for fnam in ['dec09s.txt', 'dec09.txt']:
        with open(fnam) as file:
            a, b = part1and2(file.readlines())
            print(a)
            print(b)

