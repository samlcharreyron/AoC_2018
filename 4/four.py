import sys
import re
from datetime import datetime
from collections import defaultdict, namedtuple

def get_datetime(line):
    return datetime.strptime(re.search(r'\[(.)+\]', line).group(), '[%Y-%m-%d %H:%M]')

def sort_timestamps(lines):
    return sorted(lines, key=get_datetime)

def get_asleep(lines):
    num_min_asleep = defaultdict(int)
    gid = 0
    time_fa = None 
    time_wu = None

    min_asleep = defaultdict(lambda: [0]*59)

    for line in lines:
        gs = re.search('(?<=Guard #)(\d)+', line )
        gfas = re.search('falls asleep', line)
        gwus = re.search('wakes up', line)

        if gs:
            # guard starts
            gid = int(gs.group())

        if gfas:
            # guard falls asleep
            time_fa = get_datetime(line)

        if gwus:
            # guard wakes up
            time_wu = get_datetime(line)
            num_min_asleep[gid] += (time_wu - time_fa).seconds/60
            m_fa = time_fa.time().minute
            m_wu = time_wu.time().minute
            for i in xrange(m_fa, m_wu): min_asleep[gid][i] += 1

    return num_min_asleep, min_asleep

def get_p1(num_min_asleep, min_asleep):
    gid = max(num_min_asleep.iteritems(), key=lambda (k,v): v)[0]
    minute = max(range(0,59), key=lambda x: min_asleep[gid][x])
    return gid, minute

def get_p2(min_asleep):
    Record = namedtuple('Record', ('minute', 'num'))
    d = defaultdict(Record)
    for k, v in min_asleep.iteritems():
        minute = max(range(0,59), key=(lambda x: v[x]))
        num = max(min_asleep[k]) 
        d[k] = Record(minute, num)

    gid = max(d.iteritems(), key=lambda (k, v): v.num)[0]
    return gid, d[gid].minute

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        lines_s = sort_timestamps(lines)
        num_min_asleep, min_asleep = get_asleep(lines_s)

        gid, minute = get_p1(num_min_asleep, min_asleep)
        print 'p1: %d' % (gid * minute)

        gid, minute = get_p2(min_asleep)
        
        print 'p2: %d' % (gid * minute)
