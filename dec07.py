# dec07.py
# Part 1,2 sample:
# 6440
# 5905
# Part 1,2 full:
# 248812215
# 250057090
# 

cstrengths = {'2':'a', '3':'b', '4':'c', '5':'d', '6':'e', '7':'f', '8':'g', '9':'h', 'T':'i', 'J':'j', 'Q':'k', 'K':'l', 'A':'m'}
def strength(hand):
    h = ''.join([cstrengths[c] for c in hand])  # make sortable
    hs = ''.join(sorted(h))
    if hs.count(hs[0]) == 5:  # five of a kind
        s = 'g'
    elif hs.count(hs[1]) == 4:  # four of a kind
        s = 'f'
    elif hs.count(hs[2]) == 3 and (hs.count(hs[0]) == 2 or hs.count(hs[4]) == 2):  # full house
        s = 'e'
    elif hs.count(hs[2]) == 3:  # three of a kind
        s = 'd'
    elif hs.count(hs[1]) == 2 and hs.count(hs[3]) == 2:  # two pair
        s = 'c'
    elif hs.count(hs[1]) == 2 or hs.count(hs[2]) == 2 or hs.count(hs[3]) == 2:  # one pair
        s = 'b'
    else:
        s = 'a'
    return s+h
        

def part1and2(data):
    # part 1
    cstrengths['J'] = 'j'
    hands = []
    for line in data:
        hand, bid = line.split(' ')
        bid = int(bid)
        hands.append([strength(hand), bid])
    hands.sort()
    tots = 0
    for n, h in enumerate(hands):
        tots += (n+1)*(h[1])
    # part 2
    cstrengths['J'] = 'A'
    hands = []
    for line in data:
        hand, bid = line.split(' ')
        bid = int(bid)
        if 'J' in hand:  # should we try some wildcarding?
            handts = []
            for i in range(5):  # build every possible replacement and sort them
                handts.append(strength(hand.replace('J', hand[i])))
            handts.sort()
            hands.append([handts[4][0]+strength(hand)[1:], bid]) # join best wild strength with original hand
        else:
            hands.append([strength(hand), bid])
    hands.sort()
    tots2 = 0
    for n, h in enumerate(hands):
        tots2 += (n+1)*(h[1])
    
    return tots, tots2      
            

if __name__ in ['__main__']:
    for fnam in ['dec07s.txt', 'dec07.txt']:
        with open(fnam) as file:
            result1, result2 = part1and2(file.readlines())
            print(result1)
            print(result2)