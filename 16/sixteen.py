import sys
import re
from itertools import islice

OPCODES = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
        'setr', 'seto', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

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
    for line in lines:
        if line == '':
            break

        lines_ = line.split('\n')

        reg_before = [int(ch) for ch in re.findall('\d+', lines_[0])] 
        op_code, a, b, c = [int(ch) for ch in re.findall('\d+', lines_[1])]
        reg_after = [int(ch) for ch in re.findall('\d+', lines_[2])]

        candidates = []
        for op in OPCODES:
            reg = reg_before
            reg[c] = perform_op(op, a, b, reg_before)
            if reg == reg_after:
                candidates.append(op)
        if len(candidates) > 2:
            samples += 1
    return samples

if __name__ == '__main__':
    with open(sys.argv[1]) as f: 
        lines = f.read().split('\n\n')
        print p1(lines)
