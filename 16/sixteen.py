import sys
import re
import copy
from collections import defaultdict

OPCODES = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
        'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def perform_op(op, a, b, reg):
    if op == 'addr':
        return reg[a] + reg[b]
        
    if op == 'addi':
        return reg[a] + b

    if op == 'mulr':
        return reg[a] * reg[b]

    if op == 'muli':
        return reg[a] * b

    if op == 'banr':
        return reg[a] & reg[b]

    if op == 'bani':
        return reg[a] & b

    if op == 'borr':
        return reg[a] | reg[b]

    if op == 'bori':
        return reg[a] | b
    
    if op == 'setr':
        return reg[a]

    if op == 'seti':
        return a

    if op == 'gtir':
        return int(a > reg[b])

    if op == 'gtri':
        return int(reg[a] > b)

    if op == 'gtrr':
        return int(reg[a] > reg[b])

    if op == 'eqir':
        return int(a == reg[b])

    if op == 'eqri':
        return int(reg[a] == b)

    if op == 'eqrr':
        return int(reg[a] == reg[b])

def p1(lines):
    samples = 0
    d_opcode = defaultdict(set)
    d_cand = defaultdict(set)
    for line in lines:
        if line == '':
            break

        lines_ = line.split('\n')

        reg_before = [int(ch) for ch in re.findall('\d+', lines_[0])] 
        op_code, a, b, c = [int(ch) for ch in re.findall('\d+', lines_[1])]
        reg_after = [int(ch) for ch in re.findall('\d+', lines_[2])]

        candidates = []
        for op in OPCODES:
            reg = copy.copy(reg_before)
            reg[c] = perform_op(op, a, b, reg_before)
            if reg == reg_after:
                candidates.append(op)
        if len(candidates) > 2:
            samples += 1
        for cand in candidates:
            #d_opcode[cand].add(op_code)
            d_cand[op_code].add(cand)

    print samples

    finished = set()
    while len(finished) < len(OPCODES):
        to_remove = []
        for opcode, cands in d_cand.iteritems():
            if len(cands) < 2 and (opcode not in finished): 
                cand = cands.pop()
                cands.add(cand)
                to_remove.append((cand, opcode))
        for cand, opcode in to_remove:
            print 'removing %d' % opcode
            finished.add(cand)
            for o, cands in d_cand.iteritems():
                if cand in cands:
                    if o!= opcode:
                        cands.remove(cand)
                    else:
                        d_cand[opcode] = cand
    return d_cand

def p2(lines, d_cand):
    reg = [0]*4
    for line in lines:
        opcode, a, b, c = [int(c) for c in re.findall('\d+', line)]
        op = d_cand[opcode]
        reg[c] = perform_op(op, a, b, reg) 

    print 'contents of reg 0: %d' % reg[0]

if __name__ == '__main__':
    with open(sys.argv[1]) as f: 
        part1, part2 = f.read().split(';')
        d_cand = p1(part1.split('\n\n'))
        p2(part2.splitlines()[1:], d_cand)
