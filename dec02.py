# Part 1:
# 8
# 
# Part 2:
# 
# 
# 

import string
if __name__ in ['exec','__main__']: # supports bugged runpython.org
    for fnam in ['dec02s.txt','dec02.txt']:
        with open(fnam) as file:
            print(part1(file.readlines()))
    for fnam in ['dec02s.txt','dec2s2.txt','dec02.txt']:
        with open(fnam) as file:
            print(part2(file.readlines()))
