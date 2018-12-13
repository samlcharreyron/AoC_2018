import sys
from collections import defaultdict

class Car(object):
    def __init__(self, cid, position, direction, turn=0):
        self.id = cid 
        self.position = position
        self.direction = direction
        self.turn = turn

    def __repr__(self):
        return 'Car(%d, %s, %s, %s)' % (self.id, self.position, self.direction,
                self.turn)

DIRECTIONS = '>v<^'
# turn [left, straight, right]

def p1(lines, print_map=True, N=1000):
    cars = []
    dmap = defaultdict(str)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in '<>^v':
                cars.append(Car(len(cars), (i,j), DIRECTIONS.find(c)))
                if c in '<>':
                    dmap[(i, j)] = '-'
                elif c in 'v^':
                    dmap[(i,j)] = '|'
            else:
                dmap[(i, j)] = c

    xmax = max(p[0] for p in dmap.keys())
    ymax = max(p[1] for p in dmap.keys())

    # prepare map
    if print_map:
        map_str = ''
        for x in xrange(xmax+1):
            for y in xrange(ymax+1):
                if dmap[(x,y)]:
                    map_str += dmap[(x,y)]
                else:
                    map_str += ' '
            map_str += '\n'

        print map_str

    if print_map:
        print '0, %s' % cars

    for t in xrange(N):
        for car in cars:
            new_position = car.position
            if car.direction == 0: 
                new_position = (new_position[0], new_position[1] + 1)

            elif car.direction == 1:
                new_position = (new_position[0] + 1, new_position[1])

            elif car.direction == 2:
                new_position = (new_position[0], new_position[1] - 1)

            elif car.direction == 3:
                new_position = (new_position[0] - 1, new_position[1])

            if dmap[car.position] == '-' and dmap[new_position] == '\\':
                # turn right
                car.direction = (car.direction + 1) % 4

            if dmap[car.position] == '-' and dmap[new_position] == '/':
                # turn left
                car.direction = (car.direction + 3) % 4

            if dmap[car.position] == '|' and dmap[new_position] == '/':
                # turn right
                car.direction = (car.direction + 1) % 4

            if dmap[car.position] == '|' and dmap[new_position] == '\\':
                # turn left
                car.direction = (car.direction + 3) % 4

            if dmap[new_position] == '+':
                if car.turn == 0:
                    car.direction = (car.direction + 3) % 4
                if car.turn == 2:
                    car.direction = (car.direction + 1) % 4

                car.turn = (car.turn + 1) % 3

            # crash
            if new_position in [car_.position for car_ in cars if car_.id != car.id]:
                return new_position, t

            car.position = new_position
        
        cars.sort(key=lambda c: c.position[0] * ymax + c.position[1])
        if print_map:
            print '%d, %s' % (t+1, cars)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        print p1(lines, False, 1000)

