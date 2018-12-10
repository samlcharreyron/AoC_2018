import sys
import re
import numpy as np

def p1(lines):
    positions = []
    velocities = [] 
    for line in lines:
        m = re.findall('[+-]?\d+', line)
        x = int(m[0])
        y = int(m[1])
        vx = int(m[2])
        vy = int(m[3])
        positions.append([x, y])
        velocities.append((vx, vy))
    positions = np.array(positions)
    positions_o = positions.copy()
    velocities = np.array(velocities)

    xmin, ymin = np.min(positions, axis=0)
    xmax, ymax = np.max(positions, axis=0)
    
    last = xmax - xmin

    i = 0
    for i in xrange(12000):
        #print('\nstep %d\n' % i)
        xmin, ymin = np.min(positions, axis=0)
        xmax, ymax = np.max(positions, axis=0)

        current = xmax - xmin

        if current > last:
            print 'done after %d' % i
            #message = np.zeros((ymax + 1 - ymin, xmax + 1 - xmin), np.uint8)
            #message[-ymin + positions[:,1], -xmin + positions[:,0]] = 1
            #print('\n'.join(''.join('#' if cell else '.' for cell in row) for row in message))
            break
        
        last = current
        positions += velocities

    positions = positions_o
    for j in xrange(i-1):
        positions += velocities
        
    xmin, ymin = np.min(positions, axis=0)
    xmax, ymax = np.max(positions, axis=0)
    message = np.zeros((ymax + 1 - ymin, xmax + 1 - xmin), np.uint8)
    message[-ymin + positions[:,1], -xmin + positions[:,0]] = 1
    print('time taken %d, message' % (i-1))
    print('\n'.join(''.join('#' if cell else '.' for cell in row) for row in message))

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        p1(lines)
