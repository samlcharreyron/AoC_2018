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

    #reg[0] = 16311888

    #ipv = 18
    #reg = [0, 256, 65536, 3345805, 18, 0]

    while True:
        if ipv == 28:
            print reg
            #print reg[3]

        if ipv >= (len(lines) - 1) or ipv < 0:
            break

        line = lines[ipv + 1]

        op, a, b, c = line.split()
        a = int(a); b = int(b); c=int(c)
        
        reg[ip] = ipv
        #string = 'ip=%d ' % ipv
        #string += ' %s ' % reg
        #string += line 
        reg[c] = perform_op(op, a, b, reg)
        #string += ' %s' % reg
        #print string
        #print ipv
        ipv = reg[ip]
        ipv += 1


def p2():
    D = 0
    seen = []
   
    while True:
        # 6
        C = (D | 65536)
        D = 10736359

        while True:
            # 8
            B = C & 255
            #D = D + B 
            #D = D & 16777215
            #D = D * 65899
            #D = D & 16777215
            D = (((D + B) & 16777215) * 65899) & 16777215

            if C < 256:
                if D in seen:
                    return seen[-1]
                #print D
                seen.append(D)
                # goto 6
                break
            else:
                B = 0
                C = C // 256
                #while True:
                #    # 18
                #    E = (B + 1) * 256
                #    if E > C:
                #        C = B
                #        break
                #        # goto 8
                #    else:
                #        B += 1
                #        # goto 18

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        #p1(lines)
        print p2()
