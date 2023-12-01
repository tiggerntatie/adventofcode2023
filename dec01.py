import string

def part1(data):
    d = [filter(lambda c: c in string.digits, l) for l in data]
    return d
    
if __name__ == '__main__':
    with open(fnam) as file:
        print(part1(file.readlines))