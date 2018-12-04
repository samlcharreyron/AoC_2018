#! /usr/bin/env python
import sys
from collections import defaultdict

def decode(input_str):
    return sum((int(x) for x in input_str.split()))

def decode2(input_str):
    d = defaultdict(int)
    
    current = 0
    d[0] = 1
    while True:
        for x in input_str.split():
            current += int(x)
            if d.get(current):
               return current 
            d[current] += 1

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        input_str = f.read()
        print 'first sum: %d' % decode(input_str)
        print 'first freq obtained twice: %d' % decode2(input_str) 
