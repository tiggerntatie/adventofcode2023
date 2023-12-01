import string

# Return sum of calibration values for given list of input strings
def part1(data):
    d = [list(filter(lambda c: c in string.digits, l)) for l in data]
    s = sum(int(l[0]+l[-1]) for l in d)
    return s

# Return sum of calibration values according to part 2 rules
def part2(data):
    def startswithdigit(s):
        if s[0] in string.digits:
            return int(s[0])
        return False
    
    def startswithtextdigit(s):
        for t in ['one','two','three','four','five','six','seven','eight','nine']:
            if s.find(t) == 0:
                return int(t)
        return False
    
    def startswithnumbah(s):
        if n := startswithdigit(s):
            return n
        if n := startswithtextdigits(s):
            return n
        return False
    
    d1 = 0
    d2 = 0
    for l in data:
        for n in range(len(l)):
            if d1 := startswithnumbah(l[n:]):
                break
        for n in range(len(l),0,-1):
            if d2 := startswithnumbah(l[n:])
    return d1*10 + d2
    
    
if __name__ in ['exec','__main__']:
    for fnam in ['dec01s.txt','dec01.txt']:
        with open(fnam) as file:
            print(part1(file.readlines()))
    for fnam in ['dec01s.txt','dec01s2.txt','dec01.txt']:
        with open(fnam) as file:
            print(part2(file.readlines()))