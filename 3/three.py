import sys
from collections import defaultdict
import re

def add_to_map(cid, y, x, cols, rows, cmap):
    cmap[(y,x)].append(cid) 

def process_code(string):
    cid = int(re.search('(?<=#)(\d)+(?= @)', string).group())
    y = int(re.search('(?<=@ )(\d)+(?=,)', string).group())
    x = int(re.search('(?<=,)(\d)+(?=:)', string).group())
    cols = int(re.search('(?<=: )(\d)+(?=x)', string).group())
    rows = int(re.search('(?<=x)(\d)+$', string).group())
    return cid, y, x, cols, rows

def get_cids(strings):
    return set(process_code(string)[0] for string in strings)

def get_cmap(strings):
    cmap = defaultdict(set)
    for string in strings:
        cid, ly, tx, cols, rows = process_code(string)
        for y in xrange(ly, ly+cols): 
            for x in xrange(tx, tx+rows):
                cmap[(y, x)].add(cid)
    return cmap

def count_cmap(cmap):
    return sum(len(v) > 1 for k, v in cmap.iteritems())

def find_intact(strings):
    cids = get_cids(strings)
    cmap = get_cmap(strings)
    overlapping = set()
    for k, v in cmap.iteritems():
        if len(v) > 1:
            overlapping = overlapping.union(v)
    return cids.difference(overlapping)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        print count_cmap(get_cmap(lines))
        print find_intact(lines)


