import string

def part1(data):
    d = [filter(lambda c: c in string.digits, list(l)) for l in data]
    return d
    
print (__name__)
if __name__ == 'exec':
    for fnam in ['dec01s.txt','dec01.txt']:
        with open(fnam) as file:
            print(part1(file.readlines))