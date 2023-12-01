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
            return s[0]
        return False
    
    def startswithtextdigit(s):
        for t in ['one','two','three','four','five','six','seven','eight','nine']:
            if s.find(t) == 0:
                return t
        return False
    
    d1 = ''
    d2 = ''
    for l in data:
        for n in range(len(l)):
            if d := startswithdigit(l[n:]):
                break
            if d := startswithtextdigits(l[n:]):
                break
        d1 = d
        for n in range(len(l))
        
    
    
if __name__ in ['exec','__main__']:
    for fnam in ['dec01s.txt','dec01.txt']:
        with open(fnam) as file:
            print(part1(file.readlines()))
    for fnam in ['dec01s.txt','dec01s2.txt','dec01.txt']:
        with open(fnam) as file:
            print(part2(file.readlines()))