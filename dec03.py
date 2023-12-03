# dec03.py
# Part 1,2 sample:
# 4361
# 467835
# Part 1,2 full:
# 539713
# 84159075
# 

import string
from re import finditer

def part1and2(data):
    nums = {}
    syms = {}
    gears = {}

    def parsenums(lindex, line):
        for match in finditer("([0-9]+)",line):
            nums[(match.span()[0], lindex)] = (int(match.group()), match.span()[1]-match.span()[0])
        for match in finditer("([^0-9.])",line):
            syms[(match.span()[0], lindex)] = match.group()
                        
    for lindex, line in enumerate(data):
        parsenums(lindex, line.strip())
    totes = 0
    geartotes = 0
    # initialize dict of gears
    for sym in syms:
        if syms[sym] == '*':
            gears[sym] = []
    # check each number for neighboring symbols, gears
    for nloc in nums:
        ispartnum = False
        for col in range(nloc[0]-1, nloc[0]+nums[nloc][1]+1):
            if (col,nloc[1]-1) in syms:
                if (col, nloc[1]-1) in gears:
                    gears[(col, nloc[1]-1)].append(nums[nloc][0])
                ispartnum = True
            if (col,nloc[1]+1) in syms:
                if (col, nloc[1]+1) in gears:
                    gears[(col, nloc[1]+1)].append(nums[nloc][0])
                ispartnum = True
        if (nloc[0]-1, nloc[1]) in syms:
            if (nloc[0]-1, nloc[1]) in gears:
                gears[(nloc[0]-1, nloc[1])].append(nums[nloc][0])
            ispartnum = True
        if (nloc[0]+nums[nloc][1], nloc[1]) in syms:
            if (nloc[0]+nums[nloc][1], nloc[1]) in gears:
                gears[(nloc[0]+nums[nloc][1], nloc[1])].append(nums[nloc][0])
            ispartnum = True
        if ispartnum:
            totes += nums[nloc][0]
    # grab valid gears
    for gear in gears:
        if len(gears[gear]) == 2:
            geartotes += gears[gear][0]*gears[gear][1]
    return totes, geartotes
                
if __name__ in ['exec','__main__']: # supports bugged runpython.org
    for fnam in ['dec03s.txt', 'dec03.txt']:
        with open(fnam) as file:
            result1, result2 = part1and2(file.readlines())
            print(result1)
            print(result2)