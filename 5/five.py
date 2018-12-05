import sys
from collections import defaultdict

def reacts(tg):
    return (tg[0].isupper() and tg[0].lower() == tg[1]) or \
    (tg[0].islower() and tg[0].upper() == tg[1])

def react_once(string):
    # group (0,1) ...
    tg_l = [''.join(x) for x in zip(*[iter(string)]*2)]
    reacted = ''.join([tg for tg in tg_l if not reacts(tg)])
    
    # group (1,2) ...
    if len(reacted) > 2:
        tg_l = [''.join(x) for x in zip(*[iter(reacted[1:-1])]*2)]
        reacted = reacted[0] + ''.join([tg for tg in tg_l if not reacts(tg)]) + reacted[-1]

    return reacted

def react(reacted):
    stop = False

    while not stop:
        if reacted == '':
            return reacted
        reacted_ = react_once(reacted)
        stop = reacted_ == reacted
        reacted = reacted_

    return reacted

def p2(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = defaultdict(int)

    for l in alphabet:
        string_ = string.replace(l, '')
        string_ = string_.replace(l.upper(), '')
        reacted = react(string_)
        d[l] = len(reacted)
        print 'removed %s, length: %d' %(l, d[l])

    return min(d.values())

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        string = f.readline().split()[0]
        print 'p1 before: %d, after: %d' % (len(string), len(react(string)))
        print 'p2 %d' % p2(string)
