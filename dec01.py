import string

def part1(data):
    d = [list(filter(lambda c: c in string.digits, l)) for l in data]
    s = sum(int(l[0]+l[-1]) for l in d)
    return s
    
print (__name__)
if __name__ == 'exec':
    for fnam in ['dec01s.txt','dec01.txt']:
        with open(fnam) as file:
            print(part1(file.readlines()))