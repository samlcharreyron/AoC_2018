import sys
import numpy as np
from collections import defaultdict 
import networkx as nx

dmap = defaultdict(lambda:'?')
G = nx.Graph()

def process_group(line, xb=0, yb=0):
    x, y = xb, yb
    i = 0
    while line[i] != '$': 
        c = line[i]

        if c == '(':
            r = process_group(line[i+1:], x, y)
            i = i + r +1
        elif c in ')':
            return i+1 

        elif c == '|':
            x, y = xb, yb
            i+=1

        elif c == 'S':
            G.add_edge((x,y), (x+2,y))
            dmap[(x+1, y-1)] = '#'
            dmap[(x+1, y)] = '-'
            dmap[(x+1, y+1)] = '#'
            dmap[(x+2, y)] = '.'
            x += 2
            i+=1
        elif c == 'N':
            G.add_edge((x,y), (x-2,y))
            dmap[(x-1, y-1)] = '#'
            dmap[(x-1, y)] = '-'
            dmap[(x-1, y+1)] = '#'
            dmap[(x-2, y)] = '.'
            x -= 2
            i+=1
        elif c == 'E':
            G.add_edge((x,y), (x,y+2))
            dmap[(x-1, y+1)] = '#'
            dmap[(x, y+1)] = '|'
            dmap[(x+1, y+1)] = '#'
            dmap[(x, y+2)] = '.'
            y += 2
            i+=1
        elif c == 'W':
            G.add_edge((x,y), (x,y-2))
            dmap[(x-1, y-1)] = '#'
            dmap[(x, y-1)] = '|'
            dmap[(x+1, y-1)] = '#'
            dmap[(x, y-2)] = '.'
            y -= 2
            i+=1

def print_map():
    xmin = min(x for (x,y) in dmap)
    xmax = max(x for (x,y) in dmap)
    ymin = min(y for (x,y) in dmap)
    ymax = max(y for (x,y) in dmap)

    mapstr = ''
    for x in xrange(xmin, xmax+1):
        for y in xrange(ymin, ymax+1):
            if dmap[(x,y)] == '?':
                mapstr += '#'
            else:
                mapstr += dmap[(x,y)]
        mapstr += '\n'
    print mapstr

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        line = f.readline().strip()
        dmap[(0,0)] = 'X'
        process_group(line[1:])
        print_map()

        paths = nx.shortest_path(G, source=(0,0))
        lengths = [len(p)-1 for p in paths.values()]
        print max(lengths)
        print len([l for l in lengths if l >= 1000])
