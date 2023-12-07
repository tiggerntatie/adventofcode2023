# dec05.py
# Part 1,2 sample:
# 35
# 46
# Part 1,2 full:
# 1181555926
# 
# 

from collections import Counter

def part1and2(data):
    seeds = []
    mapnames = []
    rules = {}
    
    def processrule(rulename, n):
        res = 0
        found = False
        for r in rules[rulename]:
            if n >= r[1] and n <= r[1]+r[2]-1:
                res = r[0]+n-r[1]
                found = True
                break
        if not found:
            res = n               
        return res
    
    startmap = False
    for lindex, line in enumerate(data):
        if not lindex:    # first line, get seed numbers
            seeds = [int(x) for x in line.split(': ')[1].split(' ')]
        elif line.strip() == '':
            startmap = True
        elif startmap == True:
            mapnames.append(line.split(' ')[0])
            rules[mapnames[-1]] = []
            startmap = False
        else:
            rules[mapnames[-1]].append([int(x) for x in line.split(' ')])
    
    print("r1: ")
    r1 = []
    for s in seeds:
        for name in mapnames:
            s = processrule(name, s)
        r1.append(s)
    print("r2: ")
    minr2 = 1E20
    for n in range(0, len(seeds) // 2):
        for x in range(seeds[n*2+1]):
            if not x%10000000:
                print(x)
            r2 = seeds[n*2]+x
            for name in mapnames:
                r2 = processrule(name, r2)
            if r2 < minr2:
                minr2 = r2

    return min(r1), minr2       
            

if __name__ in ['__main__']:
    for fnam in ['dec05s.txt', 'dec05.txt']:
        with open(fnam) as file:
            result1, result2 = part1and2(file.readlines())
            print(result1)
            print(result2)