import sys
import numpy as np
import matplotlib.pyplot as plt

def p1(lines):
    lumber = np.array([[c for c in line] for line in lines])
    N = lumber.shape[0]
    M = lumber.shape[1]
    totals = []
    
    for t in xrange(1000):
        lumber_n = lumber.copy()
        # top row
        for i in xrange(N):
            for j in xrange(M):
                prev_i = max(i-1, 0)
                next_i = min(i+2, N)
                prev_j = max(j-1, 0)
                next_j = min(j+2, N)
                adjacent = []
                for i_ in xrange(prev_i, next_i):
                    for j_ in xrange(prev_j, next_j):
                        if i_ != i or j_ != j:
                            adjacent.append(lumber[i_, j_])
                adjacent = np.array(adjacent)
                if lumber[i, j] == '.' and np.count_nonzero(adjacent == '|') > 2:
                    lumber_n[i, j] = '|'

                if lumber[i, j] == '|' and np.count_nonzero(adjacent == '#') > 2:
                    lumber_n[i, j] = '#'
                if lumber[i, j] == '#' and \
                (np.count_nonzero(adjacent == '#') < 1 or np.count_nonzero(adjacent == '|') < 1):
                    lumber_n[i, j] = '.'
        lumber = lumber_n
        #for i in xrange(lumber.shape[0]):
        #    print ''.join(lumber[i,:].tolist())
        num_lumber = np.count_nonzero(lumber == '#')
        num_wooded = np.count_nonzero(lumber == '|')
        total = num_lumber * num_wooded
        totals.append(total)
        print '\nafter %d  minutes there are %d' % ((t + 1), total)
    print 'there are %d lumber, %d wooded: %d' % (num_lumber, num_wooded, num_lumber * num_wooded)
    np.savetxt('totals.txt', totals)
    plt.plot(totals)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        print p1(lines)
