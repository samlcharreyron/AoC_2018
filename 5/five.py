import sys
from collections import defaultdict

def react(reacted):
    stack = []

    for c in reacted:
        if stack:
            if stack[-1] == c.swapcase():
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    return len(stack)

def p2(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = defaultdict(int)

    for l in alphabet:
        string_ = string.replace(l, '')
        string_ = string_.replace(l.upper(), '')
        d[l] = react(string_)
        print 'removed %s, length: %d' %(l, d[l])

    return min(d.values())

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        string = f.readline().split()[0]
        print 'p1 before: %d, after: %d' % (len(string), react(string))
        print 'p2 %d' % p2(string)
