# dec04.py
# Part 1,2 sample:
# 13
# 30
# Part 1,2 full:
# 25231
# 9721255
# 

from collections import Counter

def part1and2(data):
    wintots = 0
    cc = Counter()
    def parsenums(line):
        card, num = line.split(': ')[1].split(' | ')
        cards = list(filter(lambda x: x, card.strip().split(' ')))
        nums = list(filter(lambda x: x, num.strip().split(' ')))
        return cards, nums
        
    for lindex, line in enumerate(data):
        lnum = lindex + 1
        cc.update([lnum,])
        c, n = parsenums(line.strip())
        if (matches := len(list(filter(lambda a,b=n: a in b, c)))) > 0:
            cc.update(cc[lnum]*list(range(lnum + 1, lnum + 1 + matches)))
            wintots += pow(2,  matches - 1)
    return (wintots, sum(cc.values()))

if __name__ in ['__main__']:
    for fnam in ['dec04s.txt', 'dec04.txt']:
        with open(fnam) as file:
            result1, result2 = part1and2(file.readlines())
            print(result1)
            print(result2)