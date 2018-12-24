import sys
import re

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
    ip = int(re.findall('\d+', lines[0])[0])
    reg = [0] * 6
    ipv = 0

    #ipv = 11
    #reg = [0, 1, 0, 11, 10551367, 10551367]
    #reg = [1, 10551367, 0, 11, 10551367, 10551367]

    while True:
        if ipv >= (len(lines) - 1) or ipv < 0:
            break

        line = lines[ipv + 1]

        op, a, b, c = line.split()
        a = int(a); b = int(b); c=int(c)
        
        reg[ip] = ipv
        string = 'ip=%d ' % ipv
        string += ' %s ' % reg
        string += line 
        reg[c] = perform_op(op, a, b, reg)
        string += ' %s' % reg
        print string
        ipv = reg[ip]
        ipv += 1
    print reg[0]

def p2(lines):
    ip = int(re.findall('\d+', lines[0])[0])
    reg = [0] * 6
    reg[0] = 1
    ipv = 0

    ipv = 4 
    #reg  = [0, 1, 1, 4, 1, 10551367]
    #reg  = [0, 1, 10551367, 4, 10551367, 10551367]
    #reg  = [1, 2, 2, 4, 10551367, 10551367]
    #reg  = [1, 2801, 10551367, 4, 3767, 10551367]
    reg  = [2802, 2801, 10551368, 4, 3768, 10551367]
    #reg  = [2802, 2801, 10551368, 4, 10551367, 10551367]
    #reg  = [2802, 2802, 2802, 4, 1, 10551367]
    reg  = [2802, 3767, 10551367, 4, 2801, 10551367]
    reg  = [6569, 3768, 3768, 4, 1, 10551367]
    reg  = [6569, 10551367, 10551367, 4, 1, 10551367]
    reg  = [10557936, 10551367, 21102734, 4, 10551367, 10551367]

    for s in xrange(30):
            
        if ipv >= (len(lines) - 1) or ipv < 0:
            break

        line = lines[ipv + 1]

        op, a, b, c = line.split()
        a = int(a); b = int(b); c=int(c)
        
        reg[ip] = ipv
        string = 'ip=%d ' % ipv
        string += ' %s ' % reg
        string += line 
        reg[c] = perform_op(op, a, b, reg)
        string += ' %s' % reg
        print string
        ipv = reg[ip]
        ipv += 1
    print reg[0]

def p2_():
    divisors = [2801, 3767, 10551367]
    reg = [0, 1, 1, 4, 1, 10551367]
    i = 0
    div = 1
    reg2 = 1
    reg0 = 0
    reg1 = 1
    for div in divisors:
        reg4 = 10551367/div
        reg0 += reg1
        reg1 += 1
        reg2 = reg1
        i = 0
        div += reg1
        i += 1
    
if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        p2(lines)
        #p2_()

