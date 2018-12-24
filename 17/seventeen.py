import sys
from collections import defaultdict, namedtuple
import re

def p1(lines, display=False):
    m = defaultdict(lambda: '.')
    #m[complex(500, 0)] = '+'

    for line in lines:
        xstr = re.findall('x=\d+[..\d]*', line)[0]

        if '..' in xstr:
            xstart, xend = [int(c) for c in re.findall('\d+', xstr)]
        else:
            xstart = int(re.findall('\d+', xstr)[0])
            xend = xstart

        ystr = re.findall('y=\d+[..\d]*', line)[0]

        if '..' in ystr:
            ystart, yend = [int(c) for c in re.findall('\d+', ystr)]
        else:
            ystart = int(re.findall('\d+', ystr)[0])
            yend = ystart

        for i in xrange(xstart, xend+1):
            for j in xrange(ystart, yend+1):
                m[complex(i, j)] = '#'

    xmin = min(int(k.real) for k in m.keys()) - 1
    xmax = max(int(k.real) for k in m.keys()) + 1
    ymin = min(int(k.imag) for k in m.keys()) - 1
    ymax = max(int(k.imag) for k in m.keys()) + 1

    w_stack = []
    w_stack.append(complex(500, 1))

    while w_stack:
                
        w = w_stack.pop()

        if display:
            line = ''
            for y in xrange(int(w.imag)-5, int(w.imag)+20):
                for x in xrange(int(w.real)-20, int(w.real)+20):
                   line += m[complex(x, y)]
                line += '\n'
            print line
        
        n = w + complex(0,1)

        if n.imag > ymax:
            continue

        if m[n] not in '#~':
            m[w] = '|'
            w_stack.append(n)
        else:
            wall_right = False
            wall_left = False
            # find all right 
            for r in xrange(1, 1 + xmax - int(n.real)):
                if m[n + complex(r, 0)] in '~#': 
                    if m[w + complex(r,0)] == '#':
                        wall_right = True
                        break
                else:
                    break
                
            # find all left 
            for l in xrange(1, 1 + int(n.real) - xmin):
                if m[n + complex(-l, 0)] in '~#': 
                    if m[w + complex(-l, 0)] == '#':
                        wall_left = True
                        break
                else:
                    break

            if wall_left and wall_right:
                for i in xrange(1, l):
                    m[w + complex(-i, 0)] = '~'
                for i in xrange(1, r): 
                    m[w + complex(i, 0)] = '~'
                m[w] = '~'
                w_stack.append(w + complex(0, -1))
            else:
                for i in xrange(1, l):
                    m[w + complex(-i, 0)] = '|'
                for i in xrange(1, r): 
                    m[w + complex(i, 0)] = '|'
                m[w] = '|' 

                if not wall_left and not wall_right:
                    w_stack.append(w + complex(r, 0))
                    w_stack.append(w + complex(-l, 0))
                elif wall_left:
                    w_stack.append(w + complex(r, 0))
                else:
                    w_stack.append(w + complex(-l, 0))
    print len([k for k,v in m.iteritems() if v in '~|' and k.imag > ymin and k.imag < ymax])
    print len([k for k,v in m.iteritems() if v in '~' and k.imag > ymin and k.imag < ymax])

    line = ''
    for y in xrange(0, ymax):
        for x in xrange(xmin, xmax):
           line += m[complex(x, y)]
        line += '\n'
    with open('out.txt', 'w') as f:
        f.write(line)
    
            
        
if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        p1(lines)
