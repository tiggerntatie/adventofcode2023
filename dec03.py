# dec03.py
# Part 1,2 sample:
# 4361
# 467835
# Part 1,2 full:
# 539713
# 84159075
# 

import string

def part1and2(data):
    nums = {}
    syms = {}
    gears = {}

    def parsenums(lindex, line):
        searching = True
        num = 0
        cindex = 0
        for n, c in enumerate(line):
            if searching: # searching for a number
                if c in string.digits: # found a first digit
                    searching = False
                    cindex = n
                    num = int(c)
                elif c != '.':
                    syms[(n, lindex)] = c # found a symbol                
            else: # not searching (inside number)
                if c not in string.digits: # end of a number
                    searching = True
                    nums[(cindex, lindex)] = (num, len(str(num))) # found a number
                    num = 0
                    if c != '.':
                        syms[(n, lindex)] = c # symbol at the end
                else:
                    num = num*10 + int(c)
        # clean up end of line search
        if not searching:
            nums[(cindex, lindex)] = (num, len(str(num))) # found a number
                
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