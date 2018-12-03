import sys
from collections import Counter
from itertools import combinations
#from itertools import accumulate

def process_line(line):
    c = Counter(line)
    return c.values().count(2), c.values().count(3)

def process_total(lines):
    # twos = 0
    # threes = 0 
    #     
    # for line in lines:
    #     x, y = process_line(line)
    #     if x:
    #         twos += 1
    #     if y:
    #         threes +=1

    # return twos * threes

    twos = (process_line(line)[0] > 0 for line in lines)
    threes = (process_line(line)[1] > 0 for line in lines)
    return sum(twos) * sum(threes)

def num_same_letters(word_a, word_b):
    return sum(a==b for a,b in zip(word_a, word_b))

def correct_boxes(line_l): 
    for word_a, word_b in combinations(line_l, 2):
        if num_same_letters(word_a, word_b) == (len(word_a) - 1):
            return word_a, word_b

def get_common_letters(word_a, word_b):
    return ''.join(a for a,b in zip(word_a, word_b) if a == b)

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        print process_total(lines)
        print get_common_letters(*correct_boxes(lines))
