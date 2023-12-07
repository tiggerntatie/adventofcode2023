# dec06.py
# Part 1,2 sample:
# 288
# 71503
# Part 1,2 full:
# 138915
# 27340847
#

from math import sqrt

def calcway(t, d):
    xt = (t + sqrt(t**2 - 4*d))/2
    nt = (t - sqrt(t**2 - 4*d))/2
    return int(xt-1E-10) - int(nt)
    

def part1and2(data):
    # part 1
    times = [int(x) for x in data[0].split(":")[1].split()]
    dists = [int(x) for x in data[1].split(":")[1].split()]
    ways = 1
    for t, d in zip(times,dists):
        ways *= calcway(t, d)
    # part 2
    t = int(''.join(data[0].split(":")[1].split()))
    d = int(''.join(data[1].split(":")[1].split()))
    
    return ways, calcway(t, d)
                        
if __name__ in ['__main__']:
    for fnam in ['dec06s.txt', 'dec06.txt']:
        with open(fnam) as file:
            result1, result2 = part1and2(file.readlines())
            print(result1)
            print(result2)