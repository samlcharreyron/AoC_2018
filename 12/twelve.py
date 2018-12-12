import sys
import re
from collections import defaultdict
import numpy as np

def p1(lines, neg=2000, pos=2000, N=20):
    initial_state = lines[0].split()[2]
    state = neg * '.' + initial_state + pos * '.'
    idx = [-3 + c for c in xrange(len(state))]
    rules = []
    for line in lines[2:]:
        ns = line[-1]
        pred = line[0:5]
        rule = {'pred': pred, 'next': ns}
        rules.append(rule)

    #print('0: %s' % (state))
    ss_ = 0 
    sums = []
    for i in xrange(N):
        new_state_l = ['.'] * len(state)
        for rule in rules:
            matches = re.finditer('(?=(' + re.escape(rule['pred']) + '))', state)
            for m in matches:
                #state_l = list(state)
                new_state_l[m.start()+2] = rule['next']
        state = ''.join(new_state_l)
        #print('%d: %s' % (i+1, state))

        ss = sum(i-neg if c == '#' else 0 for i,c in enumerate(state))
        sums.append(ss)
        print(i)
        if ss == ss_:
            break
    np.savetxt('sums.txt', sums)
        

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        p1(lines, N=1000)

