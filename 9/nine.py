import sys
from collections import defaultdict, deque

def p1(num_players=9, last_marble=25, display=False):
    scores = defaultdict(int)
    current = 0
    counter = 1
    marbles = [0]
    player = 0

    while counter != last_marble:
        if (counter % 23) == 0:
            current = (current - 7) 
            # convert to positive number
            if current < 0:
                current = len(marbles) + current
            removed = marbles.pop(current)
            scores[player] += (removed + counter)
        else:
            new_position = (current + 2) % len(marbles)
            if new_position == 0:
                marbles.append(counter)
                current = len(marbles) - 1
            else:
                marbles.insert(new_position, counter)
                current = new_position

        if display:
            before = ' '.join(str(x) for x in marbles[:current])
            after = ' '.join(str(x) for x in marbles[current+1:])
            print '[%d] %s [%d] %s' % (player+1, 
                    before, marbles[current], after) 

        player = (player + 1) % num_players
        counter += 1

    return max(scores.values()), len(marbles)

def p2(num_players=9, last_marble=25, display=False):
    scores = defaultdict(int)
    current = 0
    counter = 1
    marbles = deque([0])
    player = 0

    while counter != last_marble:
        if (counter % 23) == 0:
            # convert to positive number
            marbles.rotate(7)
            removed = marbles.pop()
            marbles.rotate(-1)
            scores[player] += (removed + counter)
        else:
            marbles.rotate(-1)
            marbles.append(counter)

        if display:
            marbles_l = list(marbles)
            before = ' '.join(str(x) for x in marbles_l[:current])
            after = ' '.join(str(x) for x in marbles_l[current+1:])
            print '[%d] %s [%d] %s' % (player+1, 
                    before, marbles_l[current], after) 

        player = (player + 1) % num_players
        counter += 1

    return max(scores.values())

if __name__ == '__main__':
    print p2(int(sys.argv[1]), int(sys.argv[2]))


