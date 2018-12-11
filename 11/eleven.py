import sys
import re
import numpy as np
import scipy.signal

def p1(ser):
    xg, yg = np.meshgrid(np.arange(1, 301), np.arange(1,301))
    rack_id = 10 + xg
    grid = rack_id * yg
    grid += ser
    grid *= rack_id
    grid = (grid / 100) % 10
    grid -= 5
    kernel = np.ones((3,3), np.int)
    powers = scipy.signal.convolve2d(grid, kernel, 'valid')
    idx = np.argmax(powers)
    position = np.unravel_index(idx, (298, 298))
    return np.max(powers), position[1] + 1, position[0] + 1
    
    #for i in xrange(298):
    #    for j in xrange(298):
    #        powers[i*298+j] = np.sum(grid[i:i+3,j:j+3])
    #        positions[i*298+j, :] = [j+1,i+1]
    #idx = np.argmax(powers)
    #return powers[idx], positions[idx]

def p2(ser):
    xg, yg = np.meshgrid(np.arange(1, 301), np.arange(1,301))
    rack_id = 10 + xg
    grid = rack_id * yg
    grid += ser
    grid *= rack_id
    grid = (grid / 100) % 10
    grid -= 5
    powers_ = np.zeros((300,))
    positions_ = np.zeros((300,2))
    print grid
    for k in xrange(1,30):
        print 'doing k: %d' % k
        w = 300 - k + 1
        kernel = np.ones((k,k), np.int)
        powers = scipy.signal.convolve2d(grid, kernel, 'valid')
        idx = np.argmax(powers)
        position = np.unravel_index(idx, (w, w))
        powers_[k] = powers[position]
        if k > 1 and powers_[k] < powers_[k-1]:
            break
        positions_[k,:] = [position[1] + 1, position[0] + 1]

    idx = np.argmax(powers_)
    return positions_[idx,:], idx

if __name__ == '__main__':
    print(p2(int(sys.argv[1])))
